lotto_results = []
unique_num_list = []
num_count = {}

def add_lotto_results(response):
    lotto_results.append(response)
    
def get_lotto_results():
    return lotto_results

def add_unique_num_list(number):
    if number not in unique_num_list:
        unique_num_list.append(number)

def add_num_count(number):
    if number in num_count:
        num_count[number] = num_count[number] + 1
    else:
        num_count[number] = 1

def get_unique_num_list():
    return unique_num_list

def has_data():
    return len(lotto_results) > 0




