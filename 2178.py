import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
data=[list(map(int,input().rstrip())) for _ in range(n)]

q=deque([(0,0)])

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and data[nx][ny]==1:
            q.append((nx,ny))
            data[nx][ny]=data[x][y]+1

print(data[n-1][m-1])