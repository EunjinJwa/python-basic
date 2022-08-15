# dictionary : {key, value}

dictionary = {
    "name": "건조 딸기",
    "type": "당절임",
    "origin": "필리핀",
    "ingredient": ["딸기", "설탕", "색소"]
}

print("dictionary 요소 출력 : ", dictionary["name"])

dictionary["name"] = "건조 딸기 pro"
print("dictionary 요소 출력 : ", dictionary["name"])

if dictionary.get("price") == None:
    dictionary["price"] = 5000
print(dictionary)

for key in dictionary:
    print(key, " : ", dictionary[key])

# items() 함수 사용
for key, value in dictionary.items():
    print(key, " : ", value)