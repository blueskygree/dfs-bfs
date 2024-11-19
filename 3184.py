import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

r,c=map(int,input().split())
data=[list(input().rstrip()) for _ in range(r)]
visited=[[False]*c for _ in range(r)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
total_sheep=0
total_wolf=0

def dfs(x,y):
    global s_count,w_count
    visited[x][y]=True

    if data[x][y]=='o':
        s_count+=1
    elif data[x][y]=='v':
        w_count+=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and data[nx][ny]!='#':
            dfs(nx,ny)



for i in range(r):
    for j in range(c):
        if not visited[i][j] and data[i][j]!='#':
            s_count=0
            w_count=0
            dfs(i,j)
            if s_count>w_count:
                total_sheep+=s_count
            elif w_count>=s_count:
                total_wolf+=w_count

print(total_sheep,total_wolf)
