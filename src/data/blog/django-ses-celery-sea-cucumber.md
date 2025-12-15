---
author: Greg Taylor
pubDatetime: 2011-04-15T16:03:00+00:00
modDatetime:
title: django-ses + celery = Sea Cucumber
slug: django-ses-celery-sea-cucumber
featured: false
draft: false
tags: ["Python", "Cloud", "Django", "Programming"]
description: ""
---

Maintaining, monitoring, and keeping a mail server in good standing canbe pretty time-consuming. Having to worry about things like PTR records
and being blacklisted from a false-positive stinks pretty bad. We also
didn’t want to have to run and manage yet another machine. Fortunately,
the recently released [Amazon Simple Email Service](http://aws.amazon.com/ses/) takes care of this
for us, with no fuss and at very cheap rates.

We ([DUO Interactive](https://github.com/duointeractive)) started using [django-ses](https://github.com/hmarr/django-ses) in production a few
weeks ago, and things have hummed along without a hitch. We were able to
drop django-ses into our deployment with maybe three lines altered. It’s
just an email backend, so this is to be expected.

Our initial deployment was for a project running on [Amazon EC2](http://aws.amazon.com/ec2/), so
the latency between it and SES was tiny, and reliability has been great.
However, we wanted to be able to make use of SES on our Django projects
that were outside of Amazon’s network. Also, even projects internal to
AWS should have delivery re-tries and non-blocking sending (more on that later).

Slow-downs and hiccups and errors, oh my!
-----------------------------------------

The big problem we saw with using django-ses on a deployment external to
Amazon Web Services was that any kind of momentary slow-down or API
error (they happen, but very rarely) resulted in a lost email. The
django-ses email backend uses boto’s new SES API, which is blocking, so
we also saw email-sending views slow down when there were bumps in
network performance. This was obviously just bad design on our part, as
views should not block waiting for email to be handed off to an external service.

django-ses is meant to be as simple as possible. We wanted to take
django-ses’s simplicity and add the following:

* Non-blocking calls for email sending from views. The user shouldn’t
  see a visible slow-down.
* Automatic re-try for API calls to SES that fail. Ensures messages get delivered.
* The ability to send emails through SES quickly, reliably, and
  efficiently from deployments external to Amazon Web Services.

The solution: Sea Cucumber
--------------------------

We ended up taking Harry Marr’s excellent [django-ses](https://github.com/hmarr/django-ses) and adapting it
to use the (also awesome) [django-celery](https://github.com/ask/django-celery). Celery has all of the things
we needed built in (auto retry, async hand-off of background tasks), and
we already have it in use for a number of other purposes. The end result
is the now open-sourced [Sea Cucumber Django app](https://github.com/duointeractive/sea-cucumber/). It was more
appropriate to fork the project, rather than tack something on to
django-ses, as what we wanted to do did not mesh well with what was
already there.

An additional perk is that combining Sea Cucumber with django-celery’s
handy admin views for monitoring tasks lets us have peace of mind that
everything is working as it should.

Requirements
------------

* boto 2.04b+
* Django 1.2 and up, but we won’t turn down patches for restoring
  compatibility with earlier versions.
* Python 2.5+
* celery 2.x and django-celery 2.x

Using Sea Cucumber
------------------

* You may install Sea Cucumber via pip: **pip install seacucumber**
* You’ll also probably want to make sure you have the latest boto:
  **pip install —upgrade boto**
* Register for [SES](http://aws.amazon.com/ses/).
* Look at the Sea Cucumber [README](https://github.com/duointeractive/sea-cucumber/blob/master/README.rst).
* Profit.

Getting help
------------

If you run into any issues, have questions, or would like to offer
suggestions or ideas, you are encouraged to drop issues on our [issue
tracker](https://github.com/duointeractive/sea-cucumber/issues). We also haunt the #duo room on FreeNode on week days.

Credit where it’s due
---------------------

[Harry Marr](http://hmarr.com/) put a ton of work into boto’s new [SES backend](https://github.com/boto/boto/blob/master/boto/ses/connection.py), within a
day of Amazon releasing this service. He then went on to write
[django-ses](https://github.com/hmarr/django-ses). We are extremely thankful for all of his hard work, and
thank him for cranking out a good chunk of code that Sea Cucumber still uses.
