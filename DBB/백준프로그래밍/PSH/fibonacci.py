# 1일때는 1 0일때는 0이니까 그대로
# 2번째부터는 바로 앞에 두항의 합

def fibonacci(n):
  result = 0
  if n <= 1:
    return n
  result = fibonacci(n-1) + fibonacci(n-2)
  return result

n = int(input())
print(fibonacci(n))