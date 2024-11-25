import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
data=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

q=deque()
q.append(1)

def bfs():
    while q:
        now=q.popleft()
        for i in data[now]:
            if visited[i]==0:
                visited[i]=now
                q.append(i)

bfs()
res=visited[2:]
for i in res:
    print(i)