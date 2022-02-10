from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

N = int(input())

for i in range(1,N+1):
  queue.append(i)

#print(queue)
#print(len(queue))


while (len(queue) > 1): # 1이상!
    queue.popleft() # 맨위에 날리기
    queue.append(queue.popleft()) # 그 다음 위에꺼 날린 다음에 큐 해주기
print(queue[0])
