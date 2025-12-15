---
author: Greg Taylor
pubDatetime: 2015-01-11T22:31:00+00:00
modDatetime:
title: python-colormath 2.1.0 released
slug: python-colormath-2-1-released
featured: false
draft: false
tags: ["Python", "Color Science", "Programming"]
description: ""
---

[python-colormath](https://github.com/gtaylor/python-colormath) 2.1.0 haslanded, bringing with it some excellent new features and bug fixes.
See the [release notes](http://python-colormath.readthedocs.org/en/latest/release_notes.html)
for a more detailed look at the changes.

The headlining feature is the replacement of our hardcoded conversion tables with
[NetworkX](https://networkx.github.io/)-based resolution of color conversions (courtesy, Michael Mauderer).
Color Appearance Models and IPT round out the rest of the new features.

Installation
------------

The easiest way to get python-colormath is through pip/easy\_install:

```
pip install colormath
```

Alternatively, grab it from [PyPi](https://pypi.python.org/pypi/colormath/).

Halp!
-----

If you get stuck, create an issue in the
[issue tracker](https://github.com/gtaylor/python-colormath/issues)
and we can figure it out.
