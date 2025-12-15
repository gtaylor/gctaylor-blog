---
author: Greg Taylor
pubDatetime: 2014-05-03T00:31:00+00:00
modDatetime:
title: python-colormath 2.0 released!
slug: python-colormath-2-0-released
featured: false
draft: false
tags: ["Python", "Color Science", "Programming"]
description: ""
---

[python-colormath](https://github.com/gtaylor/python-colormath) was startedback in 2008, when I was an undergraduate at Clemson University (Go Tigers!).
While there are a good number of people out there making use of the module
effectively, there were a lot of things I wanted to do differently in an
eventual 2.0 release. There were some usability issues that arose from my
being relatively new to Python at the time.

But all has been made well now. I am happy to announce the immediate release of
[python-colormath 2.0](https://pypi.python.org/pypi/colormath/)! A
few hilights:

* [Better documentation](http://python-colormath.readthedocs.org/)
* Python 3.3+ support added. Python 2.6 and lower no longer supported.
* A complete re-working of RGB and RGB conversions. I’m biased, but I think we’ve
  now got more correct RGB handling than the vast majority of color math libraries
  out there, regardless of language.
* While the color space conversion math remains largely untouched, there is
  now a dedicated color\_conversions submodule that is devoted to the cause.
  I think this is a good clarity/usability win.
* Our unit test suite saw a lot of improvement. They are now easier to write,
  more complete, and more helpful when failures occur.
* Numpy matrix-driven Delta E functions were incorporated for a nice
  speed win. In addition to the standard Delta E calls, you can use a vectorized
  equivalent that is much faster.

See the [2.0 release notes](http://python-colormath.readthedocs.org/en/latest/release_notes.html#id2)
for a more detailed look at the differences.

**NOTE: There are backwards incompatible changes in this release.** In order
to set things right, there were quite a few breakages, but I’ve done the best
I can to document these.

Installation
------------

The easiest way to get python-colormath is through pip/easy\_install:

```
pip install colormath
```

Halp!
-----

If you get stuck, create an issue in the
[issue tracker](https://github.com/gtaylor/python-colormath/issues)
and we can figure it out.
