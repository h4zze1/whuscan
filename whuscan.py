#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time
import check
import banner
import argparse
from urlparse import *

def main():
	banner.showBanner()

	# GET all parameter start !
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help = "Input the URL you want to scan here", action = "store", required = True)
	parser.add_argument("-a", "--all", help = "Exacute all scan steps including sql, xss, hash test", action = "store_true", default = False)
	parser.add_argument("-s", "--sql", help = "Crawl your website and check sql injection vulunbility", action = "store_true", default = False)
	parser.add_argument("-x", "--xss", help = "Crawl your website and check xss vulunbility", action = "store_true", default = False)
	parser.add_argument("-hc", "--hashcheck", help = "Crawl your website and check if your website hase been tampered", action = "store_true", default = False)
	parser.add_argument("-rt", "--roundtime", help = "Input the time between 2 rounds of the scan. If it is empty, the script will be exacuted 1 time", action = "store", type = int, default = 0)
	args = parser.parse_args()

	test_url = args.url
	count = 1
	for i in xrange(1,9999):
		print "\n[*]Starting", str(count), "times checking..."
		# Connection test start
		domin = urlparse(test_url)
		log_path = './log/target/' + domin.path 
		if (os.path.exists(log_path)):		# Has connected before _*_
			print "Folder Exist! Writing log..."
		else:		# First time to connect _*_
			if (check.checkConn(test_url) == 1): 
				print "\n[Info]Connection Success!"
				os.makedirs(log_path)
			else:
				print "\n[Info]Connection Fail."
				exit()
		# Connection test end

		if (args.all or args.sql):
			print "[*]Sqli testing! =>" + test_url

		if (args.all or args.xss):
			print "[*]xss testing! =>" + test_url

		if (args.all or args.hashcheck):
			print "[*]hashcheck testing! =>" + test_url

		if (args.roundtime != 0):
			count = count + 1
			for j in xrange(0, int(args.roundtime)):
				print '\r' + str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))) + " | Next round will start in " + str(args.roundtime - j) + " seconds",
				sys.stdout.flush()
				time.sleep(1)
			print "\r                                                                                    \n"

		else:
			exit()


if __name__ == "__main__":
	main()