# time limit: 1sec
# memory limit: 128mb

str_loc = input()
curr_loc = [ord(str_loc[0])-96, int(str_loc[1])]
moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
cnt = 0
for m in moves:
    moved = [curr_loc[0]+m[0], curr_loc[1]+m[1]]
    if moved[0]>0 and moved[0]<9 and moved[1]>0 and moved[1]<9:
        cnt+=1
print(cnt)