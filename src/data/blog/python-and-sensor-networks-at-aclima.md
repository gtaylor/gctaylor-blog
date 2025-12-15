---
author: Greg Taylor
pubDatetime: 2015-04-02T16:00:00+00:00
modDatetime:
title: Python and Sensor Networks at Aclima
slug: python-and-sensor-networks-at-aclima
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

After a few weeks at [Aclima](http://aclima.io/), I feel like I’ve got my bearings enough to start talking about our challenges and what we’re doing with Python. It’s always interesting to hear case studies, so I’ll toss ours on to the pile.

A brief overview of Aclima
--------------------------

![](https://images.squarespace-cdn.com/content/v1/561aafd6e4b02c7f0270ba4f/1445585066189-7LVM395HMHDK88SZB7CD/image-asset.jpeg?format=original)

The best way to gain insight into how a system operates or responds to stimuli is to measure and observe it over time. By looking at historical data, we can find interesting interactions, correlations, and inspiration for future research. Sometimes, such efforts lead to sweeping changes in theories, policies, and even public opinion. A few convenient examples of such tidal shifts in opinion are drastic reductions in cigarette, lead, and asbestos usage.

The environment around us has all sorts of systems that we don’t understand particularly well. For example, the consequences of pollution on a global (and local) scale are still not particularly well understood. At an even more localized level, any number of things can influence the conditions inside of a building (and the health of its inhabitants).

As interesting as it is to measure data for the sake of measuring, the data itself isn’t particularly valuable without analysis and insight. Fortunately, [Aclima](http://aclima.io/) handles the whole process, from designing and deploying the sensors, to collecting the data and performing analysis. The end product is actionable data or recommendations, or an on-going conversation with deployment partners to change the way we imagine and manage our buildings, communities, and cities.

Where Python comes into play
----------------------------

It would be possible to build the backend for our sensor networks on any number of programming languages. However, Python has snagged a huge chunk of mindshare in the engineering and science community. It is also an incredibly capable general-purpose language. Consequently, our infrastructure and research teams both make extensive use of Python.

Some of the critical things we use Python for include (but aren’t limited to):

* The ingestion of data points in tight intervals from sensors all around the world.
* Automated analysis and tagging of incoming data.
* Querying, charting, and analyzing the data that we have gathered.
* Deploy/config management ([Ansible](http://www.ansible.com/home)).
* Various internal tools.
* [SciPy](http://www.scipy.org/) and [Pandas](http://pandas.pydata.org/) are incredibly useful!

Challenges for the backend team
-------------------------------

Since my position is within the backend team, I am most well-equipped to share some of the things we’ll be working on in the near term:

* Reliably handling inbound sensor data from thousands (or millions) of sensors around the world.
* Reducing the chance of data loss due to outages or minor disruptions in the backend.
* Building tools for our team and our customers to review and analyze the data.
* Working with interesting technologies such as [Cassandra](http://cassandra.apache.org/), [Docker](https://www.docker.com/), [Flask](http://flask.pocoo.org/), and more.
* Incorporating machine learning.
* Automating. Everything.

If any of this sounds interesting, we’re hiring!
------------------------------------------------

If building large, highly resilient, highly scalable sensor networks sounds interesting to you, check out our [Backend Software Engineer](https://boards.greenhouse.io/aclima/jobs/26120) position. We are planning to grow our team substantially this year. We also have a number of other [openings](https://boards.greenhouse.io/aclima) on the frontend, device, and research teams.
