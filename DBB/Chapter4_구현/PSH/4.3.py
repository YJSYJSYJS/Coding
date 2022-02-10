# ex) a1 문자 a를 숫자로 표현하는 방법이 뭐가 있을까? -> 아스키코드

data = input()
row = int(data[1])
# print(ord(data[0])) 아스키코드 a:97, h:104
column = int(ord(data[0])) - 96

# 앞에서 했던 것 처럼 경우의 수를 리스트로 표현
step = [[2,-1],[2,1],[-2,1],[-2,-1],[1,-2],[1,2],[-1,2],[-1,-2]]

result = 0

for s in step:
  next_r = row + s[0]
  netx_c = column + s[1]

  # and가 좋을까 or이 좋을까?
  if next_r >= 1 and next_r <= 8 and netx_c >=1 and netx_c <=8:
    result +=1

print(result)

