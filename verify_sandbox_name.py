import facebook

SYSTEM_USER_ACCESS_TOKEN = "EAAQHVzS6b54BO7ZApnlPAABVYT91FGgBq92GTlrh3LZCEhtWBkWfAM0ZBPyiizwFVNwek8ROm2tTIP4a6RbyQUc8FibGXeSDfZCNe731fO4b8Y87gIsE1sqCoCK7zWBzlwXrChwZCjytZCZBPgy1x1snIrURwXXsOBHvWSi4NH5oWXTmtiCeFDBJ6Ub6qlMH9qKkjeXJvHx"
AD_ACCOUNT_ID = "act_1402491704062551"  

try:
    graph = facebook.GraphAPI(access_token=SYSTEM_USER_ACCESS_TOKEN, version="3.1")    
    ad_account = graph.get_object(id=AD_ACCOUNT_ID, fields="name,id,account_status")

    print("### Sandbox Ad Account Details ###")
    print(f"Name: {ad_account['name']}")
    print(f"ID: {ad_account['id']}")
    print(f"Account Status: {ad_account['account_status']}")

except facebook.GraphAPIError as e:
    print("### Error with Facebook Graph API ###")
    print(f"Message: {e.message}")
    print(f"Type: {e.type}")
    print(f"Code: {e.code}")
except Exception as e:
    print("### Unexpected Error ###")
    print(e)
