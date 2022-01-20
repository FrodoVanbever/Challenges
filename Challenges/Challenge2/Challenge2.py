import requests
import json
current_access_token = "MjVlYjZmZWQtYTc4Yi00YjczLWI5ZmMtOTg3MGRjYzRhMjNkYzUwZGVmYmEtZTUx_P0A1_5998ff09-9c27-4407-818f-2305709e8d49" #token verander na 12u
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path 
headers = {
    'Authorization': 'Bearer {}'.format(current_access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
user_name = res.json()['displayName']

if res.status_code == 200:
    print("Status is OK")
    print("Username: " + user_name)
else:
    print("Status is not OK")
