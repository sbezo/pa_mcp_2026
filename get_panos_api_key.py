import json
import sys
import argparse
import requests
from time import sleep
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("PA_USERNAME")
password = os.getenv("PA_PASSWORD")
ip = os.getenv("PA_HOST")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('Generate_API_key')
url = 'https://'+ip+'/api/v1/generate_api_key'

credentials = {"username":user, "password":password}
print(credentials)

r = requests.post(url, data=credentials, verify=False)
response=r.json()
apiKey = json.dumps(response['Contents']['response']['data']['content']['api_key'])
auth_token = apiKey[1:-1]
print(auth_token)
print('')

hed = {'Authorization': 'Bearer ' + auth_token}