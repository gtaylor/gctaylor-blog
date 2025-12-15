---
author: Greg Taylor
pubDatetime: 2012-04-03T16:29:00+00:00
modDatetime:
title: Pathwright launches, powered by Snakes and Jazz
slug: pathwright-launches-powered-snakes-and-jazz
featured: false
draft: false
tags: ["Python", "Cloud", "Django", "Programming"]
description: ""
---

After over two years of development, [Pathwright](http://www.pathwright.com/) has emerged frombeta, and is open to the masses. For those with knowledge to share, we
hope this web application will give you an easy-to-use, easy-on-the-eyes
way to teach others. We provide a structured, social way for your
students to learn.

See the [Pathwright](http://www.pathwright.com/) landing page for more details, as I’m going to
leave marketing mode and get into the more philosophical and technical
topics that most of you will probably be more interested in.

What’s special about Pathwright?
--------------------------------

There is no longer a shortage of online learning software to choose
from. Players ranging from “free” to expensive exist, with wildly
varying approaches and feature lists. We chose a very specific set of
core principles to develop against:

* Online learning should be easy for both teachers and students.
* The software should be visually appealing and polished.
* Do less than the competition, but do it better.
* Prices are posted upfront, no sales calls or interaction with us is
  required to get started. We’re eager to talk to anyone who’d like to
  get in touch, but some of our competitors strong arm you into sales
  calls before you can even see the software, which we are loath to do.
* It should be easy and affordable for organizations of all sizes to
  sign up, try the software free of charge, then elect to start selling
  courses as soon as they’d like.

We are a hosted solution that handles all of the unpleasant stuff for
you (servers, billing, scaling, continuous software upgrades, support)
for you. Our hope is that our customers can spend their time creating
content and interacting with their students, instead of dealing with
infrastructure or dialing IT.

A peek under the hood
---------------------

Pathwright is powered by the [Python](http://python.org/) and [Django](https://www.djangoproject.com/). The two were
chosen for their ease of use, and being good enough to accomodate our
fast-paced development process. Almost any modern, widely used framework
would have done the trick, our team was just very comfortable with this
particular stack.

All of our servers are on Amazon Web Services. We’ve found the pricing
to be great, and the ability to effectively “outsource” portions of our
stack has freed up a lot of development time. We run no media servers
([S3](http://aws.amazon.com/s3/) + [CloudFront](http://aws.amazon.com/cloudfront/)), no mail servers ([SES](http://aws.amazon.com/ses/)), no self-hosted load
balancers ([ELB](http://aws.amazon.com/elasticloadbalancing/)), and have drastically simplified a number of other
things with AWS’s services.

A few really critical parts of our stack:

* [nginx](http://nginx.org/) (front-facing proxy)
* [postgres](http://www.postgresql.org/)
* [memcached](http://memcached.org/)
* [RabbitMQ](http://www.rabbitmq.com/) (broker for celery)
* [Sentry](https://www.getsentry.com/welcome/) (a real life-saver)
* [Stripe](https://stripe.com/) (payments and billing)

Some crucial Python packages:

* [django](https://www.djangoproject.com/)
* [gunicorn](http://gunicorn.org/) (app server)
* [celery](http://celeryproject.org/) (background task processing)
* [boto](http://boto.cloudhackers.com/) (does it all. super important)
* [seacucumber](https://github.com/duointeractive/sea-cucumber) (SES mail with celery)
* [django-mediasync](https://github.com/sunlightlabs/django-mediasync) (combines/minifies/syncs static assets to S3)
* [django-athumb](https://github.com/duointeractive/django-athumb) (thumbnails images to S3 efficiently)
* [Fabric](http://docs.fabfile.org/) (deployment)
* [media-nommer](http://media-nommer.readthedocs.org/) (encodes our customer’s videos)

Tell us what you think!
-----------------------

We’ve worked long and hard on Pathwright, bootstrapping it from nothing.
At this point, we’re what you could say “too close” to the project to
get all the feedback we need from our team. Please let us know what you
think in the comments or via [email](mailto:support@pathwright.com).
