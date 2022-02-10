n, m = map(int,input().split())

result_list = []

for i in range(n):
  number = list(map(int, input().split()))
  result_list.append(min(number))


result = max(result_list)
print(result)

# 문제 이해하는데 오래 걸림
# 숫자 받는 코드 1번째 줄 알고 있기
# List를 만들고 거기서 max를 하는 생각을 함
# list 안에 숫자를 추가하는 데에 있어 append를 안써서 문법 오류가 떴었음
