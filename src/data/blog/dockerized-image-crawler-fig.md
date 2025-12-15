---
author: Greg Taylor
pubDatetime: 2015-01-10T10:44:00+00:00
modDatetime:
title: Networked, multi-container image crawling with Docker and fig
slug: dockerized-image-crawler-fig
featured: false
draft: false
tags: ["Python", "Programming", "Docker"]
description: ""
---

Like many, I’ve been playing with [Docker](https://www.docker.com/) as it has been developing. I feltreasonably comfortable creating images and running isolated containers, but
I had yet to tinker with automatically provisioning and networking multiple
containers together.

To remedy this, I spent a weekend writing a simple distributed dockerized
image crawler using [Twisted](https://twistedmatrix.com/), [Docker](https://www.docker.com/), and [fig](http://www.fig.sh/). The full source (under a BSD
license) can be found in the [Github repo](https://github.com/gtaylor/dockerized-image-crawler).

The [README](https://github.com/gtaylor/dockerized-image-crawler/blob/master/README.rst) covers a lot of this in more detail, but the application is
comprised of three container types:

* An HTTP web API for enqueuing jobs. For the sake of this example, you only
  run one of these, but it’d be easy to adapt the code to support multiple instances.
* A worker container that carries out the image crawling. You can run as many
  as these as you’d like.
* A Redis container that is used for tracking job state and results.

The worker daemons connect to the HTTP web API container over ZeroMQ, PULLing
jobs that the HTTP daemon PUSHes. If this were anything but a toy app, you’d
probably want a proper message broker that could offer stronger deliverability
and persistence guarantees.

Assorted Observations
---------------------

* I may have been doing something wrong, but [boot2docker](http://boot2docker.io/) seems to be pretty
  rough with volume mounting. It looks like it’d be pretty easy to mount
  a directory within the boot2docker VM, but the host machine->container sharing
  didn’t work in real-time. I expect this will improve with time, or I could
  have missed something.
* [fig](http://www.fig.sh/) is a great idea, and is very handy. I’m looking forward to seeing where
  this concept is taken over the next few years.
* There is a great [python:2.7](https://registry.hub.docker.com/_/python/)
  image on Docker Hub that serves as a great starting point. They’ve got all
  sorts of other versions and alternative implementations ([PyPy](https://registry.hub.docker.com/_/pypy/)) covered.
