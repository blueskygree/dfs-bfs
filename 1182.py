"""import sys
input=sys.stdin.readline
from itertools import combinations

n,s=map(int,input().split())
data=list(map(int,input().split()))
count=0

for i in range(1,n+1):
    cmb=combinations(data,i)

    for x in cmb:
        if sum(x)==s:
            count+=1
print(count)""" # 조합으로 구현(조합은 순열과 다르게 순서를 고려하지 않기 때문에 중복이 없다)

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000000)

n,s=map(int,input().split())
data=list(map(int,input().split()))
count=0

def dfs(index,current_sum):
    global count
    if index==n:
        return
    
    current_sum+=data[index]

    if current_sum==s:
        count+=1

    dfs(index+1,current_sum) #현재 data[index]를 선택한 경우

    dfs(index+1,current_sum-data[index]) #현재 data[index]를 선택하지 않는 경우

dfs(0,0)
print(count)