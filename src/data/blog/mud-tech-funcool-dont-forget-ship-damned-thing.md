---
author: Greg Taylor
pubDatetime: 2013-01-08T04:26:00+00:00
modDatetime:
title: MUD tech is fun/cool, but…
slug: mud-tech-funcool-dont-forget-ship-damned-thing
featured: false
draft: false
tags: ["Mud", "Programming", "Gaming"]
description: ""
---

As software development evolves, there are an ever-expanding number ofways to put together very complex, elaborate systems that are fun to
geek out on. Multi-processing is becoming increasingly prevalent,
distributed systems are a boon to cases with massive scalability or
reliability requirements, and there are all kinds of neat data stores
available. These are all definitely things that have a place in software.

But what does this mean, in the context of a MUD?
-------------------------------------------------

Honestly, very little. Even a very large MUD with hundreds of connected
players can be ran on a very pedestrian machine with a modest amount
RAM, and very little bandwidth. Multi-threading is not a requirement for
performance (and can often work against it). Highly distributed,
multi-server setups are hitting nails with jackhammers. After all, we’re
talking about a genre that primarily features smaller (<100 connected
players) games.

An important thing to keep in mind when developing a MUD is that simple,
well-thought-out MUD architectures have a huge advantage over those
their more complex kin: *They are easier to develop, and they are a lot
more likely to ever see the light of day*.

MUDs are a labor of love
------------------------

Although you’ll hear people crying about the demise of the text-based
genre, there will always be a niche out there for our kind. However, the
vast majority of the games in our space are going to remain
non-commercial, and mostly developed by volunteers on their spare time.

By making simplicity a high priority, we make sure that it’s easier to
make progress when you *do* have a few moments to sit down and work on
your game. While you could write a super-distributed,
super-fault-tolerant MUD server, it’s probably going to make future
development more complicated, *and you may run out of steam before you
get anywhere close to being “done”*. As someone who would love to see
more great MUDs out there, this makes me sad!

Developing and launching a MUD is a labor of love, and it has to be fun
and interesting to you. You have a finite amount of time to get your
game launched before you probably lose interest and move on to other
things. This “time limit” varies from person to person, and some possess
the rare ability to regularly, routinely work on a game for years before
going public, but those types are very rare now. Your goal should be to
open to the public before your “ok, time to move on” timer goes off.
Simplicity is one of your biggest allies while pursuing this goal.

But… there are always caveats
-----------------------------

A very valid counter-point to this argument for simplicity is that MUDs
are a great way to learn new technologies, to experiment, to do things
one might not normally do. If one’s goal is to tinker more so than to
actually release a game to the world, you can throw this all out the
window. Get as complex/geeky/sexy as you’d like, and have a blast. Who
cares if you never ship? That’s not the point for you, anyway.

For those that are most concerned with actually “shipping”
----------------------------------------------------------

Focus on your core functionality. What is your “minimum viable product?”
What is the most direct way to get to your opening day? Avoid
unnecessary complexity, and remember that you can always refactor and
improve performance/scalability as you grow. Nothing is set in stone.

Avoid traps like multi-threading (unless you really have to have it),
super scalability, and elaborate distributed setups unless you just
really want to play. You’re designing a Gocart, not an IndyCar.

Simplicity. Clarity. Focus. Oh, and ship the damned thing!
