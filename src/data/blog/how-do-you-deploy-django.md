---
author: Greg Taylor
pubDatetime: 2011-03-28T05:17:00+00:00
modDatetime:
title: How do YOU deploy Django?
slug: how-do-you-deploy-django
featured: false
draft: false
tags: ["Python", "Programming", "Django"]
description: ""
---

There are a good number of choices for deploying Django projects,whether they be [Fabric](http://docs.fabfile.org/), [Chef](http://wiki.opscode.com/display/chef/Home), [Puppet](http://www.puppetlabs.com/), [Paver](http://paver.github.com/paver/), or something
else. However, each may be more suitable for some types of deployments
than others. For example, Fabric’s lack of parallel execution may leave
you frustrated if you have many dozens of hosts to deploy to, and Chef’s
complexity and [scattered documentation](http://wiki.opscode.com/display/chef/Home) may be somewhat discouraging,
as powerful as it seems.

Show and Tell
-------------

We ([DUO Interactive](http://duointeractive.com/)) have been using Fabric for our deployments.
We’ve got a few projects in development and maintenance, most of which
are single app server situations (which Fabric is awesome for). To keep
our deployments consistent across our various projects, we wrote a
smattering of management commands and Fabric methods, and tossed it up
on GitHub as [django-fabtastic](https://github.com/duointeractive/django-fabtastic). There is no real documentation aside
from comments, but we figured we’d share what has worked for our simple deployments.

We’ve been extremely happy with Fabric and fabtastic for our simple
deployments, but a new project looks to be moving towards the more
complex end of the deployment spectrum in the future. We’re looking at
the possibility of at least five app servers by year’s end, and are
frustrated with our Fabric-based deployment (with a handful of app
servers) for a few reasons:

* It can be pretty slow with a good number of app servers.
* Hosts are deployed to one at a time, with no abiiity to execute
  deployments in parallel.
* We sit our EC2 app servers behind one of AWS’s Elastic Load
  Balancers. At any given time during deployment, users might get an
  updated app server, or one that has not been deployed to yet. This
  inconsistency is troubling. We’d still get this even with parallel
  execution (as it stands right now), but it would *possibly* be less
  of a problem.

In an Ideal World
-----------------

I personally would love to see a deployment system that could do the following:

1. Fire off an individual deployment step to a large number of nodes at
   a time (in parallel, not one at a time).
2. Have the ability to wait until all nodes have completed certain steps
   before progressing onwards with the deployment. For example, wait
   until all nodes have checked out the latest version of the source
   before restarting the app servers. There would obviously still be a
   small period in time where not all nodes have reloaded the code, but
   it would potentially be a lot better than what we’re seeing right now.

What do YOU do?
---------------

So I ask the readers: What tools do you use to deploy your projects
with, and how many Django app servers do you deploy to? What works well
for you with your deployment strategy, and what irritations do you face?
