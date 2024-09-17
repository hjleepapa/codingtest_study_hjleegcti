def solution(n, answer, x, y):
    if n == 1:
        answer.append([x, y, n])
        return
    solution(n-1, answer, x, 6-x-y)
    answer.append([x, y, n])
    solution(n-1, answer, 6-x-y, y)


n = 3
answer = []
solution(n, answer, 1, 3)

for one, two, value in answer:
    one = one-1+65
    two = two-1+65
    print('Move disk', value, 'from', chr(one),'to', chr(two))
    
# 321  0   0
# 32   0   1 => 1-> 3
# 3    2   1 => 1-> 2
# 3    21  0 => 2-> 3
# 0    21  3 => 1-> 3
# 1    2   3 => 2-> 1
# 1    0   32 =>2-> 3 
# 0    0   321=>1-> 3

##1    2   3 
# 21   0   0 
# 2    1   0 => 1-> 2
# 0    1   2 => 1-> 3
# 0    0   21 => 2 -> 3

