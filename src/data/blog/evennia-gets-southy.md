---
author: Greg Taylor
pubDatetime: 2011-03-21T04:30:00+00:00
modDatetime:
title: Evennia gets Southy
slug: evennia-gets-southy
featured: false
draft: false
tags: ["Evennia", "Gaming", "Django", "Mud", "Python"]
description: ""
---

The Django-based [Evennia MUD Server](http://evennia.com/) took another great step forwardtoday in adding support for the excellent [South](http://south.aeracode.org/) migration app. This
should knock down another barrier for those considering beginning
development on their own games. The kinds of schema changes from this
point forward should be fully covered by the South migrations that we provide.

For those that aren’t familiar with Evennia, it is the first
well-established MUD server built with Django (perhaps the first,
period). This makes game development extremely simple, and gives us a
lot of power to webbify games (take a look at the included web-based
client, for an example). Twisted handles our network layer, and some
scheduling. Another unique thing (as far as MUDs go) is that there is
actually a good bit of [documentation](http://code.google.com/p/evennia/wiki/Index?tm=6).
