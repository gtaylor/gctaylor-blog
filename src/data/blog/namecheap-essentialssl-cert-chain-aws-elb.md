---
author: Greg Taylor
pubDatetime: 2013-03-29T13:30:00+00:00
modDatetime:
title: namecheap.com EssentialSSL and Amazon ELB
slug: namecheap-essentialssl-cert-chain-aws-elb
featured: false
draft: false
tags: ["Cloud"]
description: ""
---

For those using the SSL capabilities of Amazon Elastic Load Balancer (ELB),you often need to upload a *Certificate Chain* to avoid SSL errors in some browsers.

We use [Namecheap](http://www.namecheap.com/) and their Comodo [EssentialSSL](http://www.namecheap.com/ssl-certificates/comodo.aspx) wildcard certs. If you
specify “Other” as your server type, you’ll get a collection of files
that comprise the Certificate Chain/CA Bundle, instead of a single file
(like you’d get if you specified Apache during the CSR submission process).
If you haven’t purchased your cert yet, save yourself some trouble and
just say you’re using Apache. If you specified “Other” or have found yourself
with a bunch of \*.crt files, read on.

I am going to assume that you are using OpenSSL. I am also going to assume
that you have the same files I do. If this isn’t the case, you could try
downloading their [CA Bundle](https://support.comodo.com/index.php?_m=downloads&_a=viewdownload&downloaditemid=66&nav=0,1,20), but this may or may not work (or be up to date).

```
cat EssentialSSLCA_2.crt ComodoUTNSGCCA.crt UTNAddTrustSGCCA.crt 
    AddTrustExternalCARoot.crt > ca-chain.crt
```

This is all you need to paste into the “Certificate Chain” field in the
SSL Cert selection dialog on the AWS Management Console.

While you’re here, have another tip: If the dialog complains about an
invalid Private Key or Public Key Certificate, you probably need to PEM
encode it. My key was RSA, so this is what PEM-encoding looked like for me:

```
openssl rsa -in mycert.com.key -out mycert.com.pem
```

This is then safe to paste into the “Private key” field. If for whatever
reason your \*.crt file came back in another format, you could also use this
same set of steps to encode it (though, my was sent to me PEM encoded already).
