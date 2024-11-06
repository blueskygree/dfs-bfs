import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n=int(input())
for _ in range(n):
    m,n,k=map(int,input().split())
    data=[[0]*m for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        data[b][a]=1


    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    count=0

    def dfs(x,y):
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny]==1:
                    data[nx][ny]-=1
                    dfs(nx,ny)
    for i in range(n):
        for j in range(m):
            if data[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)