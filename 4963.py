import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def dfs(x,y):
    data[x][y]=0
    
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<h and 0<=ny<w and data[nx][ny]==1:
            dfs(nx,ny)

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    data=[]
    for _ in range(h):
        data.append(list(map(int,input().split())))

    count=0
    for i in range(h):
        for j in range(w):
            if data[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)
    