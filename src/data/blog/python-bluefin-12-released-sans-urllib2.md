---
author: Greg Taylor
pubDatetime: 2012-09-19T21:36:00+00:00
modDatetime:
title: python-bluefin 1.2 released, sans urllib2
slug: python-bluefin-12-released-sans-urllib2
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

python-bluefin 1.2 has been released. python-bluefin is a very thinwrapper around the [Bluefin](http://www.bluefin.com/) payment gateway’s API. The two major
changes are:

* urllib2 has been removed, with the excellent [requests](http://docs.python-requests.org/) taking its place.
* We now check directmode’s status\_code for known failure codes and
  raise exceptions based on what we find. Previously, no exception was
  raised, which would result in a silent failure if you weren’t looking
  at status\_code yourself.

To install, either easy\_install/pip install bluefin, or download
directly from its [PyPi page](http://pypi.python.org/pypi/bluefin/).
