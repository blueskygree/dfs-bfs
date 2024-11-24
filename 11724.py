import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    data[u].append(v)
    data[v].append(u)
visited=[False]*(n+1)

def dfs(v):
    visited[v]=True
    for i in data[v]:
        if not visited[i]:
            dfs(i)

cnt=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)