---
author: Greg Taylor
pubDatetime: 2011-08-02T05:41:00+00:00
modDatetime:
title: A MUD behind a proxy is… potentially great
slug: mud-behind-proxy-potentially-great
featured: false
draft: false
tags: ["Mud", "Python", "Programming"]
description: ""
---

My perpetual tinker project is a [MUD server](https://github.com/gtaylor/dott) that may or may not eversee the light of day. In recent adventures, I pursued [using Exocet](http://gc-taylor.com/blog/2011/7/20/exocet-makes-code-reloading-easy/) to
make my goal of a mostly interruption-less experience for the players a
reality. The attempt worked in most cases, but failed horribly in a few
others. The failures were bad enough to make me scrap the idea. The next
best thing I could think of is to stick a proxy server in front of the
MUD server.

The proxy would handle all of the telnet protocol and session stuff, and
just dumbly pipe input into the MUD server through Twisted’s [AMP](http://twistedmatrix.com/documents/current/api/twisted.protocols.amp.html) (a
really neat, simple, 2-way protocol). When a user inputs something, the
proxy says to MUD server “A session attached to an Object with an ID of
“a20dl3da” input this. The MUD server would then have any object matches
route the input through whatever command tables they are subscribed to,
causing things to happen in-game.

Communication back to the proxy would happen whenever an an Object’s
emit method (IE: print to any sessions controlling this object). The
proxy would see if it had a session attached to the given object, and
call the TelnetProtocol’s msg() method with the output.

Neat thing #1: Strictly enforced separation
-------------------------------------------

Convention typically dictates that connection and protocol-level things
be kept separate from business logic and other more interesting things.
However, having separate proxy and MUD server sections of the codebase
really enforces that separation in my mind.

Keeping session and protocol-level gunk confined to the proxy makes the
MUD server easier to understand, maintain, and test. I find this layout
a little easier to mentally digest.

The other cool thing in the future is that adding support for other
protocols (websockets, anyone?) can be handled in the proxy, hooking the
input/output into AMP commands. Protocols are already in their own
island with Twisted, but this separation is much more strictly enforced
under this arrangement (which again, I like). The MUD server can speak
in a protocol-agnostic format like Markdown or BBcode, and the protocols
can format the output for whatever they are serving.

Neat thing #2: Neither proxy nor MUD server care if the other dies
------------------------------------------------------------------

Consider the following two scenarios:

* *MUD server dies, proxy stays up.*

  The proxy accepts connections, but all input is left with an error
  message telling the user to stay put until the MUD comes back up. All
  sessions are maintained, and Twisted’s [auto-reconnection
  facilities](http://twistedmatrix.com/documents/current/core/howto/clients.html#auto4) continuously tries to get back in touch with the MUD.
  When it does come back up, business continues as usual without
  interruption. The MUD server doesn’t care about sessions, and the
  proxy doesn’t care about in-game objects, rooms, and etc.
* *The proxy goes down, but the MUD server stays up.*

  This one isn’t quite as neat. In theory, this scenario should be
  extremely rare. If the proxy goes down, the user is unable to connect
  to the running game. They’ll need to re-connect once the proxy comes
  back up. However, the MUD server continues about its business in the
  meantime, so mobs are moving, the economy is ticking, etc. Once the
  proxy is back, it re-connects and players can interact with the game
  world again.

Neat thing #3: We don’t need to bother with code re-loading
-----------------------------------------------------------

The last, and most important, neat thing is that because of neat things
#1 and #2, we don’t need to implement code re-loading. If both proxy and
MUD server are monitored/auto-restarted by something like [Supervisor](http://supervisord.org/),
the latest version of the game code can be loaded by silently shutting
down the MUD server (but leaving the proxy up). Supervisor (or runit, or
launchctl, or whatever) sees the server process down, restarts it, and
the proxy automatically re-connects as soon as it’s back up.

The end result is that the user may get an error or two if they’re
trying to type stuff while the server is down, but the outage should be
short and potentially completely unnoticed by some of the players. We
don’t need to worry about all of the messyness associated with code
reloading, and we can keep the MUD server focused on game logic.

Code to come
------------

I’ve got a proof-of-concept for this arrangement “working”, but it’ll be
some time before I am able to restore the existing features of the MUD
server to work with the new proxy + MUD server model. I’ll continue to
write posts about progress as it happens.
