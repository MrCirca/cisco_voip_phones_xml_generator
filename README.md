# Cisco XML config file generator
It's a python script that generates configuration files for cisco voip devices.
You can add as many devices and extensions as you want

You should create a file in the same directory, naming 'cisco_inventory.yml'
So you can paste the given example try to create your own configuration file.

Example inventory
```
---
cisco_voip_devices:
  - name: 220
    mac_address: test_mac_address
    extensions:
      - extension_number: 1
        short_name: Line1
        display_name: extension_name_1
        user_id: test_user1
        password: password_1
        dialplan: test_dialplan_1
        share_call_appearance: private
        share_ext: private
        nat_mapping_enable: "Yes"
        nat_keepalive_enable: "Yes"
        proxy: voip.example.com
        register: "Yes"
        register_expires: 180
        preferred_codec: G722
        use_preferred_codec_only: "No"
        second_preferred_codec: G711a
        third_preferred_codec: G711u
        sip_port: 5070
      - extension_number: 2
        short_name: Line2
        display_name: display_name_2
        user_id: user_2
        password: password_2
        dialplan: dialplan_2
        share_call_appearance: private
        sip_port: 5060
        share_ext: private
        nat_mapping_enable: "Yes"
        nat_keepalive_enable: "Yes"
        proxy: voip.example.com
        register: "Yes"
        register_expires: 180
        preferred_codec: G722
        use_preferred_codec_only: "No"
        second_preferred_codec: G711a
        third_preferred_codec: G711u
```
