import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000000)

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global size
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and data[nx][ny]==1:
            visited[nx][ny]=True
            size+=1
            dfs(nx,ny)

count=0
res=0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and data[i][j]==1:
            visited[i][j]=True
            size=1
            count+=1
            dfs(i,j)
            res=max(res,size)

print(count)
print(res)