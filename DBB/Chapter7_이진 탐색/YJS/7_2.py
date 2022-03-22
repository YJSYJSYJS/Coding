'''
time: 2sec
mem: 128MB
input:
 - N(1~1000000), M(1~2000000000)
 - 떡 높이(0~1,000,000,000)
output:
 - 절단기 높이(H)
''' 
N, M = map(int, input().split()) # 떡 개수와, 요청 높이
items = list(map(int, input().split())) # N개의 떡 높이들
H = max(items)-1 # init H

while True:
    total = 0
    for i in items:
        res = i-H
        if res>0:
            total+=res
    if total>=M:
        break
    else:
        H-=1

print(H)

# H보다 더 큰 element들을 선별해서 진행해도되지만,
# 비교연산과 산술연산은 똑같은 계산 복잡도를 가지므로 굳이 진행하지 않았음.