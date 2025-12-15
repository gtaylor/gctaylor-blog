---
author: Greg Taylor
pubDatetime: 2011-08-23T00:03:00+00:00
modDatetime:
title: Amazon ElastiCache review
slug: amazon-elasticache-review
featured: false
draft: false
tags: ["Cloud", "Reviews"]
description: ""
---

Amazon Web Services has just announced the beta release of [AmazonElastiCache](http://aws.typepad.com/aws/2011/08/amazon-elasticache-distributed-in-memory-caching.html), a hosted/managed [memcached](http://memcached.org/) service. This is an offer
similar to [Relational Database Service (RDS)](http://aws.amazon.com/rds/) in that the management
and clustering is handled for you, leaving you with a host/port to point
your services at.

Powered by Memcached
--------------------

Their announcement doesn’t provide too many details about the inner
workings of the ElastiCache, but it appears the initial beta is some
form of memcached 1.4.5. It’s entirely possible that they have made modifications.

There may be future additions of different engines, such as Redis, but
AWS has not provided any indications of this happening in the immediate future.

Unlike some of the recent AWS feature launches, ElastiCache sports a tab
on the AWS Management Console, which is great. Administering your
clusters looks to be dead simple.

Performance and benchmarks
--------------------------

It’s still pretty early, and I haven’t been able to find any benchmarks
comparing an EC2 instance with Memcached to ElastiCache. However, keep a
few things in mind:

* You can deploy your ElastiCache to single or multiple availailibty
  zones. Instances within the same zone can communicate with
  ElastiCache just as fast as they can to neighboring EC2 instances.
* It is likely that like RDS, Amazon has tweaked the instances that run
  ElastiCache specifically for this workload.

That said, my uneducated guess would be that performance between a
properly configured EC2 instance and ElastiCache will be negliglble. But
that’s not what they’re selling you on. You’re paying the premium for
not having to manage that part of your stack.

Usage case
----------

For sites with low to moderate traffic, running a dedicated memcached
instance may not be worth the money, or an increase in your service’s
footprint. It is often fine to run a memcached server on the same
instance as your app server. Memcached is great about not using much
CPU, but it will happily consume as much RAM as you allow it to.

As your site grows, you may find that memcached actively uses RAM that
your app server needs, causing resource contention. Worse case, you may
find yourself hitting swap space. This can be absolute death for even
moderately trafficked sites.

For those that are finding their memcached process needing more and more
RAM to satiate your application’s needs, it’s probably time to explore
breaking your caching out into its own EC2 instance, or ElastiCache.

Price
-----

ElastiCache clusters come in sizes similar to EC2 instances: Small,
Large, XL, etc. On the lower end, the monthly price for a single-node,
Small On-Demand ElastiCache cluster is about $70. To serve as a basis
for comparison, a Small On-Demand EC2 instance costs about $63. For
those that actually use On-Demand instances over prolonged periods of
time, the difference is negligible. You’re paying a $7/month premium to
not have to hassle with administering your memcached instance.

However, the price difference for Reserved instances vs. On-Demand
ElastiCache is large. Let’s say you use a Small Reserved EC2 instance.
By the time you take into account the up-front reservation fee and the
reduced monthly fee, you’re looking at around $41/month for a 1-year
term. Since ElastiCache currently has no Reservation capability like EC2
yet, this leaves us with a marked difference in price points. A
single-node, Small On-Demand ElastiCache would be $756 for the whole
year, vs. $491 for the Small Reserved EC2 instance with a 1-year term.
That’s a $265 savings for doing it yourself and shelling out the
up-front reservation fee.

Cheaper alternatives
--------------------

For those that find the price for ElastiCache a little too high, there
are a few different options that might be more affordable:

* Run memcached on one of your current instances, or on the same
  instance as the app server. This assumes lower load/traffic. Make
  **sure** that you aren’t running out of RAM.
* Run memcached on an On-Demand Micro instance. This is one of the few
  useful tasks I’ve found for Micro instances. Recall that memcached is
  extremely easy on the CPU, and Micro instances have around 613 MB to
  play with. This would cost around $15/month On-Demand (less with a
  Reserved instance). If you are free-tier eligible, this route would
  be free for a year, if you haven’t already fired up another Micro instance.
* If you can afford the up-front fee, a Reserved Small EC2 instance is
  powerful enough to handle even well-trafficked sites. You could pay a
  little more and get two Small Reserved EC2 instances for a moderate
  bit more than a single-node Small ElastiCache cluster.

The verdict
-----------

I love that Amazon is adding this, and think it’ll be a competitive
service **eventually**. ElastiCache is currently in beta, and the prices
are higher while they’re figuring out their costs and margins. The lack
of a Reserved ElastiCache cluster option is unfortunately the killer. At
the higher ends in particular, On-Demand ElastiCache is a good deal more
expensive than the equivalent  Reserved EC2 instance.

**I strongly suggest waiting for the prices to come down**, and for the
ability to purchase Reserved ElastiCache clusters. As it stands, this
service isn’t cost-effective yet for the benefit.
