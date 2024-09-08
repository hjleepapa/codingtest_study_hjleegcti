def solution(n, k, cmd):
    # 1 삭제된 행의 인덱스를 저장하는 리스트
    deleted = []
    
    # 2 링크드리스트에서 각 행의 위아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]
    #print('up', up)
    down = [i + 1 for i in range(n + 1)]
    #print('down', down)
    
    # 3 현재 위치를 나타내는 인덱스
    k += 1
    
    # 4 주어진 명령어(cmd) 리스트를 하나씩 처리
    for cmd_i in cmd:
        # 5 현재 위치를 삭제하고 그 다음 위치로 이동
        if cmd_i.startswith("C"): # 접두사 판별 함수
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        # 6 가장 최근에 삭제된 행을 복원
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        
        # 7 U 또는 D를 사용해 현재 위치를 위아래로 이동
        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

        # 8 삭제된 행의 위치에 'X'를, 그렇지 않은 행의 위치에 'O'를 포함하는 문자열 반환
    answer = ["O"] * n
    
    for i in deleted:
        answer[i - 1] = "X"
        
    return "".join(answer)