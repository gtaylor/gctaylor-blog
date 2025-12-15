---
author: Greg Taylor
pubDatetime: 2011-10-17T04:58:00+00:00
modDatetime:
title: CouchDB as a MUD server data store
slug: couchdb-mud-server-data-store
featured: false
draft: false
tags: ["Mud", "Python", "Programming"]
description: ""
---

I’ve been using [CouchDB](https://github.com/gtaylor/dott) as the data store for my in-developmentMUD, [Dawn of the Titans](https://github.com/gtaylor/dott). So far it’s been very enjoyable to work
with, through the [CouchDB](http://pypi.python.org/pypi/CouchDB)
Python module. I’ll take a moment to share my experiences, for those who
might be interested.

To provide some background, my MUD server is built specifically for the
game I’m working on, but I’ve been developing it in the open on
[GitHub](https://github.com/gtaylor/dott). The whole thing is built on [Twisted](http://twistedmatrix.com/), and is loosely styled
after [TinyMUX](http://tinymux.org/) 2 (with Python in place of C++ and SoftCode).

Why CouchDB?
------------

This is probably the first question on most people’s minds. There was
nothing overly scientific about the choice of CouchDB. For me, this was
a very uninteresting choice. I wasn’t really interested in querying
whatever DB I used, as I wanted to keep almost everything
memory-resident. I didn’t need much scalability at all, and I didn’t
really need a relational database. *The only thing I really needed a DB
for was persistence.*

In the end, I thought CouchDB’s use of JSON documents was pretty neat,
and figured they’d allow for a really simple way to store objects. It
was also a chance to learn something new (which was the biggest factor
of all).

The Perks
---------

So far, CouchDB has been a joy to work with. I realize that almost all
of these are possible with X relational/non-relational DB, but I still
give an approving nod to CouchDB in these cases.

The biggest benefit to using CouchDB is that my in-game object loading
code looks something like this (pseudocode):

```
# Retrieve the object's document from CouchDB. This is a JSON
# dict, whose keys are the object's various attributes (name,
# description, location, etc).
object_doc = self._db[doc_id]
# A simplified example of how a Room is loaded. The CouchDB's keys
# are expanded as kwargs to the Room's __init__. Presto, loaded object.
loaded_object = RoomObject(**object_doc)
```

This may not seem like anything earth-shattering (it really isn’t), but
it makes things very simple to manage and expand on. RoomObject’s
\_\_init\_\_ method knows exactly what to do with a CouchDB object document.

Since CouchDB just deals with JSON documents, I can add/remove keys
(which become object attributes in-game) without hassling with schema
modifications or explicitly specifying fields. I’ve been surprised at
how little time I spend mucking with the DB. I’m free to just focus on
dealing in the realm of my MUD server, without worrying too much about
my data store.

Another great thing about CouchDB is [Futon](http://couchdb.apache.org/screenshots.html), the web-based management
console for CouchDB. It has made editing objects a breeze. I do this
constantly when tinkering with objects. My set of in-game building
commands is currently very limited, so this helps me keep getting things
done while those materialize.

The last cool thing I’ll mention is that saving objects to the DB can
easily be made asynchronous, and you can bulk submit objects (instead of
saving one at a time). While async DB operations are expected for most
DBs, CouchDB’s calls/queries are really easy to work into a Twisted
project (without resorting to threads/processes), since the calls are
all just HTTP requests (that can be deferred via Twisted’s HTTP client).
Take a look at [Paisley](https://github.com/smcq/paisley/blob/master/paisley/client.py) for an example of how simple it is to perform
non-blocking queries.

The downsides
-------------

There is only really one downside (for what I’m doing) to CouchDB, and
many non-relational stores in general: I have to manually assure that
all ‘fake relations’ stay valid, and fail gracefully if they end up
invalid. For example, let’s say I have an Exit that leads to ‘Test
Room’. If said room is deleted, the exit should be un-linked or deleted.
Leaving the exit in place means that someone attempting to travel
through it (to the now non-existant room) would see an error message,
since the ‘destination’ attribute points to an invalid object ID.

Most MUD servers have to do this kind of cleanup on their own anyway,
I’m just somewhat spoiled from my time spent with Postgres/MySQL/SQLite
on [Evennia](http://evennia.com/), which cleaned up after me (CASCADE!). So this is far from
a show-stopper, just something I’m not used to.

The only other thing that could possibly be construed as a down-side is
that querying CouchDB feels clumsy to me. This is almost certainly due
to knowledge gaps on my end. I didn’t really need this in my case
anyway, so no harm here.

In summation
------------

Used in the context of a MUD, CouchDB has been awesome to work with.
I’ve enjoyed it much more than my last MUD server projecet using
relational DBs. In the end, the choice of data store should be made
based on what lets you spend more time on your game, rather than your
serialization/persistence/object saving. For any sanely designed MUD,
you’re not likely to hit performance issues, and it all comes down to a
matter of preference.
