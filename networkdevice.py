import requests
import json
from requests.auth import HTTPBasicAuth

# -------- ISE CONNECTION INFO --------
ISE_HOST = "10.10.10.10"        # ISE IP or FQDN
USERNAME = "ersadmin"           # ERS-enabled user
PASSWORD = "MySecretPassword"   # password
VERIFY_SSL = False              # set True if using trusted cert

# -------- NETWORK DEVICE INFO --------
DEVICE_NAME = "Switch-01"
DEVICE_IP = "192.168.10.5/32"   # ISE requires CIDR notation
RADIUS_SECRET = "Rad1usSecret123"
TACACS_SECRET = "TacacsSecret123"

# Optional Device Group (example)
DEVICE_GROUP = "Device Type#All Device Types"   # Must match ISE NDG hierarchy


def add_network_device():
    url = f"https://{ISE_HOST}/ers/config/networkdevice"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "NetworkDevice": {
            "name": DEVICE_NAME,
            "description": "Added by Python API script",
            "NetworkDeviceIPList": [
                {
                    "ipaddress": DEVICE_IP,
                    "mask": 32
                }
            ],
            "authenticationSettings": {
                "networkProtocol": "RADIUS",
                "radiusSharedSecret": RADIUS_SECRET
            },
            "tacacsSettings": {
                "sharedSecret": TACACS_SECRET,
                "connectModeOptions": "ON"
            },
            "NetworkDeviceGroupList": [
                DEVICE_GROUP
            ]
        }
    }

    # ---- SEND TO ISE ----
    print(f"Adding network device: {DEVICE_NAME} ...")

    resp = requests.post(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers=headers,
        data=json.dumps(payload),
        verify=VERIFY_SSL
    )

    print(f"HTTP Status: {resp.status_code}")
    try:
        print(resp.json())
    except:
        print(resp.text)


if __name__ == "__main__":
    add_network_device()
