import sys
input=sys.stdin.readline


def dfs(start,now,value,cnt):
    global ans
    if cnt==n:
        if data[now][start]: # 현재 도시에서 시작 도시로 돌아가는 경로가 있는 경우에만 순회를 종료
            value+=data[now][start]
            if ans>value:
                ans=value
        return
    
    if value>ans: # 탐색 중인 경로의 비용이 이미 현재까지의 최소 비용보다 큰 경우 탐색을 더 진행하지 않고 종료시켜버림
        return

    for i in range(n):
        if not visited[i] and data[now][i]:
            visited[i]=1
            dfs(start,i,value+data[now][i],cnt+1)
            visited[i]=0

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
visited=[0]*n
ans=sys.maxsize

for i in range(n):
    visited[i]=1
    dfs(i,i,0,1)
    visited[i]=0
print(ans)