# 크레인 인형 뽑기 게임 (https://school.programmers.co.kr/learn/courses/30/lessons/64061)
# - 다시 풀어볼 문제
def solution(board, moves):
    answer = 0
    lanes = [[] for _ in range(len(board[0]))]
    stack = []
    
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])
                
    for m in moves:
        if lanes[m - 1]:
            target = lanes[m - 1].pop()
            
            if stack and stack[-1] == target:
                answer += 2
                stack.pop()
            else:
                stack.append(target)
    
    return answer

print(
    solution(
        [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
        [1, 5, 3, 5, 1, 2, 1, 4]
    )
)