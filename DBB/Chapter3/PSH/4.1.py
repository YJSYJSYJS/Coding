n = int(input())
x,y = 1,1
x_n,y_n = 1,1
dir = input().split()  # 여러개 입력으로 받기

move = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 입력 횟수 만큼 돌면서 이 방향이 어떤건지 확인이면...move안에서 for문으로 돌려서 학인해봐야하나..
for i in dir:
  for j in range(len(move)):
    if i == move[j]:
      x_n = x + dx[j]
      y_n = y + dy[j]
  if x_n>=1 and y_n>=1:
    x = x_n
    y = y_n

print(x,y)

# 