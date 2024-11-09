import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=[list(input().rstrip()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
count=0

dx=[-1,1]
dy=[-1,1]

def dfs(x,y):
    if data[x][y]=='-':
        visited[x][y]=True
        for i in range(2):
            ny=y+dy[i]
            if 0<=ny<m and not visited[x][ny] and data[x][ny]=='-':
                dfs(x,ny)
    if data[x][y]=='|':
        visited[x][y]=True
        for i in range(2):
            nx=x+dx[i]
            if 0<=nx<n and not visited[nx][y] and data[nx][y]=='|':
                dfs(nx,y)

for i in range(n):
    for j in range(m):
        if not visited[i][j]: #방문하지 않은 경우에만 dfs
            dfs(i,j)
            count+=1
print(count)