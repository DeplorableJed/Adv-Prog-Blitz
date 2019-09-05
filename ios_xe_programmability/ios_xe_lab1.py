#!/usr/bin/env python3


# developed by Gabi Zapodeanu, TSA, Global Partner Organization


import requests
import urllib3
import ncclient
import xml
import xml.dom.minidom
import json
import utils
import netconf_restconf

from ncclient import manager

from urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth  # for Basic Auth
from config import IOS_XE_HOST, IOS_XE_PORT, IOS_XE_USER, IOS_XE_PASS

urllib3.disable_warnings(InsecureRequestWarning)  # Disable insecure https warnings



#
# example of how to use NETCONF anD RESTCONF to access ISO XE devices operational data
#

# IOS XE device hostname using NETCONF


hostname_netconf = netconf_restconf.get_netconf_hostname(IOS_XE_HOST, IOS_XE_PORT, IOS_XE_USER, IOS_XE_PASS)
print('\nThe IOS XE device hostname using NETCONF is: ', hostname_netconf)


# IOS XE device hostname using RESTCONF

hostname_restconf = netconf_restconf.get_restconf_hostname(IOS_XE_HOST, IOS_XE_USER, IOS_XE_PASS)
print('\nThe IOS XE device hostname using RESTCONF is: ', hostname_restconf)


# interface name to be used for NETCONF and RESTCONF API calls
interface = 'GigabitEthernet0/0'

print('\nThis script will get the interface ' + interface + ' operational data using NETCONF and RESTCONF')
input('Enter any key to continue with NETCONF ')


# get the operational data for the interface using NETCONF

int_oper_data_xml = netconf_restconf.get_netconf_int_oper_data(interface, IOS_XE_HOST, IOS_XE_PORT, IOS_XE_USER, IOS_XE_PASS)
# pretty print xml data
print(int_oper_data_xml.toprettyxml())

input('Enter any key to continue with RESTCONF ')


# get the operational data for the interface using RESTCONF

int_oper_data_json = netconf_restconf.get_restconf_int_oper_data(interface, IOS_XE_HOST, IOS_XE_USER, IOS_XE_PASS)
utils.pprint(int_oper_data_json)
