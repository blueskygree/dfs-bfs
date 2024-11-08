import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m=map(int,input().split())
data=[list(input().rstrip()) for _ in range(m)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
wcolor=0
bcolor=0

def dfs(x,y,cnt,color):
    data[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<m and 0<=ny<n:
            if data[nx][ny]==color:
                cnt=dfs(nx,ny,cnt+1,color)
    return cnt

for i in range(m):
    for j in range(n):
        if data[i][j]=='W':
            wcolor+=dfs(i,j,1,'W')**2
        elif data[i][j]=='B':
            bcolor+=dfs(i,j,1,'B')**2
print(wcolor,bcolor)