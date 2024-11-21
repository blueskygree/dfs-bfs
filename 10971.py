import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
visited=[0]*n