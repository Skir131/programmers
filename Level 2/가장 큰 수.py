def sort(a):
    # 퀵소트 방식으로 문제 해결
    if not a:
        return []
    pivot = a[0]
    # 비교 조건 예 : 6, 10에 대하여 610, 106을 비교하고 610이 앞으로 오도록 한다. 
    return sort([i for i in a[1:] if i+pivot > pivot+i]) + [pivot] + sort([i for i in a[1:] if i+pivot <= pivot + i])
    
                    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sort(numbers)
    return str(int("".join((numbers))))