---
author: Greg Taylor
pubDatetime: 2013-12-03T22:40:00+00:00
modDatetime:
title: When (and when not) to use EC2
slug: when-and-when-not-to-use-ec2
featured: false
draft: false
tags: ["Cloud"]
description: ""
---

There is a lot of advice on the internet regarding the suitability of [EC2](http://aws.amazon.com/ec2/).One can easily find all kinds of benchmark and price comparisons, long rants
on Cloud vs Bare metal, and any number of other reasons for or against using [EC2](http://aws.amazon.com/ec2/).
I feel that a lot of these articles miss the mark entirely, and figured I’d
toss up my own attempt at guidelines for choosing (or avoiding) [EC2](http://aws.amazon.com/ec2/).

This article will attempt to provide a simple list of some (but not all)
cases where EC2 is and isn’t a good fit. I will undoubtedly miss some, and there
are exceptions to every case, but take these as a set of general guidelines.
Also, for the sake of brevity, I assume that you have a basic grasp of
what [EC2](http://aws.amazon.com/ec2/) is. If not, check out the [EC2](http://aws.amazon.com/ec2/) page before continuing.

EC2’s killer feature
--------------------

Before we get to the fun stuff, I want to take a moment to highlight
EC2’s killer feature: **Elasticity**. Here are some important bits extracted
from the AWS [EC2](http://aws.amazon.com/ec2/) page:

```
Amazon EC2’s simple web service interface allows you to obtain and
configure capacity with minimal friction.
[...]
Amazon EC2 reduces the time required to obtain and boot new server instances
to minutes, allowing you to quickly scale capacity, both up and down, as
your computing requirements change. Amazon EC2 changes the economics of
cloud computing servers by allowing you to pay only for capacity that
you actually use.
```

EC2’s primary goal is to make it easy to provision and destroy VMs as needed.
They’ve got an advanced set of HTTP APIs for managing your fleet, a very good
set of imaging/provisioning utilities, a wide variety of instance sizes to
choose from, and they even excellent auto-scaling capabilities built into [ELB](http://aws.amazon.com/elasticloadbalancing/).
The hourly billing allows you to handle bursts of traffic without a long-term
commitment, and you can also fire up experimental/tinker instances without much expense.

There are other services that also offer some of these things individually, but
EC2 is at the front of the pack when it comes to provisioning instances and
scaling up/down.

It’s not all sunshine and roses
-------------------------------

*“That sounds great! Why would I ever want to use anything else?”*

* The performance per dollar is atrocious. Be prepared to shell out for
  a larger instance to get consistent performance. This is more of a barrier
  for projects with smaller budgets. In the case of a very well-funded project,
  infrastructure spend is (probably) much less of a concern.
* Amazon Web Services in general features a pretty steep learning curve before
  one can make informed infrastructure decisions. You’ll need to learn about security
  groups, [EBS](http://aws.amazon.com/ebs/), EC2’s SSH key management system, how snapshots/AMIs work,
  performance characteristics, common sources of failures, etc.
* The lower end instances (below m1.large) are embarrassingly underpowered
  and erratic. For services or applications with low resource requirements,
  this may or may not be an issue. Make sure you benchmark and test before
  committing to a reservation!
* [EBS](http://aws.amazon.com/ebs/) has had serious reliability issues and is very inconsistent
  performance-wise without [Provisioned IOPS](http://aws.amazon.com/ebs/piops/) or RAID. The majority of the
  larger EC2 outages have been due to EBS issues.
* The customer service is abysmally bad. Unless you pay for a [Support Plan](http://aws.amazon.com/premiumsupport/),
  your only option is to post to a public forum and hope that someone from
  AWS replies. I understand that AWS operates at a huge scale, but I expect
  better from a company full of brilliant people like Amazon. Telling paying
  customers (without a support plan) to post in the forums for help is
  inexcusable. A support plan should be for above-and-beyond service.

*“That was discouraging. Let’s get back to the good stuff.”*

EC2 is a potential good fit for your application when…
------------------------------------------------------

* You want/need to be able to scale up and down to meet handle traffic.
  This can be done automatically via [ELB](http://aws.amazon.com/elasticloadbalancing/) (after some setup work), via the
  EC2 HTTP API, or by the more traditional web based management console.
* Your application *has* to have consistently fast, low latency access to at
  least one other AWS service.
* Your application pumps enough traffic into/out of an AWS service and
  you don’t want to pay the higher external traffic tolls.
* You plan on using a number of managed services that typically pair with EC2.
  For example, [ElastiCache](http://aws.amazon.com/elasticache/), [RDS](http://aws.amazon.com/rds/), [CloudSearch](http://aws.amazon.com/cloudsearch/), and etc. These can be a
  life-saver if your team doesn’t have the ops/administrative skill to manage
  the equivalent EC2 instances yourselves. Though, they’re not always a good
  value for teams with some ops chops in-house.
* You have enough budgeted to pay for the instance sizes that are appropriate
  for your performance needs. For many/most, this probably involves buying
  at least some instance reservations.
* EC2 would allow you to streamline your operations processes enough to
  allow you to run with a smaller ops team. Spending more for infrastructure
  convenience is a lot less expensive than hiring another employee.

EC2 is probably not a good fit for your application when…
---------------------------------------------------------

* You don’t need to scale up/down much. This is one of the biggest
  strengths of EC2. If you aren’t using it, you can go with something
  much cheaper/faster/more reliable/more consistent.
* You can’t afford to pay for redundancy, but your application has high
  stability/availability requirements. EC2 instances fail, EBS volumes fail
  or slow down randomly, entire availability
  zones fail. The systems supporting EC2 are incredibly complex and
  operate at a massive scale. Stuff happens. If you can’t afford some
  measure of cross-availability-zone redundancy (at minimum) and your application
  has stability requirements, EC2 is probably not for you.
* The need to purchase 1-3 year instance reservations to get decent hourly rates
  on instances bothers you. The On Demand rates can be incredibly expensive if
  you run instances with them for extended periods of times. A reservation
  requires the upfront payment of a large chunk of the next 1-3 year’s costs.
  This can be a problem for those without enough liquid capital. It also means
  that adding additional capacity can be a larger business decision.
* Your application has components that require very consistent performance,
  but you can’t afford one of the very large instance sizes that have few
  to no neighbors on the host machine. Very high activity DB servers often
  fall into this category.
* You are wanting to eventually incorporate bare metal servers into your fleet.
  EC2 currently only offers virtualized instances, though you can rent out
  an entire host machine for yourself.
  Alternatively, you can use [Direct Connect](http://aws.amazon.com/directconnect/) to bridge to certain data
  centers, but you’ll want to make sure this fits in your architecture and budget.

Advice on deciding for or against EC2
-------------------------------------

Read through the cases outlined above again and keep a tally of how many
apply for your project. If you find that a good number of the cases under
“good fit” apply, EC2 is probably worth further consideration. If you find that
more than 1-2 of the scenarios under “not a good fit” are true, you should
probably tread more carefully.

Exceptions, omissions, and etc
------------------------------

*“But you forgot X case, or your advice isn’t appropriate for my usage case!”*

This article attempts to be decent one-size-fits-most guide, but there are
exceptions and other scenarios that I didn’t cover. If you know some of
these, you probably don’t need this guide. If I missed something super obvious,
leave a comment and I’ll update the article.

I don’t cover comparing prices against other providers in this article, but I’d
like to point out that some of EC2’s price is there because of convenience and
flexibility. You are paying extra for the ability to interact with stuff like
[ELB](http://aws.amazon.com/elasticloadbalancing/), [CloudWatch](http://aws.amazon.com/cloudwatch/), and other services. Perhaps I’ll follow up with another
article expanding on this more if there’s interest…

In the end, it will come down to you identifying your requirements and finding
the best fit.

On a related note, if you need help or advice with infrastructure planning,
get in touch with me via the Contact link on the top navbar.
