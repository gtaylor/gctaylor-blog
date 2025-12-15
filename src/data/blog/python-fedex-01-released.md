---
author: Greg Taylor
pubDatetime: 2009-09-23T20:31:00+00:00
modDatetime:
title: python-fedex 0.1 Released
slug: python-fedex-01-released
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

After a few weeks of slow work, I finally have released python-fedex.This module is a very light wrapper around suds and the Fedex WSDLs.
There is very little abstraction, the idea is just to handle the
annoying WSDL stuff behind-the-scenes and raise some basic exceptions if
really bad things happen.

By figuring out the suds+WSDL end of things, I hope to allow other
Python developers to jump into their projects much more quickly. This
will be used in a production environment at IP, and will see extensive
testing starting in a few weeks.

If you are at all interested or curious, see the [python-fedex Google
Code page](http://code.google.com/p/python-fedex/).
