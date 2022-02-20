# 선택정렬

n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

for i in range(len(array)):
  max_index = i
  for j in range(i+1, len(array)):
    if array[max_index] < array[j]:
      max_index = j
  
  array[i], array[max_index] = array[max_index] , array[i]

print(array)