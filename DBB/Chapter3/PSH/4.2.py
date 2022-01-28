# 문자 하나 입력
# 00시 00분 00초, 문자 변수를 6개로 잡고 하나하나 비교하기 vs 시,분,초로 해도 될까?
# 비교는 for문을 이용

number = int(input())

count = 0

for h in range(number+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s) :
        count += 1


print(count)


# 처음에 for문마다 in문을 썼는데 count가 많이 나와서 이유를 생각해봤는데
# 이런식으로 접근하면 50분 55초를 count1로 해야되는데 count 3으로 계산해서 이런 문제가 있었음
# 이걸 해결하려고 그냥 문자열을 합쳐서 중복을 체크 안하게 하기!