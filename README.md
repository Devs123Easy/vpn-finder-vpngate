# Easy VPN Finder

A small Python script that fetches public VPN servers from the VPN Gate API and generates an OpenVPN configuration file for the server you choose.

I originally made this for personal use, but decided to publish it in case anyone else finds it useful.

## Features

* Fetches currently available VPN servers from VPN Gate
* Parses the server list using Python's built-in `csv` module
* Displays server information such as:
  * IP address
  * Country
  * Ping
* Lets you choose a server interactively
* Decodes the OpenVPN configuration provided by VPN Gate
* Saves the selected configuration as:

```text
vpn.ovpn
```

## Requirements

Python 3 and the `requests` library.

Install `requests` with:

```bash
python -m pip install requests
```

On Windows you can also use:

```bash
py -m pip install requests
```

## Usage

Run the script:

```bash
python scan_vpn.py
```

The script will fetch the available servers and display a list similar to:

```text
Found 95 servers

1    36.12.228.153    Japan                    2 ms
2    110.66.191.52    Japan                    2 ms
3    58.80.42.154     Japan                    2 ms
4    110.67.198.122   Japan                    2 ms
```

Choose the number of the server you want to use:

```text
Input server 1 - 95: 3
```

The script will decode the `OpenVPN_ConfigData_Base64` field returned by the VPN Gate API and save the resulting configuration as:

```text
vpn.ovpn
```

You can then connect using OpenVPN (if you are on linux):

```bash
sudo openvpn --config vpn.ovpn
```

If the connection succeeds, OpenVPN should eventually display:

```text
Initialization Sequence Completed
```

You can verify your public IP with:

```bash
curl https://api.ipify.org
```

## How It Works

The script retrieves server data from:

```text
https://www.vpngate.net/api/iphone/
```

VPN Gate returns the server list in CSV format.

The script:

1. Downloads the server list
2. Removes unnecessary API comments
3. Parses the CSV data
4. Displays available servers
5. Lets the user select one
6. Reads the `OpenVPN_ConfigData_Base64` field
7. Decodes it from Base64
8. Saves the result as `vpn.ovpn`

## Notes

VPN Gate servers are public volunteer-operated VPN relay servers, so availability, latency and speed can change frequently.

Do not assume that a public VPN server is trusted. Avoid using random public VPN servers for sensitive activity such as banking, private accounts or confidential data.

This project is not affiliated with VPN Gate or the University of Tsukuba.

## Disclaimer

This project is provided for educational and personal-use purposes.

You are responsible for how you use the software and for complying with applicable laws, service terms and network policies.

## Code Quality™

Is this the most advanced VPN client ever created?

No.

Does it work?

Usually.

Did I spend way too much time making a fancy architecture for a script that downloads a `.ovpn` file?

Also no.

¯\*(ツ)*/¯
