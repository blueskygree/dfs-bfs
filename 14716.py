import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000000)

m,n=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(m)]
visited=[[False]*n for _ in range(m)]

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def dfs(x,y):
    global cnt
    visited[x][y]=True

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and data[nx][ny]==1:
            dfs(nx,ny)

cnt=0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and data[i][j]==1:
            dfs(i,j)
            cnt+=1
print(cnt)