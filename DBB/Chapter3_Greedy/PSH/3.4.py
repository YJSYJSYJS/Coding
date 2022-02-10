n, k = map(int,input().split())
count = 0

while n>=k:
  if n % k == 0:
    n = n // k
    count += 1
  
  n -= 1
  count +=1

print(count)

# 단순하게 생각한 idea
# 마지막으로 남은 수에 대하여 1씩 빼기를 생각하지 않음
# ex) n이 2가 되었는데 k가 3일 경우
# 답안에 있는 target 써써 하는 코드 확인하기! while문이 1번 돌때마다 무조건 / 연산을 해주므로 N 이 엄청 클 경우 빠르게 감소하고 log 시간 복잡도로 나옴