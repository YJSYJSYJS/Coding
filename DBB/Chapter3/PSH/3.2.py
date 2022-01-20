n, m, k = map(int,input().split()) # n = 배열의 크기, m = 더해지는 횟수, k = 횟수 제한

data = list(map(int,input().split()))

# 큰 수 두개를 찾기...
# 리스트 정렬하고 뽑기 or Max 뽑고 그 값 list에서 빼주고 다시 max 뽑기

data.sort(reverse = True)
first = data[0]
second = data[1]
result = 0
number = 0
# 6을 3번 더하고 5를 1번 더하고 6을 3번 더하고 5를 1번 더하기?
for i in range(m):
    if number==k:
      number = 0
      result += second
    else:
      number += 1
      result += first


print(result)

