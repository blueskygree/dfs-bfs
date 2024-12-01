import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]


def dfs(x,y):
    dx=[data[x][y],0] # 이 문제의 핵심 
    dy=[0,data[x][y]] # 이 문제의 핵심
    visited[x][y]=True

    if x==n-1 and y==n-1:
        print("HaruHaru")
        sys.exit(0)

    for i in range(2):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            dfs(nx,ny)

visited[0][0]=True
dfs(0,0)
print("Hing")