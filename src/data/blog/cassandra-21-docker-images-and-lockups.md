---
author: Greg Taylor
pubDatetime: 2015-12-23T22:57:54+00:00
modDatetime:
title: Cassandra 2.1 Docker images and lockups
slug: cassandra-21-docker-images-and-lockups
featured: false
draft: false
tags: ["Cassandra", "DevOps"]
description: ""
---

We recently noticed that we had locked up Cassandra Docker containers piling up when running our integration tests.

![](https://images.squarespace-cdn.com/content/v1/561aafd6e4b02c7f0270ba4f/1450911218546-G55WXSGIILXM7I2MP26P/image-asset.png?format=original)

After digging around some more, we saw some others complaining of similar symptoms. Something in common with all cases was the use of Cassandra 2.1.x images. After seeing someone mention that Cassandra 2.2 and 3.x images weren't showing this behavior, we gave it a shot.

As luck would have it, this did the trick! So for anyone else running into Cassandra Docker containers with the following symptoms, consider switching to 2.2+:

* Containers never fully start, hanging after creation.
* Containers can't be rm'd or killed.
* *docker logs* shows no output in addition the the previous two.
