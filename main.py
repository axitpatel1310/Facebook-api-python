import requests

ACCESS_TOKEN = "EAAQHVzS6b54BO7ZApnlPAABVYT91FGgBq92GTlrh3LZCEhtWBkWfAM0ZBPyiizwFVNwek8ROm2tTIP4a6RbyQUc8FibGXeSDfZCNe731fO4b8Y87gIsE1sqCoCK7zWBzlwXrChwZCjytZCZBPgy1x1snIrURwXXsOBHvWSi4NH5oWXTmtiCeFDBJ6Ub6qlMH9qKkjeXJvHx"
AD_ACCOUNT_ID = "act_1402491704062551"
GRAPH_API_VERSION = "v21.0"
BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}"

CAMPAIGN_NAME = "Python Created Campaign"
CAMPAIGN_OBJECTIVE = "OUTCOME_AWARENESS"  
CAMPAIGN_STATUS = "PAUSED"  
SPECIAL_AD_CATEGORIES = ["NONE"]

url = f"{BASE_URL}/{AD_ACCOUNT_ID}/campaigns"

payload = {
    "access_token": ACCESS_TOKEN,
    "name": CAMPAIGN_NAME,
    "objective": CAMPAIGN_OBJECTIVE,
    "status": CAMPAIGN_STATUS,
    "special_ad_categories": SPECIAL_AD_CATEGORIES,
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    campaign = response.json()
    print("### Campaign Created Successfully ###")
    print(f"Campaign ID: {campaign['id']}")
else:
    print("### Error Creating Campaign ###")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")