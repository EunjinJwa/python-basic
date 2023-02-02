from lotto_request import request_lotto
import random

class LottoNumber:
    lotto_results = None
    unique_num_list = []
    num_count = {}

    def __init__(self, lotto_results):
        self.lotto_results = lotto_results
        self.unique_num_list = []
        self.num_count = {}
        self.gen_number_summary()

    def add_unique_num_list(self, number):
        if number not in self.unique_num_list:
            self.unique_num_list.append(number)

    def gen_number_summary(self):
        for result in self.lotto_results:
            self.add_unique_num_list(result['drwtNo1'])
            self.add_unique_num_list(result['drwtNo2'])
            self.add_unique_num_list(result['drwtNo3'])
            self.add_unique_num_list(result['drwtNo4'])
            self.add_unique_num_list(result['drwtNo5'])
            self.add_unique_num_list(result['drwtNo6'])

    def pick_numbers(self):
        target_list = self.unique_num_list.copy()
        print(self.unique_num_list)
        results = []
        for i in range(6):
            index = random.randrange(0, len(target_list))
            picked = target_list.pop(index)
            results.append(picked)
        return results
   
        

def get_lotto_numbers(drw_no):
    lotto_results = []
    for i in range(15):
        drw_no = drw_no - 1
        response = request_lotto(drw_no)
        lotto_results.append(response)
    
    return LottoNumber(lotto_results)

def gen_lucky_numbers(drw_no, count):
    results = []
    lotto_number_obj = get_lotto_numbers(drw_no)
    
    for i in range(count):
        results.append(lotto_number_obj.pick_numbers())
    
    return results
