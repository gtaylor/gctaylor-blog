---
author: Greg Taylor
pubDatetime: 2013-04-16T14:40:00+00:00
modDatetime:
title: EMDR Map Sheds its Snake Skin
slug: emdr-map-sheds-its-snake-skin
featured: false
draft: false
tags: ["GoLang"]
description: ""
---

As a fun exercise, I set out to re-write the WebSocket server behind[EMDR Map](http://map.eve-emdr.com/) in [GoLang](http://golang.org/).

The Python version
------------------

The [initial version](https://github.com/dliverman/eve-market-ping-map/blob/727a43a4660af72ddd037ad0bec9e9bfc249f969/ws_server.py)
of the WebSocket server powering the map was developed
with Python, gevent-websockets, and ZeroMQ. While the original Python version
was pretty simple, it was much heavier on memory and didn’t free resources
very quickly after disconnections. My biggest gripe was that I wasn’t entirely
happy with how the Greenlets interacted with one another. Time to
needlessly re-invent the wheel for fun and profit!

The GoLang version
------------------

After [cobbling something together](https://github.com/dliverman/eve-market-ping-map/tree/master/server),
I found that some resources were saved, but nothing earth-shattering. More
importantly, I feel that the channels and goroutines pattern makes a lot more
sense for this particular project than my coroutines and internal ZeroMQ sockets.

I apologize for the lack of build instructions or documentation of any sort,
but such is the norm for my experiments like this!

* See the [EMDR Map](http://map.eve-emdr.com/).
* View the [project on GitHub](https://github.com/dliverman/eve-market-ping-map).
