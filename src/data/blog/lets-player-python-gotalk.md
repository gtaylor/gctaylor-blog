---
author: Greg Taylor
pubDatetime: 2015-01-23T00:55:00+00:00
modDatetime:
title: Let’s play: python-gotalk
slug: lets-player-python-gotalk
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

A recent [HackerNews post](https://news.ycombinator.com/item?id=8930426) announced [Gotalk](https://github.com/rsms/gotalk), a simple bidirectional protocol.I can imagine your collective eyeballs rolling. “Oh great, yet another
half-baked way for… things to talk to one other”. But keep following along,
maybe you’ll see something you like. Here are some highlights:

* **By Rasmus Andersson** - You may know him from his work at Facebook,
  Spotify, and Dropbox.
* **Bidirectional** — There’s no discrimination on capabilities depending on
  who connected or who accepted. Both “servers” and “clients” can expose
  operations as well as send requests to the other side.
* **Concurrent** - Not too earthshattering, but this is a non-blocking,
  multiplexed protocol.
* **Debuggable** - ASCII-based wire format. You can, of course, encode your
  payloads any number of way, but you’ll have an easy time with your
  packet sniffers and debug tools.
* **Pretty damned simple** - There’s not a whole lot to Gotalk. A handful
  of message types. A pretty simple, easy-to-parse wire format. Nothing
  crazy for terminology or concepts. If you were curious about network
  protocols and wanted a gentle intro, this would be a great one to look at.

The official [Gotalk](https://github.com/rsms/gotalk) repo has a bunch of examples and even some helper
libraries in Go and JS. The official implementation is in Go, with the JS
libraries being built on top of WebSockets.

But what about Python?!?
------------------------

> “But Greg, I too want to play with this fledging version 0.0 protocol! And
> I want to do it in Python!”

You, my friend, are in luck! I have a rough, version 0.0 Python module to go
with this new, version 0.0 protocol.

For now, most of the effort is on message serialization and deserialization.
We’ll be keeping that separate from any of the naughty bits (sockets,
IO, and other things). The goal is to provide some reusable components that
people can tinker with.

And more importantly, I haven’t ever bothered to mess around at the
protocol level very often. This has been a great excuse to play around with
a spec that is just getting started.

Pull requests, issues, suggestions, and the whole lot are welcome. Tell me
how bad I screwed up!

Closing notes
-------------

If it wasn’t already evident, **do not use this for anything but tinkering
right now!**.

Also, to stem the tide of “Well, why didn’t you just use X instead?”, this
is a fun little experiment for me. Yes, I wrote a protocol
serialization/deserialization for funzies. No, I’m not mentally ill.
