#!/usr/bin/python3

import xml.etree.ElementTree as ET
from pprint import pprint
from xml.dom import minidom
import yaml

def make_extension(extension):
    extension_number = extension['extension_number']
    extension_elem = ET.SubElement(begin, 'Extension_{}_'.format(extension_number), attrib={'group':'Phone/Line_Key_{}_'.format(extension_number)})
    extension_elem.text = str(extension_number)
    ext_short_name = ET.SubElement(begin, 'Short_Name_{}_'.format(extension_number), attrib={'group':'Phone/Line_Key_{}_'.format(extension_number)})
    ext_short_name.text = str(extension['short_name'])
    ext_display_name = ET.SubElement(begin, 'Display_Name_{}_'.format(extension_number), attrib={'group':'Ext_{}/Subscriber_Information'.format(extension_number)})
    ext_display_name.text = str(extension['display_name'])
    user_id = ET.SubElement(begin, 'User_ID_{}_'.format(extension_number), attrib={'group':'Ext_{}/Subscriber_Information'.format(extension_number)})
    user_id.text = str(extension['user_id'])
    password = ET.SubElement(begin, 'Password_{}_'.format(extension_number), attrib={'group':'Ext_{}/Subscriber_Information'.format(extension_number)})
    password.text = str(extension['password'])
    dialplan = ET.SubElement(begin, 'Dial_Plan_{}_'.format(extension_number), attrib={'group':'Ext_{}/Dial_Plan'.format(extension_number)})
    dialplan.text = str(extension['dialplan'])
    share_call_appearance = ET.SubElement(begin, 'Share_Call_Appearance_{}_'.format(extension_number), attrib={'group':'Phone/Line_Key_{}'.format(extension_number)})
    share_call_appearance.text = str(extension['share_call_appearance'])
    share_ext = ET.SubElement(begin, 'Share_Ext_{}_'.format(extension_number, attrib={'group':'Ext_{}_/Share_Line_Appearance'.format(extension_number)}))
    share_ext.text = str(extension['share_ext'])
    nat_mapping_enable = ET.SubElement(begin, 'NAT_Mapping_Enable_{}_'.format(extension_number), attrib={'group':'Ext_{}_/NAT_Settings'.format(extension_number)})
    nat_mapping_enable.text = str(extension['nat_mapping_enable'])
    nat_keep_alive_enable = ET.SubElement(begin, 'NAT_Keep_Alive_Enable_{}_'.format(extension_number), attrib={'group':'Ext_{}_/NAT_Settings'.format(extension_number)})
    nat_keep_alive_enable.text = str(extension['nat_keepalive_enable'])
    sip_port = ET.SubElement(begin, 'SIP_Port_{}_'.format(extension_number), attrib={'group':'Ext_{}_/SIP_Settings'.format(extension_number)})
    sip_port.text = str(extension['sip_port'])
    proxy = ET.SubElement(begin, 'Proxy_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Proxy_and_Registration'.format(extension_number)})
    proxy.text = str(extension['proxy'])
    register = ET.SubElement(begin, 'Register_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Proxy_and_Registration'.format(extension_number)})
    register.text = str(extension['register'])
    register_expires = ET.SubElement(begin, 'Register_Expires_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Proxy_and_Registration'.format(extension_number)})
    register_expires.text = str(extension['register_expires'])
    preferred_codec = ET.SubElement(begin, 'Preferred_Codec_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Audio_Configuration'.format(extension_number)})
    preferred_codec.text = str(extension['preferred_codec'])
    use_pref_codec_only = ET.SubElement(begin, 'Use_Pref_Codec_Only_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Audio_Configuration'.format(extension_number)})
    use_pref_codec_only.text = str(extension['use_preferred_codec_only'])
    second_preferred_codec = ET.SubElement(begin, 'Second_Preferred_Codec_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Audio_Configuration'.format(extension_number)})
    second_preferred_codec.text = str(extension['second_preferred_codec'])
    third_preferred_codec = ET.SubElement(begin, 'Third_Preferred_Codec_{}_'.format(extension_number), attrib={'group':'Ext_{}_/Audio_Configuration'.format(extension_number)})
    third_preferred_codec.text = str(extension['third_preferred_codec'])
with open('cisco_inventory.yml', 'r') as inventory:
    inventory_output = yaml.load(inventory)
    for device in inventory_output:
        for device_name in inventory_output[device]:
            begin = ET.Element('flat-profile')
            station_name = ET.SubElement(begin, 'Station_Name', attrib={'group':'Phone/General'})
            station_name.text = str(device_name['name'])
            for info in device_name['extensions']:
                make_extension(info)
            mydata = minidom.parseString(ET.tostring(begin, encoding='UTF-8')).toprettyxml(indent=" ")
            with open("{}.xml".format(device_name['mac_address']), "w") as myfile:
                myfile.write(mydata)
