---
author: Greg Taylor
pubDatetime: 2010-01-20T19:29:00+00:00
modDatetime:
title: PIL + TIFF = Fun
slug: pil-tiff-fun
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

We had to do some things at work using TIFF files with software thatrelied on the presence of certain TIFF Tags. We’re slowly phasing out
some legacy C applications with Python equivalents, and decided to use
Python Imaging Library for the task.

Everything worked brilliantly, aside from the fact that most of the tags
from the original file we were modifying were getting wiped out in the
newly saved file. This was a show-stopper, so I spent some time
spelunking in PIL source and fixed the tag-obliterating behavior for the
tags we were primarily interested in.

By no means is my work all-inclusive, but I did find some other minor
bugs that probably weren’t noticed by most applications that were
reading the resulting tiffs. Right now my modifications are sitting in a
fork of the main repository on Bitbucket. I’ve got a pull request in
with effbot, but until then, check out my work on the
[pil-2010-gtaylor](https://bitbucket.org/gtaylor/pil-2010-gtaylor/overview/) fork. Comments, suggestions, and mean-spirited
nit-picking are welcome.
