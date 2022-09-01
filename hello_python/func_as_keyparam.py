# 키워드 매개변수에 함수 전달하기


books = [{
    "title": "hello python",
    "price": 30000
},{
    "title": "hello network",
    "price": 25000
},{
    "title": "hello linux",
    "price": 40000
}]

def getPrice(book):
    return book["price"]

print("# 가장 저렴한 책은?")
print(min(books, key=getPrice))  # -> price 값을 비교하여 최솟값을 구한다. 
print()

print("# 가장 비싼 책은?")
print(max(books, key=getPrice))
# lambda 사용! 
print(max(books, key=lambda x: x["price"]))

