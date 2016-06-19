#!/usr/bin/env python
# coding=utf-8
import sys
import time
import requests


# Connection test begin !!
def checkConn(test_url):
    if test_url[:4] != "http":
        test_url = "http://" + test_url
    headersme = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    print "\n[*]Stability Test\n"
    print "[*]Connecting...\n"

    total_count = 0  # Initial count number
    success_count = 0

    # Try 5 times and if more than 3 times is connective, stable!
    for i in range(1, 6):
        try:
            req = requests.get(url=test_url, headers=headersme, timeout=3)
            if req.status_code == 200:
                success_count = success_count + 1
                total_count = total_count + 1
        except:
            total_count = total_count + 1
        for ti in range((total_count - 1) * 20, total_count * 20):
            time.sleep(0.02)
            print "\r********************* ", ti, "% *********************\r",
            sys.stdout.flush()

    if success_count > 2:
        print "\r********************* 100 % *********************"
        print "\n[*]The url you are requesting is STABLE"
        return 1
    else:
        return 0

# Connection test end !!
