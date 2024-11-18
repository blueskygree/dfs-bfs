import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n=int(input())
data=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global count
    visited[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and data[nx][ny]==1:
            count+=1
            dfs(nx,ny)

res=[]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and data[i][j]==1:
            count=1
            dfs(i,j)
            res.append(count)

print(len(res))
res.sort()
for j in res:
    print(j)