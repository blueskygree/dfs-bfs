import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
s=int(input())
data=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(s):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

cnt=0
def bfs(v):
    global cnt
    q=deque([v])
    visited[v]=True

    while q:
        cur=q.popleft()

        for i in data[cur]:
            if not visited[i]:
                q.append(i)
                cnt+=1
                visited[i]=True

    return cnt

print(bfs(1))