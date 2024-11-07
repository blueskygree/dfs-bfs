import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

r,c,k=map(int,input().split())
data=[list(input().rstrip()) for _ in range(r)]
visited=[[False]*c for _ in range(r)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=0

def dfs(x,y,dist):
    global count
    
    if x==0 and y==c-1 and dist==k:
        count+=1
        return
    else:
        visited[x][y]=True
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and data[nx][ny] != 'T':
            dfs(nx,ny,dist+1)
        
    visited[x][y]=False #백트래킹

dfs(r-1,0,1)
print(count)