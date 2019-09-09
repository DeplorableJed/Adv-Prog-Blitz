#!/usr/bin/env python3

# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems

# import Python packages
import urllib3
import requests
import json
import sys
sys.path.append('..')
                

# import functions modules
import webex_teams_apis

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth
from config import WEBEX_TEAMS_URL, WEBEX_TEAMS_AUTH

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def main():

    # ask user to input a name for a new space
    new_space_name = input('Enter a name for the Webex Teams Space: ')

    # create a new space
    space_id = webex_teams_apis.create_space(new_space_name)
    print('The new space created has the Webex Teams id: ', space_id)

 
if __name__ == '__main__':
    main()
