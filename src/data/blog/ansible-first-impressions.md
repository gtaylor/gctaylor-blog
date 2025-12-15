---
author: Greg Taylor
pubDatetime: 2013-02-08T06:22:00+00:00
modDatetime:
title: Ansible first impressions
slug: ansible-first-impressions
featured: false
draft: false
tags: ["Python", "Programming", "DevOps"]
description: ""
---

After brief visits with [Puppet](https://puppetlabs.com/) and [Chef](http://www.opscode.com/chef/) for config management,I’ve set my sights on [Ansible](http://ansible.cc/). It’s late and I’ve been staring at
this stuff for way too long today, but here are some early observations:

* I really like that it is written in Python. Puppet and Chef are great
  pieces of software, but I spend my days staring at Python. It’s nice
  not having to context switch away.
* The [documentation](http://ansible.cc/docs/), while organized somewhat weirdly, is
  surprisingly thorough and helpful. I found myself much less
  frustrated and overwhelmed in comparison to my forays into Puppet and Chef.
* It’s just SSH.
* The playbook organization and format make a lot of sense to me. It
  feels a whole lot less complex than Chef in particular.

As far as negatives:

* The documentation is very good but it could use some organizational
  tweaking. The related links at the bottom of some of the pages are
  very erratic and sometimes incomplete.
* If you’re wanting to use Ansible as a Python API, the [docs](http://ansible.cc/docs/api.html) for
  this are pretty incomplete.

So far, Ansible looks very promising. I think this is going to be a
great fit for us at [Pathwright](http://www.pathwright.com). Perhaps we’ll even have some time
to contribute improved docs.
