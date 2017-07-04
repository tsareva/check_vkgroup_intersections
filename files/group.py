#!/usr/bin/envquit() python
# -*- coding: utf-8 -*-
import sys, socket, ssl
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs, csv, sqlite3, urllib, vkontakte, time
from create_token import create_token


token = open("files/token.txt").read()
vk = vkontakte.API(token=token)

def get_info(group_id):
	x = 1
	while True:
		try:
			print "Getting data for group ", group_id
			fields='members_count,description,contacts,links'
			all_group_info = vk.groups.getById(group_ids=group_id, fields=fields)
			all_group_info = all_group_info[0]
			count = all_group_info.get(u'members_count', None)
			return count
		except (socket.gaierror, socket.timeout, ssl.SSLError):
			print "Can't create connection for %s time. Trying again..." % x
			time.sleep(1)
			x+=1
			continue
		except vkontakte.api.VKError as error:
			if error.code == 5:
				create_token()
				quit()
			elif error.code == 100:
				count = None 
				return count
			else:
				print error
				quit()
			
def get_members_ids(group_id, count):
	offset = 0
	id_list = []
	while (count > len(id_list)):
		try:
			list = vk.groups.getMembers(group_id=group_id, offset=offset)
			id_list += list[u'users']
			print "Getting member list: %s of %s done" % (len(id_list), count)
			offset += 1000
			time.sleep(0.2)
		except:
			time.sleep(0.2)
			continue
	return id_list
	

