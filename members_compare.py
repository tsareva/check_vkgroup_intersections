#!/usr/bin/env python
# -*- coding: utf-8 -*-

#VK API can't correctly work with short names like "club7777"
#So we need to check for it and correct if it is needed
def get_group_id(vk_club):
    if vk_club.find('club') != -1:
        group_id = vk_club[4:]
    elif vk_club.find('event') != -1:
        group_id = vk_club[5:]
    elif vk_club.find('public') != -1:
        group_id = vk_club[6:]
    else:
        group_id = vk_club
    try:
        int(group_id)
    except: 
        group_id = vk_club
    return group_id

#check for vk_api lib
from pip import main, get_installed_distributions
installed_packages = get_installed_distributions()
flat_installed_packages = [package.project_name for package in installed_packages]
if 'vk_api' in flat_installed_packages: 
	pass
else: 
	print("vk_api module is needed. Trying to install...")
	main(["install", 'vk_api'])

import vk_api

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

login = input("login: ") 
password = input("password: ")
vk_session = vk_api.VkApi(
		login, password,
		auth_handler=auth_handler  
	)

vk_session.auth()	
	
tools = vk_api.VkTools(vk_session)
vk = vk_session.get_api()

id1 = get_group_id(input('Enter first group id: '))
id2 = get_group_id(input('Enter second group id: '))

members1 = tools.get_all('groups.getMembers', 1000, {'group_id': id1})["items"]
members2 = tools.get_all('groups.getMembers', 1000, {'group_id': id2})["items"]

intersection = len(set(members1).intersection(members2))

print("There are %s common users" % intersection)

if intersection > 0:
	print("It is %s percent for group with %s id" % (round(intersection*100/len(members1), 1), id1))
	print("It is %s percent for group with %s id" % (round(intersection*100/len(members2), 1), id2))
	
input("Press enter to quit")