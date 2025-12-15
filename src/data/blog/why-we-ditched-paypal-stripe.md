---
author: Greg Taylor
pubDatetime: 2011-12-08T22:03:00+00:00
modDatetime:
title: Why we ditched PayPal for Stripe
slug: why-we-ditched-paypal-stripe
featured: false
draft: false
tags: ["Python", "Cloud", "Programming"]
description: ""
---

A recent backwards-incompatible change to the PayPal Adaptive API led toour web application being unable to accept new users for about five days
a while back. We were getting a very vague “Session has expired” error,
and PayPal support couldn’t figure out what was wrong. Nothing in that
section of the codebase had changed for months, the breakage randomly started.

It ended up being that a recent PayPal API update had made a previously
optional field required, and they only updated their PDF documentation
(I use their HTML docs). There was no communication of the change in
requirements leading up to the breakage, and we were alerted to the
issue by frustrated customers calling support (instead of PayPal).

This was the second such breakage during our year or so of using
PayPal’s Adaptive API. Granted, we use some of their more advanced split
payments and invoicing features, this should not happen. Additionally,
we weren’t happy with the user experience during checkout, which featured:

* Re-directing users to PayPal. User enters credit card details or logs
  into their PayPal account.
* User confirms they want to allow us to bill them.
* User is re-directed to our site, where we again confirm their selection.
* User gets what they paid for (an enrollment in a course).

A combination of being unhappy with customer support and the disruption
of our checkout process with redirects led to us searching for alternatives.

The search begins
-----------------

Initially, we looked at other similar (but more simple) services.
[WePay](https://www.wepay.com/) was at the top of our list. This is a young but promising
service that makes collecting payments much easier than PayPal. They
have a [Python API](https://github.com/wepay/Python-SDK) (that we contributed some to), and good
documentation. However, they still needed us to redirect our customer to
WePay’s site, which ultimately led to their being scratched from the list.

We investigated some traditional payment processors like Braintree and
Authorize.net, and while they looked like great services, we needed our
customers (schools and businesses) to be able to get set up to receive
payments quickly. A lot of traditional gateways have long, complicated
setup processes, often involving sales calls and working with banks.
Each of our customers would have had to go through this process, which
would have presented a huge barrier in the setup process. They also
typically require you to send credit card data through your servers,
which means obtaining a level of PCI Compliance (not that we aren’t
already security-conscious).

Another service we had heard great things about was [Stripe](https://stripe.com/). Like
WePay, Stripe is a relatively new service, but has backing from former
PayPal execs, along with some other great names. Diving in to figure out
what the excitement about, we weren’t disappointed.

Stripe gets it right
--------------------

The refreshing thing about Stripe is that they weren’t afraid to break
convention. Instead of redirecting customers to Stripe, or sending their
credit card data to their servers from ours (which you can still do if
you want), they wrote a nifty bit of javascript called [stripe.js](https://stripe.com/docs/stripe.js).
This little guy sends credit card data from a form on your site directly
to Stripe’s servers (over SSL), which returns a unique token for that
credit card. Said token is then submitted to your server via
GET/POST/whatever, and your server uses the token instead of the user’s
credit card number.

No redirects are necessary, we avoid having to hassle with monetary and
time expense of PCI compliance, and the checkout experience is seamless
for our user. We condensed everything down to one click of a button,
staying 100% on our branded site.

Top-top notch customer support
------------------------------

The other thing that really shocked us after dealing with PayPal is
Stripe’s customer support. We navigated to their [support page](https://stripe.com/help/contact) to see
where we could ask some questions early in the process. Imagine our
shock when we saw a [Campfire chatroom](https://stripe.com/campfire) linked there. I cautiously
entered the room, not sure what to expect. As the room loaded and I
listened in on conversations, I realized that this chatroom has the
Stripe developers in it, as well as the business-oriented staff.

Encouraged, I started my deluge of questions to determine whether Stripe
would be an option for us. The Stripe staff answered everything
consistently, thoroughly, and quickly. I stopped by a good number of
times during the two weeks we were researching alternatives, and they
were patient every time.

Let’s contrast this to our PayPal setup process during our early development:

* Jump back and forth between some really convoluted, duplicated
  content across the then new x.com and their old developer doc CMS.
* Guess which form to fill out. Send it in.
* Get to work using their simple NVP API. Learn that what we were doing
  required the use of a completely different service.
* Fill out more forms, switch to Web Payments Pro. Learn that this too
  isn’t what we needed.
* Switch to the Adaptive Payments API. This particular API was actually
  pretty easy to work with, though a lot more complicated than Stripe’s.

And then our more recent complete service outage:

* Enter a ticket in PayPal explaining that our customers weren’t able
  to checkout, and were seeing a very unhelpful error message.
* Get a really vague, un-helpful answer back from someone we can’t
  actively engage with.
* Get our ticket passed from person to person, having to explain things
  over again.
* Having days go by until our issue gets passed to an engineer capable
  of diagnosing our issue.

PayPal’s mindshare and feature list are huge, but support is such a
critical consideration. If we had been in anything but our current
closed beta state, this would have been a major catastrophe.

Stripe, now with more Python
----------------------------

Another handy tidbit is that Stripe does have an officially maintained
and supported Python library, [stripe-python](https://github.com/stripe/stripe-python). You can talk to the same
developers who maintain this in the aforementiponed [Campfire
chatroom](https://stripe.com/campfire), as well.

Bashing PayPal is becoming the stylish thing to do, but…
--------------------------------------------------------

*I’m going to get on my podium here for a second, so feel free to
navigate somewhere else if this kind of thing bothers you.*

A year ago, I usually brushed most harsh criticism of PayPal off. They
had been good enough for my personal and professional use. We didn’t
really have any reason to deal with their support before our current
project, so it was a nice, cozy, detached relationship.

Dealing with their signup process, and later having to deal with their
awful support during a service interruption soured me to them quite a
bit. Hearing about how they have increasingly taken to [freezing](http://www.regretsy.com/2011/12/05/cats-1-kids-0/)
[accounts](http://www.escapistmagazine.com/news/view/103385-PayPal-Freezes-750K-in-MineCraft-Devs-Account) for [silly](http://blog.diasporafoundation.org/2011/10/19/how-diaspora-found-its-tiger-stripe-in-the-midst-of-a-paypal-fiasco.html) reasons has made the negative light I view them
in even more intense.

Do consider alternatives before taking your business to this bloated,
slow, and unsupportive behemoth. The small guys are going to want your
business more, and do more to keep it. Few can go toe-to-toe with PayPal
on a per-feature basis, but rarely do you use even the majority of the
feature set.
