import requests
import json

def request_lotto(drw_no):
    response = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drw_no}")
    return json.loads(response.text)