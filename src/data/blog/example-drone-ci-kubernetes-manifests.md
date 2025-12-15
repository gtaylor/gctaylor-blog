---
author: Greg Taylor
pubDatetime: 2015-10-28T03:57:29+00:00
modDatetime:
title: Example Drone CI Kubernetes manifests
slug: example-drone-ci-kubernetes-manifests
featured: false
draft: false
tags: ["Kubernetes", "CI", "Google Cloud", "Cloud", "Docker", "DevOps"]
description: ""
---

**Update 9/22/2016: This blog post was eventually used to create a [drone-on-kubernetes](https://github.com/drone-demos/drone-on-kubernetes) demo repository. Check that out for more up-to-date examples.**

I've been evaluating [Drone](https://github.com/drone/drone), with the goal to get it running on [Kubernetes](http://kubernetes.io/). I figured I'd share some *very* preliminary manifests, for anyone who else may be tinkering. How to use these is outside of the scope of this article, but [Google Container Engine](https://cloud.google.com/container-engine/) is an easy way to get going.

The first order of business is to create a service to serve as an entrypoint. The end result of this on Google Cloud is a [Network Load Balancer](https://cloud.google.com/compute/docs/load-balancing/network/) with a public IP. The creation of the load balancer is handled by Kubernetes. Here's the manifest I used (HTTPS-only, in my case).

After setting a DNS entry up to point at the load balancer's public IP, the next step was to get a [replication controller](http://kubernetes.io/v1.0/docs/user-guide/replication-controller.html) set up.

A bit lengthy, but we're using the Kubernetes [Secrets API](http://kubernetes.io/v1.0/docs/user-guide/secrets.html) to store our SSL certs/keys. Our data store is SQLite, persisted with Kubernetes [gcePersistentDisk](http://kubernetes.io/v1.0/docs/user-guide/volumes.html#gcepersistentdisk). You can replace this with something else if you aren't on Google Cloud, or switch to one of the other DBs that Drone [supports](http://readme.drone.io/setup/).

While I have glossed over a lot of details, this was enough to get us up and running well enough to start evaluating Drone.

Here are a few ideas for future improvements:

* The keys in REMOTE\_CONFIG should be stored in the Secrets API. There is currently (Kubernetes 1.0) no direct way to pull a secret directly into an environment variable in the manifest. The current workaround seems to be to create a shell script to use as the Docker container's entrypoint, pulling the values from the mounted secrets volume and stuffing them in environment variables.
* HTTP -> HTTPS redirect (if you please).
* X.509 auth might be a good idea, depending on your usage case.
* DB persistence in something other than SQLite for any more active installs.
