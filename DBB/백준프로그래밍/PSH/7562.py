from collections import deque

result = []
# 8방향 체크
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(x,y,n,m):
  queue = deque()
  queue.append([x,y])

  while queue:
    x, y = queue.popleft()
    if x == n and y == m:
      result.append(graph[x][y])
      break
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >=0 and nx < size and ny>=0 and ny<size and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append([nx,ny])


case = int(input())
for _ in range(case):
  size = int(input())
  graph = [[0]*size for _ in range(size)]
  x, y = map(int, input().split())
  n, m = map(int, input().split())
  bfs(x,y,n,m)
  
for i in result:
  print(i)