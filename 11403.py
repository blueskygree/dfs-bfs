import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int,input())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            