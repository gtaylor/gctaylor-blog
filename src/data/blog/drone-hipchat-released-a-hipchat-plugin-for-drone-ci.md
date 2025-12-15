---
author: Greg Taylor
pubDatetime: 2015-11-02T20:37:12+00:00
modDatetime:
title: drone-hipchat released. A HipChat plugin for Drone CI.
slug: drone-hipchat-released-a-hipchat-plugin-for-drone-ci
featured: false
draft: false
tags: ["Python", "CI", "Programming", "DevOps"]
description: ""
---

Since the [Drone CI Plugin Marketplace](http://addons.drone.io/) didn't have one yet, I put together a quick plugin. It's written in Python instead of Go, so it won't ever be in the official plugin namespace, but it also requires substantially less [boilerplate](https://github.com/drone/drone-plugin-go) than the Go plugins. So we'll run with it because it's simple!

If this interests you, check out the [Github repo](https://github.com/gtaylor/drone-hipchat) and the [documentation](https://github.com/gtaylor/drone-hipchat/blob/master/DOCS.md). You should be able to copy/paste that sample YAML and substitute your values. Since all Drone CI plugins are Docker containers, you'll get the benefit of automatic updates if/when I make improvements or fixes in the future.

I'm all ears for feedback, which you are encouraged to send to the [issue tracker](https://github.com/gtaylor/drone-hipchat/issues).
