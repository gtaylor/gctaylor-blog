---
author: Greg Taylor
pubDatetime: 2013-02-11T22:52:00+00:00
modDatetime:
title: Fabric task for notifying New Relic of a code deploy
slug: fabric-task-for-notifying-new-relic-code-deploy
featured: false
draft: false
tags: ["Python", "Programming", "DevOps"]
description: ""
---

We’ve been doing some playing around with [New Relic](https://newrelic.com/) lately at [Pathwright](http://www.pathwright.com).One of the neat things it does is track when code deploys happen, and how
they affect responsiveness and resource consumption.

In order to notify New Relic when a deploy happens, you simply POST to their
web-based API with the information you’d like to include (change logs, commit
hashes, etc).

We currently do this via a Fabric task, which I figured I’d share. We tend
to run this from our deploy task. Enjoy!

```
import socket
import requests
from fabric.api import run, cd

def notify_newrelic_of_deploy(old_commit_hash):
    """
    New Relic tracks deploy events. Send a notification via their HTTP API.

    :param str old_commit_hash: The previously deployed git hash. This is
        easily retrieved on a remote machine by running 'git rev-parse HEAD'.
    """

    with cd(env.REMOTE_CODEBASE_PATH):
        new_commit_hash = run('git rev-parse HEAD')
        changes = run('git --no-pager log %s..HEAD' % old_commit_hash)

    headers = {
        # Adjust this to reflect your API key.
        'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    }
    payload = {
        'deployment[app_name]': 'Your App Name',
        # This is also very important to update with your own value.
        'application_id': '1234567',
        'deployment[description]': 'Fabric deploy is fun deploy',
        'deployment[revision]': new_commit_hash,
        'deployment[changelog]': changes,
        'deployment[user]': '%s@%s' % (LOCAL_USERNAME, socket.gethostname()),
    }

    requests.post("https://rpm.newrelic.com/deployments.xml",
                  data=payload, headers=headers)
```
