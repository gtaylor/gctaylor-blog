---
author: Greg Taylor
pubDatetime: 2015-07-22T12:13:00+00:00
modDatetime:
title: Enabling Cassandra logback debugging
slug: enabling-cassandra-logback-debugging
featured: false
draft: false
tags: ["Cassandra"]
description: ""
---

In our pursuit for 100% centralized logging, I found myself recently settingup [logback-gelf](https://github.com/Moocar/logback-gelf) with Cassandra working. The intention was to point Cassandra’s logback config at our [graylog2](https://www.graylog.org/) install, but I had a mis-step somewhere during setup.

After beating my head against a wall for a while, I got in touch with DataStax support to see if they could advise me how to enable logback debugging in Cassandra. They obliged, I quickly found an error message pointing me in the right direction, and we are today happily using logback+GELF with our Cassandra install.

For anyone else wishing to enable logback debug mode, add the following line to your /etc/dse/cassandra/cassandra-env.sh:

After that, debug output can be found in /var/log/cassandra/output.log.
