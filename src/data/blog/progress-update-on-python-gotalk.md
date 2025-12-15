---
author: Greg Taylor
pubDatetime: 2015-02-06T22:30:00+00:00
modDatetime:
title: Progress update on python-gotalk
slug: progress-update-on-python-gotalk
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

As covered in a [previous post](http://gc-taylor.com/blog/2015/01/23/lets-player-python-gotalk/), I’ve been tinkering with a Pythonimplementation of the fledgling [Gotalk](https://github.com/rsms/gotalk). Since this has been fun to play with,
I figured it’d be worth sharing where python-gotalk is, and what has happened
with it in the last two weeks.

Upstream gotalk progress
------------------------

Rasmus has created a new protocol [v1 branch](https://github.com/rsms/gotalk/tree/v1) in the [Gotalk](https://github.com/rsms/gotalk) repo, where all of
the new hotness is landing. A few hilights:

* Request IDs have grown from three bytes to four in response to requests for
  more potential permutations.
* A new ProtocolError message type was added. This is sent when a peer doesn’t
  understand the protocol version specified by the sender. While I haven’t
  seen any specifics on how potential downgrades may work, this could
  conceivably be used to handle that in the future (maybe?). It is not clear
  if gotalk is striving for any kinds of backwards compatibility between
  protocol versions, so that’ll be something to watch.
* The Go and JS example client/servers have progressed quite a bit.

python-gotalk updates
---------------------

At this point in time, we should be current with the gotalk [v1 branch](https://github.com/rsms/gotalk/tree/v1) wire
format (as of the night of Feb 6). I haven’t started on any socket/state
tracking stuff, and probably won’t until v1 is mostly solidified.

However, I’ve thought about keeping python-gotalk focused on just the message
marshalling/unmarshalling. The socket/state tracking code will differ quite
a bit depending on whether you are using Twisted, asyncio, Tornado, etc. It’d
also mean that python-gotalk could avoid all external dependencies.

We’ll continue tracking the Gotalk [v1 branch](https://github.com/rsms/gotalk/tree/v1) and see how it goes!
