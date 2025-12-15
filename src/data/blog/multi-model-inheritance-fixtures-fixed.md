---
author: Greg Taylor
pubDatetime: 2008-06-09T14:18:00+00:00
modDatetime:
title: Multi-Model Inheritance + Fixtures = Fixed
slug: multi-model-inheritance-fixtures-fixed
featured: false
draft: false
tags: ["Python", "Programming", "Django"]
description: ""
---

I just thought I’d take a moment to give everyone a heads up thatMulti-Model Inheritance fixture dumping and loading is now fixed, as per
Russ Magee’s [changeset 7600](http://code.djangoproject.com/changeset/7600). This fixes a subtle problem that some of
you may have seen in the form of foreign keys pointing to the wrong
objects after using loaddata to restore an app.

The “pk” fields (usually ‘id’) in the serialized dump weren’t being
loaded correctly, meaning that the objects id fields defaulted to the
table’s incremental numbering rather than using the number specified in
your object’s fixture’s “pk” field. This would not be an issue unless
you deleted an object in your original table and thus had a gap in your
primary keys (IE: they were no longer un-interrupted and sequential).

Let’s say you have three objects, 1 (Apple), 2 (Banana), 3 (Orange). You
delete Banana (2) and now have entries with keys of 1 and 3
(non-sequential). Some other arbitrary models point at 1 and 3, and you
now dumpdata your Fruit app and re-load it. The loader ignores the fact
that Orange’s PK is 3 and instead just adds it right behind apple as PK
2 (sequential, the default behavior for primary keys when no value is
specified). All of your other relations pointing at Orange in other
tables are now broken, and you’re likely to see Exceptions thrown or
models pointing to the wrong fruit (if you had more fruit defined to be
compacted into PK 3).

I have a feeling I didn’t explain this well. In the event that you’d
like further elaboration, see the [Django-Users post](http://groups.google.com/group/django-users/browse_thread/thread/17946de0a585a51/4b8ff3f7707893b8) where it’s
outlined a little beter. For those using Multi-Model inheritance and
fixtures, this was a definite show-stopper.

A big thinks goes out to Russ Magee for fixing this!
