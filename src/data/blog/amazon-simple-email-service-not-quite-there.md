---
author: Greg Taylor
pubDatetime: 2011-04-20T03:25:00+00:00
modDatetime:
title: Amazon Simple Email Service: Not quite there
slug: amazon-simple-email-service-not-quite-there
featured: false
draft: false
tags: ["Programming"]
description: ""
---

We’ve been working on transitioning a larger customer’s website from anExchange-based email server to [Amazon Simple Email Service](http://aws.amazon.com/ses/), in an
effort to improve reliability and eliminate one more bit of reliance on
internal infrastructure. I’ll share our experiences here for others
considering the same thing.

The Good
--------

* The setup process was simple (subscribing to the service, getting
  production access).
* The API calls to SES are quick and reliable.
* Sending mail is easy.

The Bad
-------

* It makes sense to have to verify ownership of an address to use as a
  “reply-to” in headers, but it’s a real pain when you send from a
  bunch of emails under one domain. There’s no way to wildcard-verify
  the entire domain. Not a deal-breaker, but kind of annoying.
* There is no way to see delivery failures. Again, not a deal-breaker,
  but not ideal.

The Ugly
--------

* For higher-volume sites, migrating to SES is awful. You start with a
  1,000 emails per 24 hours quota, and have to increase the limit by
  consistently sending enough emails to put you in the neighborhood of
  your limit. See the [Growing your quota documentation](http://docs.amazonwebservices.com/ses/latest/DeveloperGuide/index.html?ManagingActivity.PlanningAhead.html) for more
  specifics. More on this later.
* Automated quota increasing hasn’t worked for us. We’ve been sending
  right near our quota for 6 days now without a bump. We’ve hit our
  limit a few times, and lost a handful of emails because of this,
  since we were planning on the quota increasing as advertised.

Quotas: Low, inflexible, and buggy
----------------------------------

Take one look at AWS’s [migration strategies](http://docs.amazonwebservices.com/ses/latest/DeveloperGuide/index.html?ManagingActivity.PlanningAhead.html) for SES and consider the
annoyance these represent for transitioning a large, active website. The
onus is on the developer or administrator to come up with some way to
only send 1,000 emails a day until SES gets around to bumping quotas up.
There is no way to go through a verification process (like PayPal or
some other email services) and just pay for what you use. There is no
real special consideration for those who need it. There are forms to ask
for an initially higher quota, but everyone ends up at the 1,000/24 hour
limit initially.

In our case, we worked around the migration annoyances. We send about
1,500-3,000 a day, so we just manually switched back and forth between
our old SMTP/Exchange setup and the new SES backend. We’ve been doing
this for 6 days now, whereas our quota should have bumped after day 3.
*Low quotas are one thing. Not raising the limits after the documented
period is even worse*.

The Recommendation
------------------

For very small sites, or those that are starting with SES, it can be a
great fit. It’s cheaper than the comparable services, it’s simple to get
set up with, and it’s fast and reliable. For sites that already have a
higher email volume, I’d suggest avoiding SES until it matures. It’s
still not documented clearly in some places, and the quota buggyness and
inflexibility mentioned earlier in this post are show-stoppers.

This one needs another six months in the cooker. I’m sure later
iterations will improve the service, as has been the case with the other
products offered in AWS.
