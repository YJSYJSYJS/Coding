###
# 큰 수의 법칙
# 2<=N<=1000, 1<=M<=10000, 1<=K<=10000, integer
# nums: list, len(nums)=N
# K<=M
###

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

sum = 0
life=3
for m in range(M):
    if life!=0:
        sum+=nums[0]
        life -= 1
    else:
        sum+=nums[1]
        life = 3

print(sum)