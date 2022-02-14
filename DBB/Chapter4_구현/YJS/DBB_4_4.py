'''
1. 맵 사이즈, 현재위치 및 방향, 맵 입력
1-1. 맵에서 외곽부분(항상 바다) 제외
2. 육지 바다 확인
2-1. 육지
- 이동
- visited 추가
- 이동한 위치에서 확인(2번으로)
2-2. 바다
- visited 확인
- 남은 방향 있으면 회전 후 확인(2번으로)
- 남은 방향 없으면
  - visite.pop()
  - turn(visited)
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
for p in pos:
    p-=1

# 북동남서
moves = [[-1,0,0],[0,1,0],[0,-1,0],[1,0,0]]
visited = list()
curr_pos = [pos[0]-1,pos[1]-1,pos[2]]
visited.append([curr_pos[0],curr_pos[1],[curr_pos[2]]])
cnt=1

def move(loc):
    global moves
    return list(map(lambda x,y:x+y,loc,moves[loc[2]]))

def check(p):
    next_loc = move(p)
    try:
        if field[next_loc[0]][next_loc[1]]:
            return False
        else:
            return True
    except:
        return False

def turn(v):
    looked = v[-1][2].copy()
    curr_sight = looked[-1]
    curr_sight-=1
    if curr_sight<0:
        curr_sight+=4
    v[-1][2].append(curr_sight)
    return v

def dfs(curr_loc, v):
    global cnt
    print(curr_loc, visited)

    if check(curr_loc):# 육지
        print(1)
        v.append([curr_loc[0],curr_loc[1],[curr_loc[2]]])
        cnt+=1
        return dfs(move(curr_loc), v)
    elif len(visited[-1][2])<=4: # 바다 and 방향 남음
        print(2)
        return dfs(curr_loc, turn(v))
    else: # 바다 and 방향 다 봄
        print(3)
        visited.pop()
        if len(visited)==0:
            print(31)
            return
        else:
            print(32)
            return dfs(curr_loc, turn(v))

dfs(curr_pos, visited)

print(cnt)