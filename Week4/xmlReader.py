__author__ = 'marco'
import xml.etree.ElementTree as ET
tree = ET.parse('networkConfig.xml')
root = tree.getroot()

for devices in root:
    print(devices.tag)
    count = 1
    for device in devices:
        print(device.tag + " " + str(count) + " - Operating System: " + device.find('os').text + " - IP Address: " + device.find('ipAddress').text)
        count += 1
    print()