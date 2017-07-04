#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('files/')
from group import *
from create_token import *
import time, vkontakte

try:
	get_server_time()
except vkontakte.api.VKError as error:
	if error.code == 5:
		create_token()
		get_server_time()
		quit()
	else:
		print error
		quit()

id1 = raw_input('Enter first group id: ') 
id2 = raw_input('Enter second group id: ') 

count1 = get_info(id1)
count2 = get_info(id2)

members1 = get_members_ids(id1, count1)
members2 = get_members_ids(id2, count2)

intersection = len(set(members1).intersection(members2))

print "There are %s common users" % intersection
print "It is %s percent for group with %s id" % ((intersection*100/count1), id1)
print "It is %s percent for group with %s id" % ((intersection*100/count2), id2)