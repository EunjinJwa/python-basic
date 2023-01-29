db = {}

def add(key, value):
    db[key] = value

def get(key):
    return db[key]

def exists_keyword(keyword):
    return keyword in db