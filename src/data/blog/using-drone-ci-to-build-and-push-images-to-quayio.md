---
author: Greg Taylor
pubDatetime: 2015-11-20T06:17:42+00:00
modDatetime:
title: Using Drone CI to build and push images to Quay.io
slug: using-drone-ci-to-build-and-push-images-to-quayio
featured: false
draft: false
tags: ["CI", "Docker", "DevOps"]
description: ""
---

As my experimentation with [Drone](https://github.com/drone/drone) continues, the latest task was to get Docker images building and published to [Quay.io](https://quay.io) (more on I'm using Quay [here](http://gc-taylor.com/blog/2015/10/14/the-journey-to-quay-io)).

Drone uses a .drone.yml file to determine what happens in response to a `git push` (or other events). I tend to use the [build](http://readme.drone.io/build/build.html) section (not shown below) for running tests, and the [publish](http://readme.drone.io/build/publish.html) section for actually building and publishing the image from a Dockerfile. Here's a quick example of how the image creation and publishing works:

Let's break this down a bit. The first **registry** field is optional if you are pushing to Docker Hub, but required if you want to push to anything else. It's sort of like how you have to explicitly specify the registry to pull from in `docker pull` for non-Docker Hub images.

The values for **username** and **password**  correspond to a [robot account](https://docs.quay.io/glossary/robot-accounts.html) on Quay.io we're using for publishing this particular image. Robots serve as an easily-restricted way to provide access to a repo without handing over the keys to the kingdom. You'll notice that we've got some weird $$QUAY\_\* values in there as well. These are variables that are substituted in via Drone's [Secret Variables](http://readme.drone.io/build/secrets.html) feature (don't commit un-encrypted credentials!).

The **email** value is ignored on Quay.io robot accounts, so I made something up. This will vary by image registry, so read your docs!

**Repo** points at the repo in Quay.io (excluding the quay.io prefix).

Similar to the [Secret Variables](http://readme.drone.io/build/secrets.html) feature we used above for username/password, $$TAG gets substituted with whatever **tag** was pushed during the build trigger. There are a few [variables](http://readme.drone.io/build/env.html) like this that you can inject.

The **file** key/val determines which Dockerfile is used to build the image before pushing.

And finally, then **when** clause. In our particular case, I only wanted to run this Docker image publish when a tag was pushed to git (signifying a new release). Not shown above are some previous sections that run our unit and integration tests. Those are set to run on every push. The end result is that all pushes (commits and tags alike) result in tests being ran, while only tags trigger our automated publish->deploy flow.

Hopefully this helps someone out there. Be sure to comment if you have questions.
