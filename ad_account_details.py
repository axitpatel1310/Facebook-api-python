import facebook

SYSTEM_USER_ACCESS_TOKEN = "EAAQHVzS6b54BO7ZApnlPAABVYT91FGgBq92GTlrh3LZCEhtWBkWfAM0ZBPyiizwFVNwek8ROm2tTIP4a6RbyQUc8FibGXeSDfZCNe731fO4b8Y87gIsE1sqCoCK7zWBzlwXrChwZCjytZCZBPgy1x1snIrURwXXsOBHvWSi4NH5oWXTmtiCeFDBJ6Ub6qlMH9qKkjeXJvHx"
AD_ACCOUNT_ID = "act_1402491704062551"  

graph = facebook.GraphAPI(access_token=SYSTEM_USER_ACCESS_TOKEN)

try:
    ad_account = graph.get_object(f'/{AD_ACCOUNT_ID}', fields='id,name,account_status,currency,amount_spent')
    print("### Ad Account Details ###")
    print(f"ID: {ad_account['id']}")
    print(f"Name: {ad_account['name']}")
    print(f"Account Status: {ad_account['account_status']}")
    print(f"Currency: {ad_account['currency']}")
    print(f"Amount Spent: {ad_account['amount_spent']} {ad_account['currency']}")
except facebook.GraphAPIError as e:
    print(f"Error: {e}")
