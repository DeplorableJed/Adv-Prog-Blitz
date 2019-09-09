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

    # ask user to input an email for a Webex Teams user
    new_membership = input('\nEnter an email for a Webex Teams user to invite to the space: ')

    # invite user to join the space
    webex_teams_apis.add_space_membership(new_space_name, new_membership)
    input('Check the space for the new membership, hit any key to continue ')

    # ask user to input the message to be posted in the space
    new_message = input('\nEnter the message to be posted in the space: ')

    # post message to the new space
    webex_teams_apis.post_space_message(new_space_name, new_message)
    input('Check the space for the new message posted, hit any key to continue ')

    # post the same message marked down
    webex_teams_apis.post_space_markdown_message(new_space_name, new_message)
    input('\nCheck the space for the marked down message posted, hit any key to continue ')

    # ask user to input an domain name, and the URL link to be posted in the space
    new_domain_name = input('\nEnter the Domain Name be posted in the space: ')
    new_url = input('Enter the URL to be associated with the Domain Name (format "http://..."): ')

    # post the new Domain Name and URL to the space
    webex_teams_apis.post_space_url_message(new_space_name, new_domain_name, new_url)
    input('Check the space for the URL posted, hit any key to continue ')

    # upload a new image file, one provided SDA_Roles.jpg
    webex_teams_apis.post_space_file(new_space_name, 'SDA_Roles.jpg', 'image/jpg', '')
    input('\nCheck the space for the image file uploaded, hit any key to continue ')
    
    # ask the user invited to post a message to the space
    input('\nAsk the user invited to the space to post a message in the space using the Mobile or Desktop Webex Teams Client \nHit any key to continue')
    
    # check for the last message posted in the space and the identity of the user
    last_message_info = webex_teams_apis.last_user_message(new_space_name)
    
    print('\nLast message posted in the space was - ', last_message_info[0], '\nLast message was posted by the user - ', last_message_info[1])

    # delete the space
    input('\n\nEnter any key to delete the space you created ')
    
    webex_teams_apis.delete_space(new_space_name)

if __name__ == '__main__':
    main()
