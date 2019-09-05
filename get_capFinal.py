# Lab 2 Finished Example

from ncclient import manager
import sys

HOST = '10.10.10.11'
PORT = 830

USER = 'cisco'
PASS = 'cisco'

def main():
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:
        print('***Hear are the Remote Devices Capabilities***')
        for capability in m.server_capabilities:
            print(capability)

if __name__ == '__main__':
    sys.exit(main())
