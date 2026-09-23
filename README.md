# Easy VPN finder using the vpngate api

I made this tool for personal use but decided to make it open-source so some **skids** can use it.\
You will need the requests library. You can install it using:
```
py -m pip install requests
```
This script works by fetching the servers from `https://www.vpngate.net/api/iphone/`, parsing it using csv, asking the user wich server to choose, decodes the `OpenVPN_ConfigData_Base64` from base64 and saves it to **vpn.ovpn**.\

Yes, yes I know this is a pretty unprofestional script and repo but I am too lazy to make an advanced one ¯\_(ツ)_/¯
