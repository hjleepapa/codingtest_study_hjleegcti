# 방문 길이 (https://school.programmers.co.kr/learn/courses/30/lessons/49994)
# - 다시 풀어볼 문제
def is_valid_move(nx, ny):
    return -5 <= nx and nx <= 5 and -5 <= ny and ny <= 5

def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
    return nx, ny

def solution(dirs):
    x, y = 0, 0
    answer = set()
    
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        
        if not is_valid_move(nx, ny):
            continue
        
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
        
    return len(answer) / 2

print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))