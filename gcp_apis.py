#!/usr/bin/env python3


# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems


import requests
import urllib3
import json
import google_cloud_platform


from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

from config import GCP_API_KEY_COMPUTE, GCP_PROJECT


urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def create_networks():
    """

    :return:
    """
    url = 'https://www.googleapis.com/compute/v1/projects/' + GCP_PROJECT + '/global/networks' + '?key=' + GCP_API_KEY_COMPUTE
    print(url)
    payload = {
        "routingConfig": {
            "routingMode": "REGIONAL"
        },
        "name": "outside-vpc",
        "description": "csr outside network",
        "autoCreateSubnetworks": "false"
    }
    response = requests.post(url, data=json.dumps(payload))
    print(response.status_code)
    print(response.text)


def create_subnetworks():
    url = 'https://www.googleapis.com/compute/v1/projects/' + GCP_PROJECT + '/regions/us-west2/subnetworks' + '?key=' + GCP_API_KEY_COMPUTE
    print(url)
    header = {'content-type': 'application/json'}
    payload = {
        "privateIpGoogleAccess": False,
        "enableFlowLogs": False,
        "name": "outside",
        "ipCidrRange": "172.16.1.0/24",
        "network": "https://clients6.google.com/compute/v1/projects/" + GCP_PROJECT + "/global/networks/outside-vpc"
    }
    response = requests.post(url, data=payload, headers=header)
    print(response.status_code)


create_networks()
create_subnetworks()
