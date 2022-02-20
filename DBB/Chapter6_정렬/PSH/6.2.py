n = int(input())

# 2차원 리스트로 할까 했는데 이 과정이 조금 귀찮아서...그냥 리스트 안에 튜플로 함

array = []
for i in range(n):
  data = input().split()
  array.append((data[0],int(data[1])))

# 파이썬 튜플 정렬 찾아보기
array.sort(key=lambda x: x[1])

for x in array:
  print(x[0], end=' ')

