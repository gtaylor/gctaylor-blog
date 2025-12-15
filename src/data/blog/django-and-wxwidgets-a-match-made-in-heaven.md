---
author: Greg Taylor
pubDatetime: 2008-03-05T15:37:00+00:00
modDatetime:
title: Django and wxWidgets: A match made in heaven
slug: django-and-wxwidgets-a-match-made-in-heaven
featured: false
draft: false
tags: ["Programming", "Django"]
description: ""
---

During the design phase for a color accuracy management system, mycompany decided to go with a client-server model rather than individual
workstations that are more or less independent. The central server would
be responsible for recording readings from the clients and doing various
calculations on the data. We wanted most of the calculation to happen
server-side in order to keep the clients very simple, and ease of
communication from client to server was a point of emphasis.

Rather than develop a server product from scratch, we chose [Django](http://djangoproject.com)
due to familiarity and being cross-platform/database-independent. On the
client side, the GUI toolkit of choice was [wxWidgets](http://wxwidgets.org), as it runs well
on a number of platforms and has unrestrictive licensing. It also helps
that I had developed a few other applications using it.

With the underlying technologies for the client and server chosen, we
needed a means for communication between the two. A number of XML and
other serialized formats were looked at, but eventually JSON won out.
Django includes [simplejson](http://pypi.python.org/pypi/simplejson), a [Python](http://python.org) JSON encoder/decoder. On the
client side, the excellent [wxJSON](http://wxcode.sourceforge.net/docs/wxjson/) library fit into the mix very well.

A few weeks later, the decisions made thus far have more than paid off.
I’ve developed a standard JSON message class that is implemented on both
the client and server, mirroring one another. This “protocol” is used to
quickly send data back and forth, and makes the source code on both
sides very readable and compact.

Using Django to power the server product means that the whole system is
easily managed from just about any browser, and the JSON message
protocol I’ve developed may be used by customers to interact with the
server from their own applications.

A lot of this is obvious stuff, but I figured I’d throw it out there for
those that might be interested in a really great combination of technologies.
