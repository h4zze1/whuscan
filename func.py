#!/usr/bin/env python
#coding=utf-8

import hashlib

# Function md5()
def md5(mess):
	m2 = hashlib.md5()   
	m2.update(mess)   
	return m2.hexdigest()