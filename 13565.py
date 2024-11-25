import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

m,n=map(int,input().split())
data=[list(map(int,input().rstrip())) for _ in range(m)]
visited=[[False]*n for _ in range(m)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    visited[x][y]=True

    if x==m-1:
        print("YES")
        sys.exit(0)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and data[nx][ny]==0:
            dfs(nx,ny)

for j in range(n):
    if data[0][j]==0 and not visited[0][j]:
        dfs(0,j)

print("NO")