import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000000)

n,m,v=map(int,input().split())
data=[[] for _ in range(n+1)]
visited1=[False]*(n+1)
visited2=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

for i in data:
    i.sort()

def dfs(v):
    visited1[v]=True
    print(v,end=" ")
    for i in data[v]:
        if not visited1[i]:
            dfs(i)

def bfs(v):
    q=deque([v])
    visited2[v]=True
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in data[v]:
            if not visited2[i]:
                q.append(i)
                visited2[i]=True

dfs(v)
print()
bfs(v)