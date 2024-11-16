import sys
ipnut=sys.stdin.readline

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and data[nx][ny]>h:
            visited[nx][ny]=True
            dfs(nx,ny)

ans=1
for x in range(max(map(max,data))): #문제의 핵심 각행마다 최고 값을 모으고 모은값중에서 최고 값(즉 data에서 최고값) 예를 들어 최고값이9이면 0~8까지 루프 돈다.
    visited=[[False]*n for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count+=1
                visited[i][j]=True
                dfs(i,j,x)
    ans=max(count,ans) # 그 중에서 안전영역의 개수가 가장 많은 것을 리턴
print(ans)