---
author: Greg Taylor
pubDatetime: 2011-09-06T04:13:00+00:00
modDatetime:
title: Evennia MUD server grows a proxy
slug: evennia-get-proxied
featured: false
draft: false
tags: ["Mud", "Python", "Django"]
description: ""
---

I’ve obviously been on a bit of a proxied MUD server tangent of late(see [here](http://gc-taylor.com/blog/2011/8/2/mud-behind-proxy-potentially-great/) and
[here](http://gc-taylor.com/blog/2011/8/30/dott-now-more-proxy/)). I
typically haunt #evennia on FreeNode, and brought the point up to the
current maintainer, Griatch, a few weeks ago. As is typical for Griatch
when he finds something he likes, he cranked out his take on an
[AMP](http://amp-protocol.net/)-based proxy (the [Evennia](http://evennia.com/) term is “portal”) very quickly, and
[announced](https://groups.google.com/d/topic/evennia/ifopOecaoGU/discussion) the specifics a few days ago.

The biggest benefit in the case of [Evennia](http://evennia.com/) is that the old,
complicated code reloading system is now completely gone. This is a big
win in simplicity and avoiding nasty edge cases where reloading doesn’t
work as expected.

For those that haven’t heard of [Evennia](http://evennia.com/), it’s a Python + Twisted +
Django MUD server that gives you a solid foundation to immediately start
adding your game-specific stuff to. The [documentation](http://code.google.com/p/evennia/wiki/Index?tm=6) (particularly
the [developer](http://code.google.com/p/evennia/wiki/DeveloperCentral) section) is outstanding, and is amongst the very top
tier of MUD servers. If you are even partially curious, consider joining
the [Google Group](https://groups.google.com/forum/#!forum/evennia) or lurking in #evennia on FreeNode. There are lots
of interesting discussions on both from people of varying levels of involvement.
