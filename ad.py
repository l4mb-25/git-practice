import requests
import json
from requests.auth import HTTPBasicAuth

# -------- ISE CONNECTION INFO --------
ISE_HOST = "10.10.10.10"
USERNAME = "ersadmin"
PASSWORD = "MySecretPassword"
VERIFY_SSL = False

# -------- ACTIVE DIRECTORY GROUP INFO --------
AD_JOIN_POINT_ID = "12345678-90ab-cdef-1234-567890abcdef"  # AD Join Point UUID
AD_GROUP_DN = "CN=Contractors,OU=Groups,DC=corp,DC=local"  # AD Group DN


def add_ad_external_group():
    url = f"https://{ISE_HOST}/ers/config/activedirectory/{AD_JOIN_POINT_ID}/groups"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "OperationAdditionalData": {
            "additionalData": [
                {
                    "name": "groups",
                    "value": AD_GROUP_DN
                }
            ]
        }
    }

    print(f"Adding AD external group: {AD_GROUP_DN}")

    response = requests.post(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers=headers,
        data=json.dumps(payload),
        verify=VERIFY_SSL
    )

    print(f"HTTP Status: {response.status_code}")
    try:
        print(response.json())
    except:
        print(response.text)


if __name__ == "__main__":
    add_ad_external_group()
