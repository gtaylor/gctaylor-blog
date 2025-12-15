---
author: Greg Taylor
pubDatetime: 2008-03-09T03:05:00+00:00
modDatetime:
title: Powered by .
slug: powered-by-insert-here
featured: false
draft: false
tags: ["Python", "Django"]
description: ""
---

Django is able to run on a number of different web servers, databases,and operating systems. This flexibility lends itself to a lot of
diversity within the community, but what kind of combinations are the
most common?

The developers seem to suggest that Apache2 + mod\_python + Postgresql
seem to be the recommended setup, but undoubtedly there are lots of
others. I’ve heard mentions of lighttpd, FastCGI, nginx running on
Windows, Linux, Mac OS X, Unix/BSD, and others. There is even a [useful
page](http://code.djangoproject.com/wiki/ServerArrangements) on the Django wiki with some of the arrangements along with
instructions for each.

**So I pose the question to you, what do you run on? What operating
system, server, and database?** If you’re feeling really ambitious, I’d
be interested in hearing how your setup has worked for you.

As for this site, it’s hosted on Debian running Apache 2, mod\_python,
SQLite. For a simple, low traffic site like this, it has worked quite well.
