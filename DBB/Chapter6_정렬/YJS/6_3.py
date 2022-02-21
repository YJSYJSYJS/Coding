'''
2sec, 128MB
N, K: 1~100000, 0~N
A: a<10000000, int
B: b<10000000, int
'''
N, K = list(map(int,input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for k in range(K):
    if A[k]<B[k]:
        A[k]=B[k]

print(sum(A))