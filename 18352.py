import sys
input=sys.stdin.readline
from collections import deque

n,m,k,x=map(int,input().split())
data=[[] for _ in range(n+1)]
visited=[False]*(n+1)
distance=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)

def bfs(x):
    answer=[]
    q=deque([x])
    visited[x]=True
    distance[x]=0
    while q:
        now=q.popleft()
        for i in data[now]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                distance[i]=distance[now]+1
                if distance[i]==k:
                    answer.append(i)
    
    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(x)