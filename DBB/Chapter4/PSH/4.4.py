n, m = map(int, input().split()) # n : col , m : row


x, y, dir = map(int, input().split())

# N * M 맵은 list로 만들어주기
total_map = []
for i in range(n):
  total_map.append(list(map(int, input().split())))

# direction list랑 순서 맞추기 북 동 남 서
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 회전하는 걸 어떻게 표현할까? 왼쪽으로 회전하니까 북->서->남->동 (0.3.2.1)
# dir 변수 때문에 이것저것 생각함 global vs local 아니면 그때그때 받아서 쓸까

def direction():
  global dir
  if dir == 0:
    dir = 3
  else:
    dir -=1

# 가봤는지 안가봤는지도 생각해줘야함, 이중 for문으로 빈맵 하나 만들기
check_map = [[0 for col in range(n)] for row in range(m)]
check_map[x][y] = 1
count = 1
turn_time = 0 # 4방향 다 돌았으면 움직임을 멈추기 위한

# step 별로 진행하기
while True:
  direction()
  # 아직 가보지 않은 칸이 존재한다면이랑 육지일 경우!
  nx = x + dx[dir]
  ny = y + dy[dir]

  ############# 2단계 #############
  if total_map[nx][ny] == 0 and check_map[nx][ny] == 0:
    x = nx
    y = ny
    check_map[x][y] = 1
    count += 1
    turn_time = 0
    continue  # 다시 1조건으로 돌아가기 위해 while문을 continue
  else:
    turn_time = 1

  ############# 3단계 #############
  if turn_time == 4:
    nx = x - dx[dir]
    ny = y - dy[dir]

    if total_map[nx][ny] == 1:
      break
    else:
      x = nx
      y = ny
    turn_time = 0
    

print(count)


### 왜 계속 입력을 받지?..