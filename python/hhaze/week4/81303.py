# 표 편집 (https://school.programmers.co.kr/learn/courses/30/lessons/81303)
# - 다시 풀어볼 문제
def solution(n, k, cmd):
    answer = ['O'] * n
    stack = []
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    k += 1
    
    for c in cmd:
        if c.startswith('C'):
            stack.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        elif c.startswith('Z'):
            idx = stack.pop()
            down[up[idx]] = idx
            up[down[idx]] = idx
        
        else:
            action, num = c.split( )
            
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
                    
    for i in stack:
        answer[i - 1] = 'X'
    
    return ''.join(answer)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))    # "OOOOXOOO"
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))    # "OOXOXOOO"