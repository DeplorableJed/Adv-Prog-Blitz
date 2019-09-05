# Starting point for Lab 2 Advanced Path
from ncclient import manager
import sys

def main():
    with manager.connect(host=XXXX, port=XXXX, username=XXXX,
                         password=XXXX, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as XXXX:
        print('***Hear are the Remote Devices Capabilities***')

if __name__ == '__main__':
    sys.exit(main())
