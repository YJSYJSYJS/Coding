###
# with loop
# input N(N%10==0: True)
# N = 500a + 100b + 50c + 10d
# min(a+b+c+d) = ?
###

N = int(input())

units = [500, 100, 50, 10]

cnt = 0

for u in units:
    curr_quotient = N//u
    cnt += curr_quotient
    N-=u*curr_quotient

print(cnt)    

###
# greedy의 정당성을 확신하고 적용해야함!
# 단위가 500 400 100
# 위의 방식으로 최적해가 나오지 않음! -> DP
###