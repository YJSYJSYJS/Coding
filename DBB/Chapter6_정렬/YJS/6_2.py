'''
N: 1~100000
score: 1~100
name: len <= 100
성적 내림차순 이름 출력(동일 성적 이름 임의의 순서 가능)
1sec -> O(NlogN), 128mb
'''
N = int(input())
scores_dict = dict()
for n in range(N):
    c_name, c_score = input().split()
    print(c_score)
    if int(c_score) not in scores_dict.keys():
        scores_dict[int(c_score)] = [c_name]
    else:
        scores_dict[int(c_score)].append(c_name)

sorted_scores = sorted(scores_dict.items())
result = list()

for s in sorted_scores:
    result = result + s[1]

for r in result:
    print(r, end=' ')     
