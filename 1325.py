import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
data=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    data[b].append(a)

def bfs(v):
    count=0
    visited=[False]*(n+1)
    q=deque([v])
    visited[v]=True
    while q:
        v=q.popleft()
        for i in data[v]:
            if not visited[i]:
                count+=1
                q.append(i)
                visited[i]=True
    return count

result=[]

for i in range(1,n+1):
    result.append(bfs(i))

for i in range(len(result)):
    if max(result)==result[i]:
        print(i+1)