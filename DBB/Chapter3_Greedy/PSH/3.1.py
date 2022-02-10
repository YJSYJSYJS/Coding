N = 1260
count = 0
coin = [500, 100, 50, 10]

for c in coin:
    count += N // c
    N = N % c

print(count)

# 복잡하게 계산 했었지만 python 사칙연산을 다시 공부하면 // 이랑 %이라는 기호로 쉽고 간단하게코드를 짤 수 있음
