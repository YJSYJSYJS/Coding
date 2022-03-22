'''
time: 2sec -> 4000만 연산
mem: 128MB -> 128*1024*1024/4 개의 데이터(int 기준) ~ 약 3300만개의 int
input:
 - N(1~1000000), M(1~2000000000)
 - 떡 높이(0~1,000,000,000)
output:
 - 절단기 높이(H)
'''
N, M = map(int, input().split()) # 떡 개수와, 요청 높이
items = list(map(int, input().split())) # N개의 떡 높이들
H = max(items)-1 # init H
mid = (max(items)+min(items))//2 # 최대 200만 연산

# while True:
#     total = 0
#     for i in items:
#         res = i-H
#         if res>0:
#             total+=res
#     if total>=M:
#         break
#     else:
#         H-=1

# print(H)