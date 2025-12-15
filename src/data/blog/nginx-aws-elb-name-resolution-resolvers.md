---
author: Greg Taylor
pubDatetime: 2011-11-10T00:12:00+00:00
modDatetime:
title: nginx AWS ELB name resolution with resolvers
slug: nginx-aws-elb-name-resolution-resolvers
featured: false
draft: false
tags: ["Linux", "Cloud"]
description: ""
---

If you are running nginx as a proxy in front of An Amazon Web Services[Elastic Load Balancer (ELB)](http://aws.amazon.com/elasticloadbalancing/), it is not safe to merely define an
upstream using the hostname of ELB and call it a day. By default, nginx
will only do name resolution at startup time, caching the resolved IP
address infinitely.

ELB instances scale up and down based on your traffic levels, often
changing IP addresses in the process. It seems to be that increased
traffic leads to Amazon spawning a new, beefier ELB instance, then
changing the DNS record to point at the new instance. It’ll keep the old
ELB instance around for a little while to give you time to resolve the
new one, but the old instance (using the old IP) will be retired after a
short period of time. We need nginx to be able to periodically
re-resolve the load balancer’s hostname so service interruptions aren’t
encountered due to the IP address change.

The fix
-------

Fortuantely, this one is really simple to remedy. You need only use the
[resolver](http://wiki.nginx.org/HttpCoreModule#resolver) config directive in your nginx config. By specifying a DNS
server with the **resolver** directive from within nginx, you signify
that it should check with said server every five minutes (by default) to
see if the upstream ELB has changed IPs. This is done in a non-blocking
manner, and should pose no real threat to your server’s throughput.

The other critical piece is that you must add a **$request\_uri** to the
end of whatever **proxy\_pass** value you’ve specified. DNS caching will
remain without this, meaning you are no better off. See the example below.

Example
-------

```
http {
   [...]

   # Causes DNS resolution of upstreams every 5 minutes.
   resolver 172.16.0.23;

   [...]

   server {
      [...]

      proxy_pass http://somewhere.com$request_uri

      [...]
   }
}
```

The resolver directive can be used in http, server, and location
sections, so you can get as specific or as broad as you’d like.

The future fix
--------------

A later version of nginx will honor DNS TTLs, so look forward to that.
I’ll try to remember to update this article when this lands.
