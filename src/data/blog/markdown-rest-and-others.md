---
author: Greg Taylor
pubDatetime: 2011-07-19T04:01:00+00:00
modDatetime:
title: Of Markdown, REST, and others
slug: markdown-rest-and-others
featured: false
draft: false
tags: ["Mud", "Programming"]
description: ""
---

As I’m working on my [side project](https://github.com/gtaylor/dott) (You should probably watch it onGitHub to stroke my ego), I’ve been toying with how I’ll eventually
handle colors and web content. I’m almost fully set against using
MUX/MUSH color codes, as those don’t do the best job of handling where
color starts/ends. They’re also not very friendly for web-based output.

I’ve been considering a few different approaches:

* Restructured Text
* HTML
* Something resembling customized BBcode

I really like Restructured Text, but am not quite sure how I’d
substitute in the color sequences on the MUD side. HTML (or a subset of
it) is possible, but I’m not sure this is a very clean solution. BBcode
could work, and is probably the most simple to implement, but I wonder
if it’d prove too limiting.

I’ll open this up to other MUD developers for commenting. How do you
handle color in a way that plays nice with a variety of different
clients/protocols (I’m very interested to hear how games that have both
a Telnet and web-based service handle this).
