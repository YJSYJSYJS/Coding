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
# 최악의 경우라면, 문제가 될 수 있음.
# 떡의 개수가 백만개, 요청한 떡의 길이가 20억인 경우
# 백만개의 떡의 길이가 모두 2000이라면,
# 절단기의 높이는 0이어야 요청한 떡의 길이를 만족한다.
# 이 때, H의 초기값은 1999, 100만의 iteration을 2000번 진행하므로
# 200억의 iteration이 진행되며, 총 연산횟수는 600억.
# 시간제한 2초와 메모리 제한 128MB
# 파이썬은 초당 대략 2000만번의 연산 가능
# 2초 동안 4000만번의 연산 이내로 진행해야함!
# 요구 연산량은 15배