import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n=int(input())
data=[[] for _ in range(n+1)]
visited=[False]*(n+1)
distance=[0 for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

def dfs(v):
    visited[v]=True
    for i in data[v]:
        if not visited[i]:
            distance[i]=distance[v]+1
            dfs(i)

dfs(1)
res=0
for i in range(2,n+1):
    if len(data[i])==1: #리프노드를 찾는 것
        res+=distance[i]

if res%2==0:
    print("No")
else:
    print("Yes")