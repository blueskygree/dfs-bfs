import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m,k=map(int,input().split())
data=[[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]
for i in range(k):
    r,c=map(int,input().split())
    data[r-1][c-1]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global count
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and data[nx][ny]==1:
            visited[nx][ny]=True
            count+=1
            dfs(nx,ny)

res=0

for i in range(n):
    for j in range(m):
        if data[i][j]==1 and not visited[i][j]:
            count=0
            dfs(i,j)
            res=max(res,count)

print(res)