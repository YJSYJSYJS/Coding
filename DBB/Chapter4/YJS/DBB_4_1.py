# 초당 2000만번의 연산 수행 가정
# 시간 제한 1초, 데이터 수 1--만 -> O(NlogN) 이내의 알고리즘
##  1000000log1000000 ~ 20000000
# 시간 제한과 데이터 개수 우선적으로 확인 필요
N = int(input())
route = list(input().split())
row = 1
col =1
if N==1:
    print(row, col)
else:
    for r in route:
        if r == 'R':
            col += 1
            if col>N:
                col-=1
        elif r == 'L':
            col -= 1
            if col==0:
                col+=1
        elif r == 'U':
            row -= 1
            if row==0:
                row+=1
        else:
            row += 1
            if row>N:
                row-=1
        
    print(row, col)



