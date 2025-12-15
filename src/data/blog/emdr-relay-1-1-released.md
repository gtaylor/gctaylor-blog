---
author: Greg Taylor
pubDatetime: 2015-01-12T22:31:00+00:00
modDatetime:
title: EMDR Relay 1.1 Released
slug: emdr-relay-1-1-released
featured: false
draft: false
tags: ["Programming", "Go", "Gaming"]
description: ""
---

[EVE Market Data Relay](http://www.eve-emdr.com/) (EMDR) has been chugging along behind the scenesin the EVE Online developer community, quietly delivering large volumes
of player-supplied market data. But the winds of change are arriving, as
CCP has released a set of HTTP APIs for obtaining much of the data directly.
EMDR will continue to function for those who don’t want to poll on their own.

The first step in putting a fresh coat of paint on EMDR is to freshen up
the relays. We have done just that, updating and modernizing a few things.

Some hilights of the 1.1 release:

* I have built a Docker image that is now the officially endorsed way to set
  up and run an EMDR relay.
* We’ve upgraded (and now require) ZeroMQ 4.x. If you use the Docker
  image, you don’t need to worry about this.
* We now auto-restart the process every 12 hours. This works around some ZeroMQ
  edge cases where connections aren’t restored correctly. Most of our relay
  operators are already doing this, but now we all will, just in case.

See our [Docker Hub repo](https://registry.hub.docker.com/u/gtaylor/emdr-relay-go/) for full setup instructions. Current relay operators
are encouraged to upgrade, though nothing will break if you don’t.
