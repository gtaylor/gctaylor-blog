---
author: Greg Taylor
pubDatetime: 2021-09-21T04:11:06+00:00
modDatetime:
title: Unifi dynamic DNS with Google Domains
slug: unifi-dynamic-dns-with-google-domains
featured: false
draft: false
tags: []
description: ""
---

To configure your Unifi Controller/UDM as a dynamic DNS client for Google Domains:

1. Read the [Google Domains Dynamic DNS](https://support.google.com/domains/answer/6147083?hl=en) article.
2. Open your Unifi Controller/UDM’s web interface.
3. In the search bar, search for “Dyn” and click on the “Add New Dynamic DNS” link.
4. Enter the following:

   1. **Interface**: <your WAN interface here>
   2. **Service**: dyndns
   3. **Hostname**: <the FQDN to send dynamic DNS updates for>
   4. **Username**: <the auto-generated username from Google Domains>
   5. **Password**: <the auto-generated password from Google Domains>
5. Click “Apply Changes”. The update typically fires off and is visible in Google Domains within a minute or two.
