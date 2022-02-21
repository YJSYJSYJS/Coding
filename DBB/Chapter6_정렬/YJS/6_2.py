'''
N: 1~100000
score: 1~100
name: len <= 100
성적 내림차순 이름 출력(동일 성적 이름 임의의 순서 가능)
'''
N = int(input())
scores = [i for i in range(100,0,-1)]
scores_dict = dict.fromkeys(scores, [])

for n in range(N):
    c_name, c_score = input().split()
    scores_dict[int(c_score)].append(c_name)
print(scores_dict)
result = list()

for i in range(100,0,-1):
    curr_names = scores_dict[i]
    if len(curr_names)==0:
        continue
    else:
        result = result + curr_names

for r in result:
    print(r, end=' ')     