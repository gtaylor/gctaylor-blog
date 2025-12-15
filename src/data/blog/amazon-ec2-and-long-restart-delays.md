---
author: Greg Taylor
pubDatetime: 2011-03-23T00:00:00+00:00
modDatetime:
title: Amazon EC2 and long restart delays
slug: amazon-ec2-and-long-restart-delays
featured: false
draft: false
tags: ["Linux", "AWS"]
description: ""
---

I am not sure if this is an Ubuntu EC2 AMI issue, an EC2 issue, an EBS issue, or some
combination of all of these, but we are experiencing some really erratic
restart times. We run our EC2 instances with the following basic configuration:

* Size: small and medium high-cpu
* Root device: EBS
* Distro: Ubuntu 10.10 (the latest)

Symptoms
--------

The behavior we are seeing is that even our simplest,
no-extra-EBS-volumes instances periodically hang on boot when restarted.
The restart can range anywhere from less than 60 seconds, to 5 minutes,
to not at all. In the case of ‘not at all’, something bad happens to the
point where we the instance fails to reach the point where we can even
SSH in, and the syslog that the web-based management console shows looks
to be out of date.

In the case of a complete hang on restart (it seems to be 50-50 right
now), we have to reboot the machine again from the web-based AWS EC2
management console. This second reboot usually results in a full startup.

Our hunch
---------

From what we can tell, this *may* be EBS-related. Even though we
specifically have *nobootwait* on our swap partition (which is an
included ephemeral drive that is standard with the Ubuntu AMI), it seems
like Ubuntu may be freaking out when it can’t reach the root EBS drive.
It’s also possible that even despite the *nobootwait* in the fstab,
this same thing could be happening with the swap partition as well. We
haven’t had a lot of time to try different combinations, as we’re
insanely busy right now.

If anyone else has experienced something similar, please chime in.
