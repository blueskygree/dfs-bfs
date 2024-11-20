import sys
input=sys.stdin.readline
from collections import deque

m,n=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]

q=deque([])
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and data[nx][ny]==0:
                data[nx][ny]=data[x][y]+1
                q.append([nx,ny])

for i in range(n):
    for j in range(m):
        if data[i][j]==1:
            q.append([i,j])

bfs()

count=0
for i in data:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    count=max(count,max(i))
print(count-1)