---
author: Greg Taylor
pubDatetime: 2015-10-23T07:19:50+00:00
modDatetime:
title: Where does Google Cloud fit in the IaaS market?
slug: google-cloud-and-the-iaas-market
featured: false
draft: false
tags: ["Cloud", "DevOps", "Kubernetes"]
description: ""
---

After spending the last five years working almost exclusively within the [Amazon Web Services](https://aws.amazon.com/) ecosystem, 2015 has been full of lots of [Google Cloud](https://cloud.google.com/) (GC) work for me. This wasn't necessarily a conscious decision, but more a side effect of a new job.

After making the switch my initial impression was lukewarm. In many ways, Google Cloud is following in the footsteps of AWS, but trails by a substantial margin. It was difficult to anticipate what differentiating niche they'd carve out as recently as Q1 of 2015. Sure, Google was able to look at some of the mistakes AWS made and do slightly better. I just didn't see a lot that would make me recommend GC over AWS for general-purpose usage cases.

Then things got interesting
---------------------------

Q2 and Q3 saw some interesting announcements. I'd like to focus on one in particular: August 26, [Google Container Engine](https://cloud.google.com/container-engine/) (GKE) left beta. Unless you were eagerly anticipating this general availability announcement, you probably would have missed it.

GKE is a hosted [Kubernetes](http://kubernetes.io/) service. Google runs the masters, while the minions are managed VMs that you have access to. Sounds neat, but not necessarily a game-changer for Google Cloud so far. Poking around in the Kubernetes documentation, I found some curiously [neat](http://kubernetes.io/v1.0/examples/simple-nginx.html) [creature](http://kubernetes.io/v1.0/docs/admin/networking.html#google-compute-engine-gce) [comforts](http://kubernetes.io/v1.0/docs/user-guide/volumes.html#gcepersistentdisk) specifically aimed at Google Cloud. This makes perfect sense, as Kubernetes originated from and is being invested in by Google.

After experimenting with GKE and even deploying some simple production systems on it, I came away very impressed. They've definitely got a good thing going. Despite my very positive initial impression, Google has spent precious little time extolling the virtues of GKE on the Google Cloud [blog](http://googlecloudplatform.blogspot.com/). This has all of the trappings of a lesser product or a response to Amazon's [Elastic Container Service](https://aws.amazon.com/ecs/) (ECS).

But it's bigger than that!

Containerization
----------------

Before 2013, containerization was something that only the most talented organizations could hope to employ in any significant manner. The underpinnings were there, but they were much more difficult to use for mere mortals. The edges were sharper, the guts less settled. dotCloud came along and changed that with Docker.

Fast forwarding to 2015, containers are being employed all over the place. Everyone ranging from Google to Microsoft is throwing their weight behind this new world order. While we will ultimately see another future shift in how we deploy and run our systems, this is where things will be for the forseeable future.

Amazon and Google containerized very differently
------------------------------------------------

Amazon was timely in their release of [Elastic Container Service](https://aws.amazon.com/ecs/) (ECS) in April of 2015. It looked capable, interesting, and useful for those who didn't want to set up and administer their clusters. But it had and still has a fatal flaw: ECS is entirely proprietary, like much of AWS (and Google Cloud). As a consequence, there are some significant drawbacks that IaaS users will be all too familiar with:

* If you want to run a some of your ECS clusters on AWS and others on-site (or on another IaaS provider), you are out of luck. ECS is closed source and only available on AWS.
* You aren't able to fix bugs or customize ECS.
* You can't get a look at the source for ECS if you want clarification on mechanics.
* You aren't able to submit feature work or pull requests to ECS.
* While you aren't fully vendor-locked (Docker containers are still the core piece), you will need to significantly change how you deploy your systems if you move from ECS to another solution.

By contrast, Kubernetes:

* ... can run on just about any IaaS provider, or your own hardware.
* ... is open source. Fix bugs or customize away.
* ... has publicly available and developed source [Github](https://github.com/kubernetes/kubernetes).
* ... appreciates and accepts pull requests from the greater community.
* ... helps break vendor-lock, since you are running on a higher abstraction level. Almost any application that runs on Kubernetes+GKE can be adapted to run on other providers without a big time suck.

*By building Google Container Engine around an open source system and throwing significant weight behind it, Google is looking much better long term for container-heavy organizations*.

Building for the long haul
--------------------------

The container orchestration war is just getting started but is already very competitive. Google is throwing substantial weight behind Kubernetes to make sure it has its spot out front. By offering hosted Kubernetes and incorporating some neat add-ons, I think Google Cloud will be super attractive to those with a "containerize most of the things" mentality. After all, Google has [significant](http://research.google.com/pubs/pub43438.html) [experience](http://research.google.com/pubs/pub41684.html) with containers going back many years.

Additionally, Google's existing and probable future features could jive really well with GKE:

* [Auto-scaling](https://cloud.google.com/compute/docs/autoscaler/) of clusters already sort of works, even in the early goings. This can be based on things like cluster CPU util, network traffic, or even custom metrics. I expect that this will only improve over time.
* Adding the ability to add nodes of varying sizes to a cluster would be great once the Kubernetes scheduler improves. Tagging and resource usage could factor in nicely.
* Building on the last, it would be super neat if a fleet could be supplemented with [preemptible](https://cloud.google.com/preemptible-vms/) nodes.
* [Google Container Registry](https://cloud.google.com/container-registry/) is rough but cheaper than just about any other image registry (hosted or self-serve).
* You can already do some [neat things](http://kubernetes.io/v1.0/docs/user-guide/services.html#type-loadbalancer) with Kubernetes service with GCE [Load Balancers](https://cloud.google.com/networking/#loadbalancing). I expect that this will be hugely expanded over time.
* [Google Cloud DNS](https://cloud.google.com/dns/docs) integration is a no-brainer.
* I foresee some interesting opportunities to use GCE [networks](https://cloud.google.com/compute/docs/load-balancing/network/) for neat things in GKE.

While Google Cloud won't ever "kill" AWS, I do think that it will eventually be a better choice for those wanting to develop, deploy, and run non-trivial containerized systems. That is, until or unless AWS pivots a bit with their approach.

More generally, Google Container Engine sort of fills a nice gap between full IaaS and PaaS offerings. Turn some knobs to adjust your cluster (which is managed by Google), but deploy your systems via APIs like Heroku. All at a lower price and easier exit trajectory if you ever need to shift to something else.
