###
# without loop
# input N(N%10==0: True)
# N = 500a + 100b + 50c + 10d
# min(a+b+c+d) = ?
###

N = int(input())

a = N//500 if N>=500 else 0
res = N-500*a
b = res//100 if res>=100 else 0
res -= 100*b
c = res//50 if res>=50 else 0
res -= 50*c
d = res//10 if res>=10 else 0

ans = a+b+c+d
print(ans)

###
# greedy의 정당성을 확신하고 적용해야함!
# 단위가 500 400 100
# 위의 방식으로 최적해가 나오지 않음! -> DP
###