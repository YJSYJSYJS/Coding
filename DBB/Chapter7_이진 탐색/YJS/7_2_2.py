'''
time: 2sec -> 4000만 연산
mem: 128MB -> 128*1024*1024/4 개의 데이터(int 기준) ~ 약 3300만개의 int
input:
 - N(1~1000000), M(1~2000000000)
 - 떡 높이(0~1,000,000,000)
output:
 - 절단기 최대높이(H)
'''
N, M = map(int, input().split()) # 떡 개수와, 요청 높이
items = list(map(int, input().split())) # N개의 떡 높이들
items.sort(reverse=True) # NlogN(k*100만)
# 요청 높이를 N으로 나누면, 한 떡에서 잘리는 평균 길이
E = M//N
# 떡의 길이가 균일하다고 가정하고, 해당 평균길이를 H의 초기값으로
meanH = (max(items)+min(items))//2 # 최대 400만 연산
H = meanH-E
H_ascending = False
while True:
    total = 0 # 손님이 가져갈 떡의 길이 초기화
    for i in items:
        res = i-H # 해당 떡에서 손님이 가져갈 부분
        if res<0: # items가 내림차순 정렬되어 있기 때문에, stop condition
            break
        total+=res # stop condition에 해당되지 않으면, 총가져갈 길이 update
    # H update
    # 현재 H에 대해서 iteration 후 total과 M을 비교
    if total>=M: # M 이상일 경우 늘려보기
        H+=1
        H_ascending = True
        # total<M 이였다가 처음 진입 시,  print하면 답
        # 해당 조건을 원래 성립하고 있었을 경우, 
        # else 부분과 번갈아가면서 무한루프(ex: 15,16,15,16,...)
    else: # M보다 작을 경우, H의 길이를 1 낮춤
        H-=1
        if H_ascending:
            break 
        # 얼마나 낮출 지에 대해서도 adaptive하게 정할 수 있으면 좋겠지만,
        # dataset이 많을 경우(최악, 100만) 1 낮추는 것만으로 
        # 최대 100만의 길이 변화가 생길 수 있기 때문에,
        # 최소량을 감소시켜도 상관없을 듯
    if H<0 or H>max(items): # 해당 높이의 떡을 맞춰 줄 수 없는 경우
        H = 'Impossible'
        break
print(H)