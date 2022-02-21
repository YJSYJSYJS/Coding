'''
N: 1~500
N integers: 1~100000
내림차순 정렬, 1sec, 128mb
O(N^3)까지 가능(N의 크기 500)
'''

N = int(input())
arr = list()
for i in range(N):
    arr.append(int(input()))


def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[0]
    rest = arr[1:]

    l = [x for x in rest if x>pivot]
    r = [x for x in rest if x<=pivot]

    return quick_sort(l) + [pivot] + quick_sort(r)

result = quick_sort(arr)

for r in result:
    print(r, end=' ')
