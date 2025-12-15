---
author: Greg Taylor
pubDatetime: 2016-10-31T09:02:10+00:00
modDatetime:
title: Fire up an interactive bash Pod within a Kubernetes cluster
slug: fire-up-an-interactive-bash-pod-within-a-kubernetes-cluster
featured: false
draft: false
tags: ["Kubernetes", "How To"]
description: How to start an interactive bash Pod on Kubernetes.
---

*Note: This blog post is a very old and is preserved here for reference. There are probably better ways to do this today!*

In those cases where you need a throw-away interactive shell within your cluster:

You may, of course, use a different image or shell. Some of the arguments explained:

* **my-shell**: This ends up being the name of the Deployment that is created. Your pod name will typically be this plus a unique hash or ID at the end.
* **--rm**: Delete any resources we've created once we detach. When you exit out of your session, this cleans up the Deployment and Pod.
* **-i/--tty**: The combination of these two are what allows us to attach to an interactive session.
* **--**: Delimits the end of the kubectl run options from the positional arg (bash).
* **bash**: Overrides the container's [CMD](https://docs.docker.com/engine/reference/builder/#/cmd). In this case, we want to launch bash as our container's command.

Note that you'll need to update your apt cache before you can install packages:

Once you are done with your tinkering:

Post-exit, the Deployment and Pod that kubectl created will both be stopped and deleted, taking with it our container and anything we did within it.
