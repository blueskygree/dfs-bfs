import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
visited=[0]*100001

def bfs(v):
    q=deque([v])
    while q:
        current=q.popleft()

        if current==k:
            return visited[k]
        
        for i in (current-1,current+1,current*2):
            if 0<=i<100001 and not visited[i]:
                visited[i]=visited[current]+1
                q.append(i)
print(bfs(n))