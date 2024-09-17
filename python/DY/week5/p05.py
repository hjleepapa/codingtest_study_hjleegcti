def solution(start, answer, n):
    if start == n:
        return answer

    if n % start==0:
        if start > n//start:
            answer.append((n//start, start))
        else:
            answer.append((start, n//start))
    start+=1
    solution(start, answer, n)

n = 12

answer = []
solution(1, answer, n)
print(list(set(answer)))