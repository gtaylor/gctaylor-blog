---
author: Greg Taylor
pubDatetime: 2011-09-15T03:11:00+00:00
modDatetime:
title: Read the Docs: A huge thanks!
slug: read-docs-huge-thanks
featured: false
draft: false
tags: ["Python", "Programming", "Django"]
description: ""
---

When a free service or module proves to be invaluable to yourproject(s), it’s only right to thank the authors for their excellent
work. I thought I’d take a brief moment to thank all of the contributors
behind [Read the Docs](http://readthedocs.org/) for this simple but wonderful site. I have found
it to be extremely useful for my hobby and real-world projects.

For those who have yet to see the light
---------------------------------------

If you have [Sphinx](http://sphinx.pocoo.org/)-based documentation and haven’t played with [Read
the Docs](http://readthedocs.org/) yet, I can’t recommend it enough. Not only do you not have to
hassle with hosting your compiled HTML documentation yourself (or on a
specially named branch in VC), you can point many software forges’
post-commit hooks at a specific URL to enable automatic doc updating
with each commit/push.

I no longer have to manually udpate the docs with each change, or juggle
the annoying gh-pages branch on GitHub. Each commit posts to a
project-specific URL on Read the Docs, and RTD pulls the latest source,
runs [Sphinx](http://sphinx.pocoo.org/), and posts the result up within a minute or two.

Small victories in efficiency
-----------------------------

If all of this doesn’t seem like a big deal, that’s because it isn’t.
This is a small, incremental improvement to my development process that
leads to less context switching, less manual labor, and less stuff to
worry about. This is not the cure for cancer and it won’t win a Nobel
Peace Prize.

However, it is just the very small, simple improvement that makes a
noticeable impact. Low-hanging fruit. The tastiest kind.
