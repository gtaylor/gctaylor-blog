---
author: Greg Taylor
pubDatetime: 2012-02-15T03:49:00+00:00
modDatetime:
title: django-dynamodb-sessions is ready!
slug: django-dynamodb-sessions-ready
featured: false
draft: false
tags: ["Python", "Cloud", "Django", "Programming"]
description: ""
---

After much tweaking, hand-wringing, and thumping around on staging,[django-dynamodb-sessions](https://github.com/gtaylor/django-dynamodb-sessions) is ready. The package provides a
super-high-scalability session store for those hosting on Amazon’s EC2.

This may be useful to you if…
-----------------------------

You’re wanting to trim your DB size, or reduce the read/write thrashing
that happens with DB-backed sessions. You also don’t feel like
maintaining Redis, or something similar.

With the introduction of Amazon’s [DynamoDB](http://aws.amazon.com/dynamodb/), we now have a very fast,
massively scalable data store that is somebody else’s problem to secure,
update, and keep running. I’ve found the response times to be great,
especially when combined with the provided cached\_dynamodb backend
(similar to Django’s cached\_db backend).

This probably isn’t a good option for you if…
---------------------------------------------

* You aren’t hosting on EC2. While it’s still possible to use, YMMV as
  far as response times go. Within AWS, the response times are excellent.
* You’re not at a big enough scale to find yourself with a ton of
  django\_sessions table bloat, or the previously mentioned read/write
  thrashing in django\_sessions.
* You store massive (>1MB) amounts of data in sessions.

Getting Started
---------------

If you’d like to give django-dynamodb-sessions a try, either grab it
with your choice of easy\_install, pip, or other equivalent, or snag it
from its [page on PyPi](http://pypi.python.org/pypi/django-dynamodb-sessions/). Install instructions can also be found on the
[PyPi page](http://pypi.python.org/pypi/django-dynamodb-sessions/).

If you think this is interesting…
---------------------------------

Make sure to *Watch* the [project on GitHub](https://github.com/gtaylor/django-dynamodb-sessions). If there’s enough
interest, I’ll continue to tweak and improve the package.
