###
# 1<=N,M<=100, int
# N: 행, M: 열
# argmax_n(min(arr(n))), n is included in N
###

N, M = map(int, input().split())
ans = 1
for n in range(N):
    arr_n = list(map(int, input().split()))
    curr_min = min(arr_n)
    if ans < curr_min:
        ans = curr_min
print(ans)