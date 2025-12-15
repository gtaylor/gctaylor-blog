---
author: Greg Taylor
pubDatetime: 2011-08-16T20:37:00+00:00
modDatetime:
title: Tip: Pointing pylibmc at a unix domain socket
slug: tip-pointing-pylibmc-unix-domain-socket
featured: false
draft: false
tags: ["Python", "Programming", "Django"]
description: ""
---

This is a quick tip that will hopefully save someone else a few minutesat least. If you’re using Django 1.3, using pylibmc and want to point at
a local unix domain socket for memcached, this is what your CACHES
setting will look like:

```
CACHES = {
        'default': {
                'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                'LOCATION': '/tmp/memcached.sock',
        }
}
```

This also assumes that you have configured memcached to use a unix
domain socket (with the -s option in memcached.conf).
