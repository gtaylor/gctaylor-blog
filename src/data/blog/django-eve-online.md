---
author: Greg Taylor
pubDatetime: 2009-02-11T21:12:00+00:00
modDatetime:
title: Django + EVE Online
slug: django-eve-online
featured: false
draft: false
tags: ["Python", "Programming", "Gaming", "Django"]
description: ""
---

For the use of fellow Djangonauts out there, I introspected and fixed upCCP’s SQL dump of EVE Online data. This means you can now get access to
everything from the comforts of the Django ORM.

The project is still very new, and I’m not even sure it’s going to be
attractive given the table layout. At this point, it is a bunch of
introspected models and a fixed up database dump. I’ll be adding
convenience methods, \_\_unicode\_\_ functions, and etc with time to
make it more friendly. Check it out at:

<http://code.google.com/p/django-eve/>

For now this will only work on Postgres until some kind soul wants to
get the MySQL or SQLite dumps fixed up (some tables need ‘id’ primary keys).
