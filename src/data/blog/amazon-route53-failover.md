---
author: Greg Taylor
pubDatetime: 2013-04-02T00:03:00+00:00
modDatetime:
title: Amazon Route 53 DNS failover
slug: amazon-route53-failover
featured: false
draft: false
tags: ["Cloud", "DevOps", "Programming"]
description: ""
---

While it is no longer shiny and new, I just recently got a chance to sit down andplay with [Amazon Route 53’s DNS failover](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
feature. So far, I have found it to be simple and very useful for simple
cases where DNS fail-over is acceptable.

My usage case
-------------

I run [EVE Market Data Relay](http://www.eve-emdr.com/) (EMDR), which
is a distributed EVE Online market data distribution system. All pieces of
the infrastructure have at least one redundant copy, and the only single
point of failure is the DNS service itself. We can afford to lose a little
bit of data during fail-over, but a complete outage is something we can’t have.

Sitting at the top of the system are two HTTP gateways on different
machines at different ISPs. These are set up as a weighted record set, with
each gateway weighing in at 50/50 (requests are divided evenly).

We introduce the Route 53 magic by adding in a health check and associating
it with each of the two resource record sets. The health check involves
Route 53 servers around the world periodically calling a pre-determined
URL on the two HTTP gateways in search for a non-error HTTP status code.
If any of the entries fails more than three times (they check roughly
every 30 seconds), said entry is removed from the weighted set.

By the time that Route 53 picks up on the failure, yanks the entry from
the weighted set, and most fast ISP DNS servers notice the change, about
two minutes have elapsed.

Why this is a good fit for EMDR
-------------------------------

With [EVE Market Data Relay](http://www.eve-emdr.com/), it’s not the end of
the world if 50% of user-submitted data gets lost over the minute and a half
it takes for Route 53 to remove the unhealthy gateway. It’s highly likely that
another user will re-submit the very same data that was lost. Even if we never
see the data, the loss of a few data points here and there doesn’t hurt us much
in our case.

With that said, DNS failover in general can be sub-optimal in a few basic cases:

* You don’t want to leave failover up to the many crappy ISP DNS servers
  around the net. Not all will pick up the change in a timely manner.
* You can’t afford to lose some requests here and there. DNS failover isn’t
  seamless, so your application would need to be smart enough on both
  ends if data loss is unacceptable.

For more simple cases like mine, it’s wonderful.

Price
-----

In my case, Route 53 is health checking two servers that are external to
AWS, which means I spend a whopping $1.50/month on Route 53’s DNS failover.

Assorted useful bits of documentation
-------------------------------------

More details on how the health checks work can be found on the
[Route 53 documentation](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html).

Refer to the [Amazon Route 53 DNS failover](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
documentation for the full run-down.
