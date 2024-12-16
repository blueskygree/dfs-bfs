import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m,r=map(int,input().split())
data=[[] for _ in range(n+1)]
visited=[0]*(n+1)
order=1

for _ in range(m):
    u,v=map(int,input().split())
    data[u].append(v)
    data[v].append(u)

def dfs(r):
    global order
    visited[r]=order
    order+=1
    for i in data[r]:
        if visited[i]==0:
            dfs(i)

for i in range(1,n+1):
    data[i].sort()

dfs(r)

for i in range(1,n+1):
    print(visited[i])