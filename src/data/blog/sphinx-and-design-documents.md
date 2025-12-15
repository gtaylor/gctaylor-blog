---
author: Greg Taylor
pubDatetime: 2011-11-28T04:50:00+00:00
modDatetime:
title: Sphinx and Design Documents
slug: sphinx-and-design-documents
featured: false
draft: false
tags: ["Mud", "Python", "Programming"]
description: ""
---

As I’ve matured as an individual and a developer, I find that I like tospend longer and longer amounts of time in the planning phase before
writing too much code. I’ll tinker with some of the technical problems
I’m very concerned about, make sure my idea is even feasible, then jump
into design doc mode.

Depending on the complexity of the project, this can be as simple as a
Google Doc (especially if collaborating with less technical people), or
as “fancy” as [Sphinx](http://sphinx.pocoo.org/) documentation. I find the latter to be strangely
therapeutic, though (I don’t pretend to be normal).

What is Sphinx?
---------------

[Sphinx](http://sphinx.pocoo.org/) is a wonderful tool used for writing documentation for
software. In addition to being able to generate documentation from
docstrings ([autodoc](http://sphinx.pocoo.org/ext/autodoc.html?highlight=autodoc#sphinx.ext.autodoc)) for API references, it also makes it really easy
to write user/admin guides, and design docs. Your documentation can
refer to individual functions, methods, classes, and modules (if they
are [autodoc’d](http://sphinx.pocoo.org/ext/autodoc.html?highlight=autodoc#sphinx.ext.autodoc)), and you have the full power and ease of
[reStructuredText](http://docutils.sourceforge.net/rst.html) at your fingertips.

You may have seen Sphinx in action if you’ve browsed [Django](http://docs.djangoproject.com/) or
[Python’s](http://docs.python.org/py3k/) documentation. While the most avid users are Python
projects, other languages are now supported.

What does the end result look like?
-----------------------------------

In the case of my latest project, a MUD named [Dawn of the Titans](https://github.com/gtaylor/dott), the
end result looks like [this](http://dott.readthedocs.org/).

I tend to start out with high-level scribbling in a [Scratch Pad](http://dott.readthedocs.org/en/latest/index.html#scratch-pad)
section, and just brain dump high level stuff, even if it doesn’t make
100% sense.

As things solidify, they end up graduating to their final homes in the
[Administrator](http://dott.readthedocs.org/en/latest/index.html#administrator-documentation) or [Player](http://dott.readthedocs.org/en/latest/index.html#player-documentation) Documentation sections (in this project’s
case). So I am effectively writing much of the guides before I write the
actual code. As the code falls into place, my developer documentation
references autodoc’d functions/methods/classes/modules, and etc.

reStructuredText is about as simple as Wiki markup, and is really
similar to how developers have traditionally formatted comments and
READMEs. It’s not much extra burden to write in reST as opposed to just
doodling in a text editor.

When does it make sense to use Sphinx?
--------------------------------------

* When you don’t mind spending the initial time to get Sphinx set up.
* You either know, or want to know, reST.
* The ability to gradually shift to “final” documentation without
  changing formats is appealing.
* You value Sphinx’s autodoc and other extensions for API references,
  and cross-referencing such API documentation throughout your
  user/admin/dev guides is appealing.

When does it not make sense to use Sphinx?
------------------------------------------

* You are in a huge hurry.
* People without the time or knowledge to write reST or use version
  control need to be able to update the documentation.
* The project is simple enough that a Google Doc won’t be too clumsy.

Why so complicated?
-------------------

You do indeed need to learn some basic reStructuredText in order to go
the route that I have, and there is some initial setup work that can be
avoided with something like Google Docs. However, the great thing about
using something like Sphinx is that my design docs gradually morph into
very complete, thorough user/administrator/developer guides. Due to
Sphinx’s autodoc extension, I also have API reference generation baked
in, for my user/admin/dev guides to reference. A better example of what
one of my more mature projects that was designed and eventually
documented in Sphinx is [media-nommer](http://media-nommer.readthedocs.org/en/latest/index.html). See that for a good example of
what the [Dawn of the Titans](https://github.com/gtaylor/dott) documentation may eventually resemble.

There are a few moving pieces (Sphinx+reST+Revision Control), but each
one is reasonably simple to work with. You can expect to be reasonably
proficient within a day or two, if you go through [First Steps with
Sphinx](http://sphinx.pocoo.org/tutorial.html). There are some quirks, and the error handling isn’t wonderful,
but the end product is great.

Use Read the Docs
-----------------

The other thing that makes this absolutely wonderful is [Read the
Docs](http://readthedocs.org/). This lovely service compiles and hosts your final documentation
for all to see. You can even hook in a GitHub (or other service)
post-commit signal to cause it to automatically pull and re-compile your
docs after each commit.

Here is my workflow for most tinkering:

* Navigate to a file on GitHub, hit the “Edit this file” button.
* Make my changes.
* Enter commit message, hit “Commit Chanes”.
* Read the Docs gets the post-commit notification from GitHub,
  re-compiles the docs.
* After a 15-30 second delay, my docs are updated on the web for all to
  see and comment on.

I can, of course, still edit all of the docs locally in my favorite
editor, and compile everything locally to review before committing (for
more major edits).
