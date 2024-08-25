# 튜플 tpl이 주어졌을 때, 튜플 내 모든 요소의 합을 반환하는 함수를 작성하세요.

def sum_of_tuple(tpl):
    # 구현하세요
    result = 0
    for ele in tpl:
        result += ele
    return result

print(sum_of_tuple(()))  # 출력: 0
print(sum_of_tuple((5,)))  # 출력: 5
