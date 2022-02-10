###
# 큰 수의 법칙 - 수학적 풀이
# 2<=N<=1000, 1<=M<=10000, 1<=K<=10000, integer
# nums: list, len(nums)=N
# K<=M
###

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

block = list()
for k in range(K):
    block.append(nums[0])
block.append(nums[1])

sum = M//(K+1)*sum(block)
res = M%(K+1)
for r in range(res):
    sum += block[r]

print(sum)