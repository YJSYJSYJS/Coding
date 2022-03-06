# 선택정렬: 가장 작은 원소를 선택해서 앞으로 가져옴
# 삽입정렬: 순회시 각 원소들을 적절한 위치에 임시로 삽입
# -  대부분의 경우에 삽입정렬에 효율적인듯 함
# 퀵정렬: 
# - 기준 피벗 선택 후, 
# - 왼쪽에서는 작은 것 탐색, 오른쪽에서부터는 큰 것 탐색, 탐색된 값들 스왑
# - 중앙에 위치한 값과 피벗 스왑
# - 피벗 기준으로 반반 다시 반복
#
def select_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insert_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break


def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[0]
    rest = arr[1:]

    l = [x for x in rest if x<=pivot]
    r = [x for x in rest if x>pivot]

    return quick_sort(l) + [pivot] + quick_sort[r]


def count_sort(arr):
    sorted=list()
    counts = [0]*(max(arr)+1)
    
    for i in range(len(arr)):
        counts[arr[i]]+=1
    
    for i in range(len(counts)):
        for j in range(len(counts[i])):
            sorted.append(i)
    
    return sorted