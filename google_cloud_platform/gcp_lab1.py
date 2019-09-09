import argparse
import urllib3
import requests
import os

from oauth2client import client


from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

from config import GCP_CLIENT_ID, GCP_CLIENT_SECRET

client_secret = {
    "installed": {
        "client_id": GCP_CLIENT_ID,
        "client_secret": GCP_CLIENT_ID,
        "redirect_uris": "",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token"
    }
}





from oauth2client.client import flow_from_clientsecrets

flow = flow_from_clientsecrets('client_secrets.json',
                               scope='https://www.googleapis.com/auth/compute',
                               redirect_uri='')
print(flow.step1_get_authorize_url())



credentials = flow.step2_exchange(code)
