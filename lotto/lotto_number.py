import json
import requests
import random
from database.memory_db import add_lotto_results, has_data, get_lotto_results, add_unique_num_list, add_num_count, get_unique_num_list


def set_unique_num(result):
    add_unique_num_list(result['drwtNo1'])
    add_unique_num_list(result['drwtNo2'])
    add_unique_num_list(result['drwtNo3'])
    add_unique_num_list(result['drwtNo4'])
    add_unique_num_list(result['drwtNo5'])
    add_unique_num_list(result['drwtNo6'])


def get_lotto_request(drw_no):
    for i in range(15):
        drw_no = drw_no - 1
        response = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drw_no}")
        add_lotto_results(json.loads(response.text))
    
    results = get_lotto_results()
    for result in results:
        set_unique_num(result)
        set_num_count(result)
    

num_count = {}

results = []





def set_num_count(num):
    add_num_count(num['drwtNo1'])
    add_num_count(num['drwtNo2'])
    add_num_count(num['drwtNo3'])
    add_num_count(num['drwtNo4'])
    add_num_count(num['drwtNo5'])
    add_num_count(num['drwtNo6'])




def pick_numbers():
    unique_num_list = get_unique_num_list()
    print(">>", unique_num_list)
    results = []
    for i in range(6):
        index = random.randrange(0, len(unique_num_list))
        picked = unique_num_list[index]
        results.append(picked)
    return results


def gen_lottos(drw_no):
    if has_data() == False:
        get_lotto_request(drw_no)

    sorted_nums = sorted(num_count.items(), key=lambda item: item[1], reverse=True)
    return pick_numbers()
