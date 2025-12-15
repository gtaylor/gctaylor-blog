---
author: Greg Taylor
pubDatetime: 2011-10-12T01:16:00+00:00
modDatetime:
title: PyPy’s call for donations (NumPy)
slug: pypys-call-donations-numpy
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

*Disclaimer: I am not at all involved with PyPy development, planning,or management. You are about to see cheer-leading, but it’s not because
this is my project.*

PyPy has recently posted  ”[Call for donations - PyPy to support
Numpy!](http://pypy.org/numpydonate.html)” There has been some initial ground work laid by Alex Gaynor
and others, but it looks like they’re ready to go full speed ahead with
the effort now. This is great news for PyPy and Python.

[NumPy](http://numpy.scipy.org/) is one of the defacto scientific computing packages in the
Python ecosystem. There are [all kinds of other modules](http://pypi.python.org/pypi?%3Aaction=search&term=numpy&submit=search) that depend on
NumPy, and it’s used heavily in research, engineering, and other general
sciency stuff.

[PyPy](http://pypy.org/) is speedy alternative implementation of Python. In many cases,
PyPy is able to handily [whallop](http://speed.pypy.org/) traditional CPython. As of the time
of this article’s writing, PyPy’s speed center says “The geometric
average of all benchmarks is 0.21, or 4.9 times faster than CPython”.

So… why do I care?
------------------

CPython, being an interpreted language, often falls behind other
closer-to-the-metal languages and compilers. The scientific community,
along with [a good number of other modules](http://pypi.python.org/pypi?%3Aaction=search&term=numpy&submit=search) rely on NumPy. The problem
is, CPython isn’t nearly as fast as some of the alternative languages.
However, what Python loses in speed, it makes up for in ease-of-use and readability.

With a PyPy-compatible NumPy, we can greatly reduce our speed woes, and
open up PyPy compatibility with a very large set of existing modules.
The end result being PyPy is one step closer to being ready for everyday
use, and it also gets a “killer package”.

Lots of drops in the bucket = ??
--------------------------------

There’s only so much we, as individuals can do financially, but do
consider [making a small donation](http://pypy.org/numpydonate.html) to the cause. The Python community
is large, and contributions will quickly accumulate to something useful.
For those who are firmly entrenched in CPython, consider what an
aggressive, experimental Python implementation does for the greater
Python ecosystem (subject for another post or discussion).
