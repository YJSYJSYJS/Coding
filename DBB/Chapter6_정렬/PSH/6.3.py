# n은 배열의 개수 , k는 교환 횟수

n, k = map(int, input().split())
a = list(map(int , input().split()))
b = list(map(int, input().split()))

# 정렬을 해주고 인덱스 차례대로 비교해주기??
a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    temp = a[i]
    a[i] = b[i]
    b[i] = temp
  else:
    break

sum_list = sum(a)
print(sum_list)
