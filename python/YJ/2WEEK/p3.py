# 딕셔너리 d와 키 key가 주어졌을 때, 해당 키가 딕셔너리에 존재하는지 여부를 반환하는 함수를 작성하세요.

def key_exists(d, key):
    # 구현하세요
    for ele in d:
        if ele == key:
            return True
    return False

print(key_exists({"name": "Alice", "age": 25}, "address"))
print(key_exists({}, "key"))