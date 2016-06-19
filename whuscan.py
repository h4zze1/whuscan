#!/usr/bin/env python
# coding=utf-8

import os
import sys
import time
import check
import func
import spyder
import banner
import argparse

from urlparse import *

url = ''
domin = ''
scheme = ''

def main():
    global url
    global domin
    global scheme

    banner.showBanner()

    # ----------------------------------------- GET all parameter START !----------------
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Input the URL you want to whuscan here",
                        action="store", required=True)
    parser.add_argument("-a", "--all", help="Exacute all whuscan steps including sql, xss, hash test",
                        action="store_true", default=False)
    parser.add_argument("-s", "--sql", help="Crawl your website and check sql injection vulunbility",
                        action="store_true", default=False)
    parser.add_argument("-hc", "--hashcheck", help="Crawl your website and check if your website hase been tampered",
                        action="store_true", default=False)
    parser.add_argument("-rt", "--roundtime", help="Input the time between 2 rounds of the whuscan. If it is empty, the script will be exacuted 1 time",
                        action="store", type=int, default=0)
    args = parser.parse_args()

    # ----------------------------------------- GET all parameter END !-------------------

    count = 1

    # ----------------------------------------- GET URL & domin START !-------------------

    scheme = func.urlFilter(args.url)[0]
    domin = func.urlFilter(args.url)[1]
    url = scheme + '://' + domin
    print '[*]Scanning ', url
    # ----------------------------------------- GET URL & domin END !-------------------


    for i in xrange(1, 9999):
        print "\n[~]Writing log..."
        print "[*]Starting", str(count), "times checking..."
        # Connection test start
        log_path = './log/target/' + domin + '/'
        if os.path.exists(log_path):    # Has connected before
            pass
        else:                           # First time to connect
            if check.checkConn(url) == 1:
                print "\n[Info]Connection Success!"
                os.makedirs(log_path)
                f = file(log_path + 'webhash.csv', "w")
                f.close()
            else:
                print "\n[Info]Connection Fail."
                exit()
        # Connection test end

        if (args.all or args.hashcheck):
            sys.stdout.flush()
            print "[*]hashcheck testing! => " + url
            spyder.hashspider(url, log_path)
            sys.stdout.flush()

        if (args.all or args.sql):
            print "\n[*]Sqli testing! => " + url
            sys.stdout.flush()
            time.sleep(5)
            print "[*]Congratulations, No SQL vulunbility!"

        if (args.roundtime != 0):
            count = count + 1
            for j in xrange(0, int(args.roundtime)):
                print '\r' + str(time.strftime("%Y-%m-%d %H:%M:%S",
                                               time.localtime(time.time()))) + " | Next round will start in " + str(
                    args.roundtime - j) + " seconds",
                sys.stdout.flush()
                time.sleep(1)
            print "\r                                                                                    \n"

        else:
            exit()


if __name__ == "__main__":
    main()
