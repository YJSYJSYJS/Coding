from collections import deque

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    now = queue.popleft()
    print(now, end=' ')
    for i in graph[now]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True


n,m,v = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

for i in range(1, n + 1):
  edges[i].sort()

print(edges)


visited = [False] * (n + 1)
dfs(edges, v, visited)
print()
visited = [False] * (n + 1)
bfs(edges, v, visited)

