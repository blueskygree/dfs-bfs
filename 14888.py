import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
cal=list(map(int,input().split()))

maximum=-10**9
minimum=10**9

def dfs(depth,total,plus,minus,mul,div):
    global maximum,minimum

    if depth==n:
        minimum=min(minimum,total)
        maximum=max(maximum,total)
        return
    
    if plus: # 숫자값이 0이면 거짓(false) 0이 아니면 참(true)로 판단단
        dfs(depth+1,total+data[depth],plus-1,minus,mul,div)
    if minus:
        dfs(depth+1,total-data[depth],plus,minus-1,mul,div)
    if mul:
        dfs(depth+1,total*data[depth],plus,minus,mul-1,div)
    if div:
        dfs(depth+1,int(total/data[depth]),plus,minus,mul,div-1)

dfs(1,data[0],cal[0],cal[1],cal[2],cal[3])
print(maximum)
print(minimum)