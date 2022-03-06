# 순차 탐색
# 순서대로 탐색
def sequential_search(target, arr):
    for i in range(len(arr)):
        if arr[i]==target:
            return i

# 이진 탐색(재귀)
def bin_search(arr, target, start, end):
    if start>end:
        return None
    mid = (start + end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return bin_search(arr, target, mid+1, end)
    else:
        return bin_search(arr, target, start, mid-1)

# 이진 탐색(반복)
def bin_search_(arr, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 빠른 입력
'''
import sys
input_data = sys.stdin.readline().rstrip()
# rstrip으로 마지막 공백문자 제거
# 부록에 좀 더 효율적인 방법 공개(아직 못 찾음)
'''