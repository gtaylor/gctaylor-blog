---
author: Greg Taylor
pubDatetime: 2011-07-13T00:13:00+00:00
modDatetime:
title: Back to basics (again)
slug: back-basics-again
featured: false
draft: false
tags: ["Mud", "Programming", "Gaming"]
description: ""
---

It’s definitely different starting all over again with writing a new MUDcodebase. My first attempt was [Evennia](http://evennia.com), which  has evolved
significantly since I handed it over. It is/was meant to be more
general-purpose, and appeal to MUX/MUSH/MOO refugees who are tired of
softcode (MUX/MUSH’s internal scripting language). This time around, I’m
writing something specifically crafted for my own purposes, so I get to
be greedy.

I’ve got some particular ideas in mind for what I’d like to do. While I
could have used Evennia (it has matured into a fine codebase), I decided
to take what I learned from my first effort a few years ago, refine it,
and turn something out that was the bare minimum for what I want to do
(more on what that is in a future post).

I am in no way advocating this approach for most or even a few, as it’s
extremely time consuming, a re-invention of the wheel, and not at all
sexy. I find myself implementing command parsers/tables, object
persistence, and a bunch of other stuff that I’ve already done, all in
the name of being my game’s ideal environment for development. But for
those that are masochistic, have tons of time on their hands, or are
otherwise mentally ill, it can’t be beat!

While I am very unlikely to ever write documentation aside from what any
future game moderators will need, the full source code for the new
codebase can be found on [GitHub](https://github.com/gtaylor/dott). This is going to be in constant
flux, backwards incompatibilities will probably arise every time I touch
it, and it’s likely to be partially or completely broken at any time.
That said, maybe you’ll find something useful in it.
