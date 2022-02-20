n = int(input())
graph = []

for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  global count
  if x<= -1 or x >= n or y <= -1 or y >= n:
    return False
  if graph[x][y] == 1: # 1이 연결된 곳을 찾아야 하니까 1을 0으로 바꿔주기
    count += 1
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False


result = 0
count = 0
house = []
for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      result += 1
      house.append(count)
      count = 0

print(result)
house.sort()
for i in house:
  print(i)


