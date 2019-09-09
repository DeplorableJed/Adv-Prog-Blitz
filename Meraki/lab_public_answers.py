# API Python module @ https://github.com/meraki/dashboard-api-python/blob/master/meraki.py


##### DO NOT MODIFY #####
from meraki import meraki
import random
import sys

my_key = 'e24759c28edd1d97715a6ba9ea8bc679c5d2706b'
orgs = meraki.myorgaccess(my_key)
org_names = [org['name'] for org in orgs]
index = org_names.index('Public API Lab')
my_org = orgs[index]['id']
##### DO NOT MODIFY #####


# 1. Create a network

#########################
##### START EDITING #####
my_name = 'Shiyue Cheng'
my_tags = ['Commercial', 'East', 'NewEngland']
my_time = 'US/Eastern'
###### END EDITING ######
#########################

# Get the current list of networks
current_networks = meraki.getnetworklist(my_key, my_org)

# Get the current networks' names
network_names = [network['name'] for network in current_networks]

# Was my_name changed from default 'First Last'?
if my_name == 'First Last':
    sys.exit('Part 1: please edit your name\n')
# Have tags been added?
elif my_tags == '':
    sys.exit(('Part 1: please add some tags\n'))
# Does the network already exist?
elif my_name in network_names:
    my_netid = current_networks[network_names.index(my_name)]['id']
    print('Part 1: the network {0} already exists with ID {1}\n'.format(my_name, my_netid))
# Add the new network
else:
    # Call to create a newtork
    my_network = meraki.addnetwork(my_key, my_org, my_name, 'wireless', my_tags, my_time)
    my_netid = my_network['id']
    print('Part 1: created network {0} with network ID {1}\n'.format(my_name, my_netid))



# 2. Return the inventory for an organization

#########################
##### START EDITING #####
# Call to return the inventory for an organization
# One line similar to above line 33's call on meraki.getnetworklist()
inventory = meraki.getorginventory(my_key, my_org)
###### END EDITING ######
#########################

# Filter out used devices already allocated to networks
unused = [device for device in inventory if device['networkId'] is None]
print('Part 2: found total of {0} unused devices in inventory\n'.format(len(unused)))



# 3. Claim a device into a network

# Check if network already contains a device
my_network_devices = meraki.getnetworkdevices(my_key, my_netid)

# No device in network yet
if len(my_network_devices) == 0:
    # Pick a random AP from the unused inventory
    my_ap = random.choice(unused)
    my_serial = my_ap['serial']
    print('Part 3: found an unused AP from inventory, with serial number {0}\n'.format(my_serial))

    #########################
    ##### START EDITING #####
    # Call to claim a device into a network
    # Only one line needs to be filled here, with the same indentation (4 spaces)
    meraki.adddevtonet(my_key, my_netid, my_serial)
    ###### END EDITING ######
    #########################

    # Check if device was claimed correctly
    if len(meraki.getnetworkdevices(my_key, my_netid)) == 0:
        sys.exit('Part 3: AP not successfully claimed\n')
    else:
        print('Part 3: added AP {0} into the {1} network\n'.format(my_serial, my_name))
# Device already added
else:
    my_ap = my_network_devices[0]
    my_serial = my_ap['serial']
    print('Part 3: AP {0} already added to network {1}\n'.format(my_serial, my_name))



# 4. Update the attributes of a device

#########################
##### START EDITING #####
my_address = 'Lake Myvatn, Iceland'
###### END EDITING ######
#########################

# Check if address changed from default
if my_address == '500 Terry A. Francois Blvd, San Francisco, CA 94158' or my_address == '':
    sys.exit('Part 4: change your address to your favorite vacation spot (not 500TF)!\n')

#########################
##### START EDITING #####
# Call to update the attributes of a device
# Only change this one line below
meraki.updatedevice(my_key, my_netid, my_serial, my_name, my_tags, address=my_address, move='true')
###### END EDITING ######
#########################

# Check if all attributes were updated and marked moved
device_detail = meraki.getdevicedetail(my_key, my_netid, my_serial)
try:
    device_tags = device_detail['tags'].strip()
except:
    sys.exit('Part 4: no tags were applied to the device\n')
if device_detail['name'] != my_name:
    sys.exit('Part 4: the name of the device was not changed\n')
elif set(device_tags.split()) != set(my_tags):
    sys.exit('Part 4: the tags of the device were not changed\n')
elif device_detail['address'] != my_address:
    sys.exit('Part 4: the address of the device was not changed\n')
elif device_detail['lat'] == 37.4180951010362 and device_detail['lng'] == -122.098531723022:
    sys.exit('Part 4: the marker for the address was not moved\n')
else:
    print('Part 4: updated address of AP {0} to {1}\n'.format(my_serial, my_address))



# 5. Update the attributes of an SSID

#########################
##### START EDITING #####
my_ssid_name = 'Chengineer'
my_ssid_psk = 'meraki123'
###### END EDITING ######
#########################

# Check if defaults have been changed
if my_ssid_name == '' or my_ssid_psk == '':
    sys.exit('Part 5: please edit your SSID name and PSK\n')

#########################
##### START EDITING #####
# Call to update the attributes of an SSID
# Only add one line here to call the function
meraki.updatessid(my_key, my_netid, 0, my_ssid_name, True, 'psk', 'wpa', my_ssid_psk)
###### END EDITING ######
#########################

# Check if SSID was updated correctly
ssids = meraki.getssids(my_key, my_netid)
if ssids[0]['name'] != my_ssid_name:
    sys.exit('Part 5: SSID in the first slot not successfully updated\n')
elif my_ssid_name not in [ssid['name'] for ssid in ssids]:
    sys.exit('Part 5: SSID not successfully updated\n')
elif ssids[0]['psk'] != my_ssid_psk:
    sys.exit('Part 5: SSID not successfully updated\n')
elif ssids[0]['enabled'] != True:
    sys.exit('Part 5: SSID not enabled\n')
else:
    print('Part 5: updated the network {0} with SSID {1} in the first slot\n'.format(my_name, my_ssid_name))

print('You have successfully completed the Dashboard API Python lab. Congratulations!!\n')



# BONUS. Update the attributes of an SSID

#########################
##### START EDITING #####
# Call to update the attributes of all other SSIDs
# Edit the two lines and only two lines here
for x in range(1, 15):
    # Remove pass, and fill in the blank by calling a function
    meraki.updatessid(my_key, my_netid, x, my_ssid_name+str(x), True, 'psk', 'wpa', my_ssid_psk)
###### END EDITING ######
#########################

# Check if all other SSIDs were updated correctly
ssids = meraki.getssids(my_key, my_netid)
for name in [ssid['name'] for ssid in ssids]:
    if 'Unconfigured' in name:
        sys.exit('Bonus: not all SSIDs updated yet\n')
    else:
        pass
print('You have completed the bonus question. Awesome!!\n')
