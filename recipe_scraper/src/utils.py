import json
import random

import fake_useragent
import requests
from bs4 import BeautifulSoup

def save_data(file_path, method="w", data=None):
    with open(file_path, method) as file:
        json.dump(data, file, indent=5, ensure_ascii=False)

def param(link, is_json=False):
    ua = fake_useragent.UserAgent().random
    headers = {
        "user-agent":ua,
    }
    r = requests.get(link, headers=headers).text
    if is_json:
        soup = json.loads(r)
    else:
        soup = BeautifulSoup(r, "lxml")
    return soup
