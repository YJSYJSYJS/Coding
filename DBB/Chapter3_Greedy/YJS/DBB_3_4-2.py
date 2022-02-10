###
# op 1 가속화
# 2<=N<=100000, 2<=K<=100000
# iterate two operations until N==1
# op 1: N-=1
# op 2: N = N/K if (N%K==0) = True
# minimize iteration num
###

N, K = map(int, input().split())

cnt = 0
while N!=1:
    q = N//K
    r = N%K
    if r!=0:
        N-=r
        cnt+=r
    else:
        N=N/K
        cnt+=1
        
while N!=1:
    N -= 1
    cnt += 1

print(cnt)

# K가 2 이상이라는 전제조건은 최적해를 위한 중요한 조건이다!!!