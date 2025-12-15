---
author: Greg Taylor
pubDatetime: 2009-09-09T14:53:00+00:00
modDatetime:
title: Snow Leopard 10.6.0 client DNS problems
slug: snow-leopard-1060-client-dns-problems
featured: false
draft: false
tags: ["Mac"]
description: ""
---

It would appear that Snow Leopard 10.6.0 has an issue with client-sideDNS resolution. Symptoms include erratic resolution of domain names from
local network DNS servers for any command or application using
gethostbyname(). However, using the **host** or **nslookup** commands
resolve things correctly.

The current best resource for this issue is a thread on the [Apple
support forums](http://discussions.apple.com/thread.jspa?threadID=2132856). There are all kinds of suggestions as to what the
problem is and all kinds of voodoo fixes, though none have been found to
work for most (or all). I’d hold off on attempting these untill 10.6.1
rolls out, which will be in the near future.

In the meantime, i’d suggest using your /etc/hosts file for must-have
names. Keeping an eye on that thread may shed further light on the
situation as the problem is investigated in greater detail.
