import requests
import json
from requests.auth import HTTPBasicAuth

ISE_HOST = "10.10.10.10"            # <-- your ISE FQDN or IP
USERNAME = "ersadmin"               # <-- ERS-enabled user
PASSWORD = "MySecretPassword"       # <-- ERS password
VERIFY_SSL = False                  # Set to True if you use valid certificates

# ---- Endpoint values to create ----
MAC_ADDR = "AA:BB:CC:DD:EE:01"
NAME = "Test-Endpoint-01"
DESCRIPTION = "Created via Python script"
GROUP_ID = None                     # Optional ISE Endpoint Group UUID


def add_endpoint():
    url = f"https://{ISE_HOST}/ers/config/endpoint"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "ERSEndPoint": {
            "name": NAME,
            "mac": MAC_ADDR,
            "description": DESCRIPTION
        }
    }

    # Add groupId only if supplied
    if GROUP_ID:
        payload["ERSEndPoint"]["groupId"] = GROUP_ID

    print("Sending POST to ISE...")
    response = requests.post(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        data=json.dumps(payload),
        headers=headers,
        verify=VERIFY_SSL,
    )

    print(f"HTTP Status: {response.status_code}")
    try:
        print("Response:")
        print(response.json())
    except:
        print(response.text)


if __name__ == "__main__":
    add_endpoint()