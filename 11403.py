import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int,input())) for _ in range(n)]
visited=[0 for _ in range(n)]

def dfs(x):
    for i in range(n):
        if data[x][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[i]==1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
    visited=[0 for _ in range(n)]