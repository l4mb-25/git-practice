import requests
import json
from requests.auth import HTTPBasicAuth

# Disable warnings for self-signed certs (ISE commonly uses them)
requests.packages.urllib3.disable_warnings()

# ISE connection settings
ISE_HOST = "https://<ise-hostname-or-ip>"
USERNAME = "admin"
PASSWORD = "CISCOISE_PASSWORD"

# Policy Set API endpoint
url = f"{ISE_HOST}/ers/config/policyset"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Define the new Policy Set
policy_set_payload = {
    "PolicySet": {
        "name": "My-Automated-PolicySet",
        "description": "Created via API",
        "rank": 0,  # 0 = top of the list, use higher numbers for lower ranking
        "serviceName": "Default Network Access",
        "condition": {
            "conditionType": "ConditionReference",
            "isNegate": False,
            # You can use any existing condition UUID from ISE
            "id": "0f27c2f0-5f01-11e6-8b77-86f30ca893d3"
        }
    }
}

# Send the POST request
response = requests.post(
    url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    headers=headers,
    data=json.dumps(policy_set_payload),
    verify=False
)

# Print results
if response.status_code in [200, 201]:
    print("Policy Set created successfully!")
    print("Location:", response.headers.get("Location"))
else:
    print("Failed to create Policy Set")
    print("Status:", response.status_code)
    print(response.text)


    