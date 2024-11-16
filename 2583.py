import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

m,n,k=map(int,input().split())
data=[[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            data[i][j]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global count
    count+=1
    data[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<m and 0<=ny<n and data[nx][ny]==0:
            dfs(nx,ny)

num=[]
for i in range(m):
    for j in range(n):
        count=0
        if data[i][j]==0:
            dfs(i,j)
            num.append(count)

num.sort()
print(len(num))
for i in num:
    print(i,end=" ")
