####################################
# 1. 리스트의 합 문제
####################################

nums = [2, 7, 11, 15, 2, 7]
target = 9

result = []

for i in range(len(nums)):
    sum = 0
    for j in range(i+1, len(nums)):
        sum = nums[i]+ nums[j]
        if sum == target:
            if nums[i]>nums[j]:
                result.append((nums[i],nums[j]))
            else:
                result.append((nums[j], nums[i]))

result= set(result)
print("1번 문제 답: ")
print(list(result))

####################################
# 2. 연속된 1의 최대 길이
####################################

nums2 = [1, 1, 0, 1, 1, 1]

cnt = 0
max = 0
for i in nums2:
    if i==1:
        cnt+=1
    else:
        if max<cnt:
            max=cnt
        cnt=0

if max<cnt:
    max=cnt

print("2번 문제 답: ")
print(max)

####################################
# 3. 중복 요소 찾기
####################################

nums3 = [4, 3, 2, 7, 8, 2, 3, 1]

dic={}

for i in nums3:
    if i not in dic:
        dic[i]=0
    else:
        dic[i]+=1

tmpList=[]
for i, value in dic.items():
    if value>=1:
        tmpList.append(i)

print("3번 문제 답: ")        
print(sorted(tmpList))


####################################
# 4. 회전된 리스트의 회전 횟수 찾기
####################################

nums4 = [4, 5, 6, 7, 0, 1, 2]

newNums= sorted(nums4)
cnt4 = 0
if nums4 != newNums:
    while 1:
        item = nums4.pop(0)
        nums4.append(item)
        cnt4+=1

        if newNums==nums4:
            break

print("4번 문제 답: ")
print(cnt4)

####################################
# 5. 2D 리스트의 나선형 출력
####################################
        
matrix5 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 테스트용 데이터 
# matrix5 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

n5 = len(matrix5)
m5 = len(matrix5[0])

cnt5n = 0
cnt5m = 0
tmpList5=[]
check5 = 0
while 1:
    if m5==0 or n5==0:
        print("5번 문제 답: ")
        print(tmpList5)
        break


    if check5==0:
        for i in range(m5):
            tmpList5.append(matrix5[cnt5n][cnt5m])
            cnt5m+=1
        cnt5m-=1
    else:
        m5-=1
        for i in range(m5):
            cnt5m+=1
            tmpList5.append(matrix5[cnt5n][cnt5m])

    n5-=1
    for j in range(n5):
        cnt5n+=1
        tmpList5.append(matrix5[cnt5n][cnt5m])
    
    m5-=1
    for jj in range(m5):
        cnt5m-=1
        tmpList5.append(matrix5[cnt5n][cnt5m])

    n5-=1
    for ii in range(n5):
        cnt5n-=1
        tmpList5.append(matrix5[cnt5n][cnt5m])

    check5 = 1
    


    
    
    


####################################
# 6. 리스트에서 모듈러 연산 문제
####################################

nums6 = [2, 3, 5, 8, 10, 14]
k = 3

dic6={}

for i in nums6:
    key = i%k
    if key not in dic6:
        dic6[key]=1
    else:
        dic6[key]+=1

tmp6=[]
for key, value in dic6.items():
    tmp6.append((key, value))

print("6번 문제 답: ")
print(tmp6)

####################################
# 7. 슬라이딩 윈도우 최대합 문제
####################################

nums7 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k7 = 4
# 출력: 39  # 부분 리스트 [4, 2, 10, 23]의 합이 39로 최대

max7=0
for i in range(len(nums7)-k7):
    sum7 = 0
    for j in range(k7):
        sum7+=nums7[i+j]
    if max7<sum7:
        max7=sum7

print("7번 문제 답: ")
print(max7)

####################################
# 8. 특정 좌표의 8방향 값 출력 문제
####################################

matrix8 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x = 1
y = 1

dx=[0, 0, -1, 1, -1, -1, 1, 1]
dy=[1, -1, 0, 0, 1, -1, 1, -1]

n=len(matrix8)
m=len(matrix8[0])

tmpList8=[]
check=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or ny<0 or nx>=m or ny>=n:
        break
        check = 1
        print("벗어났다.")
    
    tmpList8.append(matrix8[ny][nx])

if check ==0:
    print("8번 문제 답: ")
    print(sorted(tmpList8))

####################################
# 9. 지뢰 찾기 의사코드 작성 문제
####################################

matrix9 = [
  ['M', '.', '.', 'M'],
  ['.', '.', '.', '.'],
  ['.', 'M', '.', '.']
]

## 일단 매트릭스와 같은 크기의 또다른 임시 매트릭스를 하나 더 만든다. 
## 기존의 매트릭스를 순회하면서 현재의 위치가 M 이면 임시 매트릭스의 현재 위치에도 M을 입력한다. 
## 8방향에 매트릭스가 존재한다면 임시 매트릭스의 현재 위치에 +1을 해준다. 

print("9번 문제 답: 일단 매트릭스와 같은 크기의 또다른 임시 매트릭스를 하나 더 만든다. ")
print("기존의 매트릭스를 순회하면서 현재의 위치가 M 이면 임시 매트릭스의 현재 위치에도 M을 입력한다. ")
print("8방향에 매트릭스가 존재한다면 임시 매트릭스의 현재 위치에 +1을 해준다. ")


## 문제가 살짝 이상한듯 합니다. 만약 주변 매트릭스에 의해 1이 입력된 경우, 그 다음 블록 순회시 또 매트릭스가 주변에 발견되면 
## 현재 output을 보면 +1을 해주는 것도 있고 안해주는것도 있는 것으로 보입니다. 


