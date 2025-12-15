---
author: Greg Taylor
pubDatetime: 2012-10-16T20:55:00+00:00
modDatetime:
title: python-bluefin 1.3 released
slug: python-bluefin-13-released
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

[python-bluefin](http://pypi.python.org/pypi/bluefin/) 1.3 has been released, now with improved errorhandling. The major feature in this release is that we have smoothed
over some inconsistencies in Bluefin’s error handling.

Instead of setting an HTTP status code indicating an error like they do
for most of the Bluefin API errors, we get an HTTP 200 back, and a
rarely used attribute in the response contains an error flag, with
another rarely used attribute containing a cryptic error message. Since
you need to handle invalid credit card numbers and authorization
failures gracefully, we now return a different exception (that still
inherits from what was previously returned). We also provide a more
friendly error message for the authorization-related errors, that are
not user-friendly, or human-friendly.

Of course, you can still access the original exception message through
Exception.raw\_message. See the [changelog](https://raw.github.com/duointeractive/python-bluefin/master/CHANGES.txt) for full details.

This release is backwards compatible, it’ll just give you better
granularity in your error handling.

Get it from the [PyPi](http://pypi.python.org/pypi/bluefin/) page, or by installing ‘bluefin’ from pip/easy\_install.
