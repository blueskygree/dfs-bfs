import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
a,b=map(int,input().split())
data=[[] for _ in range(n+1)]
visited=[False]*(n+1)
m=int(input())
res=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    data[x].append(y)
    data[y].append(x)

def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        cur=q.popleft()

        for i in data[cur]:
            if not visited[i]:
                q.append(i)
                res[i]=res[cur]+1
                visited[i]=True

bfs(a)
if res[b]>0:
    print(res[b])
else:
    print(-1)