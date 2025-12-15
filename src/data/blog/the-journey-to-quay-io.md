---
author: Greg Taylor
pubDatetime: 2015-10-15T04:35:53+00:00
modDatetime:
title: The journey to Quay.io - An introspection and review
slug: the-journey-to-quay-io
featured: false
draft: false
tags: ["Reviews", "Docker", "DevOps"]
description: ""
---

I've been doing a CI/CD setup revamp of late, which led to me kicking the tires of a bunch of different build/test systems. The goal was to put together a CI/CD pipeline that the entire team would feel comfortable using. My deploy target was a number of [Kubernetes](http://kubernetes.io/) clusters.

With much of our services already being adapted to work with [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/), we were ready to figure out which combination of systems would build and test our images.

I wish I knew how to quit you, Jenkins
--------------------------------------

We started by re-visiting our existing Jenkins install, with the aim to adapt it to play nice with our new Docker+Kubernetes setup. We were going to build and test the images on Jenkins, eventually pushing them to [Google Container Registry](https://cloud.google.com/container-registry/) ([Google Container Engine](https://cloud.google.com/container-engine/) has convenient integration and it's super cheap).

As a small engineer team, we ended up deciding against putting together and maintaining a Jenkins setup for a set of technologies that is so rapidly changing (Docker, docker-compose, Kubernetes, etc). GCR's permissions and authentication situation was also super rough.

Checking in on Docker Hub
-------------------------

[Docker Hub](https://hub.docker.com/) became my next stop, as it served me well with [emdr-relay-go](https://hub.docker.com/r/gtaylor/emdr-relay-go/) in the past. While it fit the bill as an image repository exceptionally well, I found the auto-build features (the hooks into specific branches/tags) and permissions to be too limited.

While I wasn't over-the-moon about Docker Hub, it would certainly work if there weren't any better options. I kept looking, to be sure I hadn't missed anything.

What is a Quay, anyway?
-----------------------

![](https://images.squarespace-cdn.com/content/v1/561aafd6e4b02c7f0270ba4f/1444887916077-UDJSIDT2EWHTKN35EZ1R/image-asset.png?format=original)

At that point, I recalled that I had heard of something called [Quay.io](https://quay.io/). At a glance, it was a bit more [expensive](https://quay.io/plans/) than Docker Hub. I had vaguely recalled that CoreOS had bought them a while back. Since I wasn't as happy with Docker Hub as I had hoped, I signed up for a trial and started building some of our images.

Things that immediately caught my eye
-------------------------------------

While I was greeted with a relatively barren, empty dashboard upon completing signup, things came to life pretty quickly as I added repositories and build hooks. Some things that made a quick impression on me:

* There was no separate notion of a Library vs Auto-Build repository like Docker Hub. A Quay repository can fit each of these without needing to be created specifically in either mode.
* It is possible to set all kinds of build triggers and filters (only build for these branches/tags.
* Quay's permission system was just enough to fit our usage cases. They support specifying defaults for newly created repos, and I love their [Robot Accounts](http://docs.quay.io/glossary/robot-accounts.html).
* Quay's build screen absolutely shames Docker Hub's. It updates in quasi-realtime, is a lot more compact, and is much more attractive to boot.
* While still in a Preview state, the Quay API is [thorough](http://docs.quay.io/api/swagger/) and reasonably well-documented.
* The tag "Visualize" feature is super handy. We can look at a maps-style view of the various Docker image layers that comprise a tag, allowing us to see an approximate of the size increases for each of the layers. While there are ways to get at this via the CLI, much of our team can benefit from this easy-to-use graphical view.
* The team immediately picked up on how to get around and use Quay. They were deploying built images to our Kubernetes clusters within a few hours of me starting to evaluate the service.

Things that could be better
---------------------------

* We noticed a fairly consistent 2-3 minute lead time before a scheduled build would actually start. Quay support mentioned that this was due to needing to spin up a new EC2 instance to ensure isolation and security. I hope they can find ways to get this down a bit, as this represents a non-trivial delay in our build/test/deploy process.
* When navigating into a build, it takes a good while to retrieve the build log. While Docker Hub's build page is hideous and doesn't seem to auto-refresh, it is fast. This is probably one of my biggest sticking points, as it actively keeps me from getting things done quickly.
* Docker Hub's support has been a bit faster to respond to questions. Quay's isn't necessarily slow (I got a response within 24 hours), they just weren't as fast. This probably comes down to the size of each of the teams. We aren't too concerned about this.

In summary
----------

We're still on our first week of using Quay, so we'll see how things develop over time. Preliminary indications are that this is an excellent (if a bit more pricey) service that will only improve over time.

If usability and granular permissions are a must for you, I'd suggest Quay over Docker Hub as of the time of this article's writing (Q4, 2015). These were two of our biggest needs, so your mileage may vary.

If you don't care a lick about usability or fine-grained permissions, Docker Hub is cheaper and is the docker client's default registry.

You probably can't choose wrong out of these two, and I'd expect both to continue getting better.
