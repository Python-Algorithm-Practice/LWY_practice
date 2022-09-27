n = int(input())
arr = list(map(int,input().split()))
arr.sort()
before = arr[0]

INF = float('inf')
leftValue = 0
rightValue = 0

#안테나 설치하는 집 
minHomeIndex = -1
#안테나 설치시 모든 집까지 총합
minHomeValue = INF

for i in range(len(arr)):
    temp = 0
    if i==0:
        for j in range(len(arr)):
            rightValue += abs(arr[j]-arr[0])
        temp = rightValue
    else:
        #왼쪽, 오른쪽에 있는 집의 개수
        left,right = i,n-i-1
        differ = abs(arr[i]-before)

        leftValue = leftValue + differ*left
        rightValue = rightValue - differ*(right+1)

        temp = leftValue + rightValue
        before = arr[i]
    
    if temp < minHomeValue:
        minHomeIndex = i
        minHomeValue = temp

print(arr[minHomeIndex])