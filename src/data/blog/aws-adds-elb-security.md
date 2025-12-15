---
author: Greg Taylor
pubDatetime: 2011-05-25T14:00:00+00:00
modDatetime:
title: AWS Adds ELB Security
slug: aws-adds-elb-security
featured: false
draft: false
tags: ["Cloud"]
description: ""
---

As of May 24, Amazon Web Services added the ability to [add Elastic LoadBalancers (ELB) to security group rules](http://aws.typepad.com/aws/2011/05/elastic-load-balancing-ipv6-zone-apex-support-additional-security.html). This will allow you to get
more specific with services that are load balanced in your security
groups, instead of having to add a rule accepting inbound traffic from
everyone (0.0.0.0/0). While this is a big step, ELBs themselves do not
use security groups to determine who can access whatever port they’re
forwarding, so if someone knows the public IP of the ELB, they can still
reach the underlying ports on the EC2 instances being load balances.

But this is a good step, we look forward to seeing more development.

Source: [Amazon Web Services Blog](http://aws.typepad.com/aws/2011/05/elastic-load-balancing-ipv6-zone-apex-support-additional-security.html)
