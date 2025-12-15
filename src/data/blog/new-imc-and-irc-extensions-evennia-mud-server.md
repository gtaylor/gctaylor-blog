---
author: Greg Taylor
pubDatetime: 2011-04-19T22:00:00+00:00
modDatetime:
title: New IMC and IRC extensions for Evennia MUD server
slug: new-imc-and-irc-extensions-evennia-mud-server
featured: false
draft: false
tags: ["Evennia", "Gaming", "Django", "Programming", "Mud", "Python"]
description: ""
---

[Evennia](http://evennia.com/), the Twisted+Django MUD server, has just finished bringing inshiny new support for IRC and IMC (Inter-mud communication) as of
revision 1456. This allows users to bind a local game channel to a
remote IRC or IMC room. Evennia transparently sends/receives messages
between the game server and the remote IRC/IMC server, while the players
are able to talk over said channel just like they would a normal one.

It is even possible to bridge an IRC room to an IMC channel, with the
Evennia server acting as a hub for messages. The next step for any eager
takers may be to create a Jabber extension (any takers?).

If you’re curious, feel free to drop by #evennia on FreeNode to pester
the developers.
