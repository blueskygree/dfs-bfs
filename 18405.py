import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
virus=[]
s,x,y=map(int,input().split())

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j],0,i,j))

virus.sort()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque(virus)
    
    while q:
        vir,time,x,y = q.popleft()
        
        if time == s:
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and data[nx][ny]==0:
                data[nx][ny]=vir
                q.append((vir,time+1,nx,ny))

bfs()
print(data[x-1][y-1])