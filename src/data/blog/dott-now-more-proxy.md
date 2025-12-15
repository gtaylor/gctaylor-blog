---
author: Greg Taylor
pubDatetime: 2011-08-30T04:31:00+00:00
modDatetime:
title: dott - now with more proxy
slug: dott-now-more-proxy
featured: false
draft: false
tags: ["Mud", "Python", "Programming"]
description: ""
---

As mentioned in my previous post about [putting a MUD behind a proxy](http://gc-taylor.com/blog/2011/8/2/mud-behind-proxy-potentially-great/),I’ve been really intrigued by some of the things such a setup would
allow. In fact, my motivation was enough to warrant actually trying to
implement my own interpretation. My implementation of this split
proxy/MUD setup has now been merged into my master branch of [dott on
GitHub](https://github.com/gtaylor/dott) (my tinker MUD that I work on when I get the urge).

A quick refresher
-----------------

For those who haven’t read the [first article](http://gc-taylor.com/blog/2011/8/2/mud-behind-proxy-potentially-great/), or are too lazy to do
so, what I’m doing is sticking a proxy in front of a MUD server. The
proxy is the only one of the two that handles telnet connections,
maintaining them even if the MUD server is down or restarting. In my
case, the proxy also handles authentication and account creation, but
this is entirely optional, and just something I wanted. The MUD server
only handles game world related stuff: rooms, objects, combat, AI, etc.

The primary benefit of this setup is that instead of dealing with messy
live, “seamless” code reloading, I just shutdown and restart the MUD
server without alerting the players. The proxy maintains the
connections, and the MUD server’s startup procedures are fast enough to
where very few players will ever notice that the game went down and back
up. If the MUD server is down, the player will get a “The MUD is
currently re-loading” message telling them to try again in a few seconds.

How it works
------------

Since my tinker project, [dott](https://github.com/gtaylor/dott), is built with Python and the excellent
[Twisted](http://twistedmatrix.com/trac/) framework, I had access to [AMP](http://amp-protocol.net/), a very simple async
messaging protocol. This allows for bi-directional communication between
the proxy and the MUD server. The proxy can do stuff like pipe commands
to the MUD server through various objects, and the MUD server can tell
the proxy to emit messages to any player controlling an object.

Beginning with the startup process, the [proxy](https://github.com/gtaylor/dott/blob/master/proxy.tac) fires up, starting a
telnet server factory to accept telnet connections from players. It
imports the [MUD server](http://github.com/gtaylor/dott/blob/master/server.tac)‘s [proxyamp](https://github.com/gtaylor/dott/blob/master/src/server/protocols/proxyamp.py) module, which contains protocol
definitions and an auto-reconnecting client factory used to communicate
with the [MUD server](http://github.com/gtaylor/dott/blob/master/server.tac). Both the
[proxy](http://github.com/gtaylor/dott/blob/master/proxy.tac) and the
[MUD server](http://github.com/gtaylor/dott/blob/master/server.tac) use the same ProxyAMP class and its commands contained within.

The [MUD server](http://github.com/gtaylor/dott/blob/master/server.tac) is started up, and the
[proxy](http://github.com/gtaylor/dott/blob/master/proxy.tac)
auto-retries its AMP client-> server connection and finds the [MUD
server](http://github.com/gtaylor/dott/blob/master/server.tac) reachable over AMP. A connection is established, and the two
pieces return to working together.

Nuances
-------

* Both the proxy and MUD server are monitored with [supervisor](http://supervisord.org/index.html). If
  either of the two go down, supervisor immediately re-starts them. My
  @reload command simply shuts down the MUD server. Supervisor sees the
  exit and restarts it for me with very little delay. The proxy
  maintains connections and things automatically pick right back up
  where they left of, when the MUD server returns.
* The MUD server and proxy can be restarted independently and in any
  order. Shutting down and starting up the proxy leads to no ill
  effects for the MUD server. It’d just boot the players. Restarting
  the MUD server leads to no discernible interruption, unless the
  player types a command. In that case, they get an error message
  telling them to try again in a few seconds.
* The proxy server handles any protocol-specific display stuff. I’ll
  eventually be doing room descriptions in some form of markup. The
  proxy would parse the markup and replace it with the appropriate
  color/formatting codes for the protocol. For telnet, this would be
  ANSI color, for a theoretical future WebSocket-based client, this
  might be JSON or HTML. The important thing to grasp here is that the
  MUD server is just handling game stuff, which is really neat.

AMP enables the building of distributed MUDs
--------------------------------------------

*The following is rambling just for the sake of illustration. I don’t
have any immediate plans to do any of the following, since MUDs are not
at all resource-intensive, and are best kept simple. With that said…*

If one were so inclined, next steps might be breaking out various
complicated systems into their own separate services. For example, maybe
we have an authentication service that the proxy communicates with over
AMP for logging users in. Your website could then also communicate with
this authentication service (just like the proxy), instead of hitting
the MUD server directly (I don’t really like the idea of hitting a MUD
server with web-related traffic). Creating new accounts from the web
uses the same plumbing as the proxy.

Or maybe you run a Twisted IMAP service for your game’s mail. Users
within the game using mail commands would be reading their mail via AMP
messages to the mail service that runs outside of the game. Those with
IMAP-enabled clients could hit the mail service separately, instead of
hitting a baked-into-the-mud service with potential denial of service or
security issues.

Another possible external service would be AI and/or a real-time combat
system. The combat system service could handle the ticks, coordinates,
and AI stuff that may be resource-intensive, messaging the MUD server
when stuff happens. Users steering or moving things around would send
AMP messages to the combat system letting it know to change states. This
is a cheap way to make use of multi-core machines, if you really need it.

Feedback, ideas, and whatever else
----------------------------------

Coming back to reality for a second, I’d love to get some more eyes on
the code ([on GitHub](https://github.com/gtaylor/dott)), or hear any ideas you may have. Please feel
free to reply below with a comment. I am writing this stuff for myself
for my own selfish use, but constructive criticism is welcome and
encouraged. The unit testing is marginal at best at the moment, as I’m
trying to figure out the best way to test AMP. However, I’ve tried to
make sure the docstrings are detailed.

If there are any slick capabilities that this setup enables, but I
haven’t mentioned them in either post, do speak up in case I missed
them. There hasve already been some comments that pointed out things I
never thought of.
