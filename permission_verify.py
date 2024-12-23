import facebook
SYSTEM_USER_ACCESS_TOKEN = "EAAQHVzS6b54BO7ZApnlPAABVYT91FGgBq92GTlrh3LZCEhtWBkWfAM0ZBPyiizwFVNwek8ROm2tTIP4a6RbyQUc8FibGXeSDfZCNe731fO4b8Y87gIsE1sqCoCK7zWBzlwXrChwZCjytZCZBPgy1x1snIrURwXXsOBHvWSi4NH5oWXTmtiCeFDBJ6Ub6qlMH9qKkjeXJvHx"
graph = facebook.GraphAPI(access_token=SYSTEM_USER_ACCESS_TOKEN, version="3.1")
permissions = graph.get_object('/me/permissions')
print("### Access Token Permissions ###")
for perm in permissions['data']:
    print(f"Permission: {perm['permission']} | Status: {perm['status']}")