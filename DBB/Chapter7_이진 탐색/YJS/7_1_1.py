'''
time: 1sec
mem: 128MB
input:
 - N(1~1000000)
 - N ints
 - M(1~100000)
 - M ints
output:
 - print: yes or no for each m
'''
N = int(input())
total = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

result = list()
for t in targets:
    if t in total:
        print('yes', end=' ')
    else:
        print('no', end=' ')


