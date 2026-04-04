# Auth0 Machine-to-Machine (M2M) Token Fetch

For the Auth0 Hackathon requirement, the agent must fetch a token using the Client Credentials flow. Do not implement a user-facing login flow. 

Use the `requests` library to fetch the token:

```python
import requests
import os

url = f"https://{os.getenv('AUTH0_DOMAIN')}/oauth/token"
payload = {
    "client_id": os.getenv("AUTH0_CLIENT_ID"),
    "client_secret": os.getenv("AUTH0_CLIENT_SECRET"),
    "audience": "[https://api.prismapi.ai](https://api.prismapi.ai)", # Or your specific API audience
    "grant_type": "client_credentials"
}
headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
token = response.json().get("access_token")
```
