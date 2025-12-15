---
author: Greg Taylor
pubDatetime: 2011-05-05T21:57:00+00:00
modDatetime:
title: Tamarin 1.1 released
slug: tamarin-11-released
featured: false
draft: false
tags: ["Python", "Cloud", "Django"]
description: ""
---

Tamarin 1.1 was released to account for the fact that there are rarecases where a user’s client doesn’t identify itself at all. I had
accounted for one form of this, but failed to handle another. You’ll
want to update to prevent ParseException exceptions from being raised if
your parser runs into this.

Tamarin is a drop-in Django app that is used to parse S3 access log
buckets. This is useful for getting the logs into a medium (a DB) that
can be more easily queried, filtered, sorted, and etc.

PyPi page is here: <http://pypi.python.org/pypi/tamarin/>

Sources are on GitHub: <https://github.com/duointeractive/tamarin>
