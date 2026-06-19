import requests
import urllib3
import os
from dotenv import load_dotenv, set_key
import xml.etree.ElementTree as ET

load_dotenv()

user = os.getenv("PA_USERNAME")
password = os.getenv("PA_PASSWORD")
ip = os.getenv("PA_HOST")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('Generate_API_key')
url = 'https://'+ip+'/api/'

params = {
    "type": "keygen",
    "user": user,
    "password": password,
}

r = requests.get(url, params=params, verify=False, timeout=30)

root = ET.fromstring(r.text)
auth_token = root.findtext("./result/key")

# Save/refresh the API token to the .env file
if auth_token:
    set_key(".env", "PA_TOKEN", auth_token)
    
