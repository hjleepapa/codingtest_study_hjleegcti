from itertools import combinations

def solution(numbers):
    tmp = list((combinations(numbers, 2)))
    tmpSum=[]
    for i in tmp:
        a, b= i
        sum = a+b
        tmpSum.append(sum)
    tmpSum=set(tmpSum)
    return sorted(list(tmpSum))