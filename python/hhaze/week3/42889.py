# 실패율 (https://school.programmers.co.kr/learn/courses/30/lessons/42889)
# - 다시 풀어볼 문제
def solution(N, stages):
    fails = {}
    total = len(stages)
    
    for i in range(1, N + 1):
        challenger = stages.count(i)
        
        if challenger == 0:
            fails[i] = 0
        else:
            fails[i] = challenger / total
            total -= challenger
    
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))    # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))    # [4, 1, 2, 3]