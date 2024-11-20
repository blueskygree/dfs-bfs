import sys
input=sys.stdin.readline


def dfs(v):
    visited[v]=1
    next=data[v]
    if visited[next]==0:
        dfs(next)

t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    data.insert(0,0)
    visited=[0]*(n+1)
    cnt=0

    for i in range(1,n+1):
        if visited[i]==0:
            dfs(i)
            cnt+=1
    print(cnt)

