# 몸풀기 문제: 배열 제어하기
def solution(arr):
    arr = list(set(arr))
    arr.sort(reverse=True)

    return arr

print(solution([4, 2, 2, 1, 3, 4]))    # [4, 3, 2, 1]
print(solution([2, 1, 1, 3, 2, 5, 4]))    # [5, 4, 3, 2, 1]