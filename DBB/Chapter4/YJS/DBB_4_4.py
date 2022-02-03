'''
1. 맵 사이즈, 현재위치 및 방향, 맵 입력
1-1. 맵에서 외곽부분(항상 바다) 제외
2. 현재위치에서 방향전환(왼쪽부터 반시계방향)
 - loop start
 - (loc0, loc1, dir) 기록 append
3. 해당 방향 바다 육지 여부
3-1. 바다면 방향 전환
3-1-1. 모든 방향 다 봤을 경우
3-1-1-1. 이전 step 존재시, backstep
3-1-1-2. 존재하지 않으면 종료
3-2. 육지면 step, cnt+=1 후 2번으로
 - 방문 기록 pop
'''
# 1. input
N, M = map(int, input().split())
pos = list(map(int, input().split()))
field = list()
for n in range(N):
    field.append(list(map(int, input().split())))

# 1-1. trim map
field = field[1:-1]
for f in field:
    del f[0]
    del f[-1]

# 북동남서
moves = [[-1,0,0],[0,1,0],[0,-1,0],[1,0,0]]

def step(p):
    # 위치(pos[0], pos[1]) 변경
    return list(map(lambda x,y:x+y, p, moves[p[2]]))
        
def turn(p):
    # 방향이 육지일때까지 방향전환
    ## 방문한 육지 생략
    ## 바다만 있을 경우 이전으로 이동
    ## 이전이 없으면 exit signal return
    p[2]-=1
    if p[2]<0:
        p[2]+=4

    return p

# 이동 경험 기억(DFS)
poses = list() # pos list
poses.append(pos)
pos = turn(pos)
poses.append(pos)
cnt=0

def move():
    for m in moves:
        if not field[pos[0], pos[1]]:# 육지
            pos = step(pos)
            poses.append(pos)
        else: # 바다
            pos = turn(pos)
            # recursion 필요(육지 or 바다)

# while True:
#     visited = list()
#     if not field[pos[0], pos[1]]:# 육지
#         pos = step(pos)
#         poses.append(pos)
#     else: # 바다
#         pos = turn(pos)
#         # recursion 필요(육지 or 바다)