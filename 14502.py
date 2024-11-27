import sys
input=sys.stdin.readline
import copy
from collections import deque

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    copy_data=copy.deepcopy(data)

    for i in range(n):
        for j in range(m):
            if copy_data[i][j]==2:
                q.append((i,j))

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if copy_data[nx][ny]==0:
                copy_data[nx][ny]=2
                q.append((nx,ny))
    
    global answer
    cnt=0

    for i in range(n):
        cnt+=copy_data[i].count(0)

    answer=max(answer,cnt)

def makewall(cnt):
    if cnt==3:
        bfs()
        return 

    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                makewall(cnt+1)
                data[i][j]=0

answer=0
makewall(0)
print(answer)