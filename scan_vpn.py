import csv
import io
import base64
try:
    import requests
except ImportError, ModuleNotFoundError:
    print("You need to install the requests library first! You can do it using 'py -m pip install requests'.")

URL = "https://www.vpngate.net/api/iphone/"

response = requests.get(URL, timeout=30)
response.raise_for_status()

lines = response.text.splitlines()

csv_lines = []

for line in lines:
    if line.startswith("#HostName"):
        csv_lines.append(line[1:])
    elif line.startswith("#") or line.startswith("*") or not line.strip():
        continue
    else:
        csv_lines.append(line)

reader = csv.DictReader(io.StringIO("\n".join(csv_lines)))
servers = list(reader)

print(f"Found {len(servers)} servers\n")

for i, server in enumerate(sorted(servers, key=lambda s: int(s["Ping"]) if str(s["Ping"]).isdigit() else 999999), start=1):
    print(
        f"{i:<4} "
        f"{server['IP']:<16} "
        f"{server['CountryLong']:<20} "
        f"{server["Ping"] if str(server["Ping"]).isdigit() else "NaN":>5} ms"
    )

while True:
    try:
        index = int(input(f"\nInput server 1 - {len(servers)}: ")) - 1
        break
    except KeyboardInterrupt:
        exit(0)
    except ValueError:
        print("You need to input a number (ctrl + C to cancel)!")
        continue
server = servers[index]

config_b64 = server["OpenVPN_ConfigData_Base64"]

config = base64.b64decode(config_b64).decode("utf-8")

filename = f"vpn.ovpn"

with open(filename, "w", encoding="utf-8") as f:
    f.write(config)

print(f"\nSaved configuration to: {filename}")