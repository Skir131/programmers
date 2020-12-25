def sort(a):
    if not a:
        return []
    pivot = a[0]
    return sort([i for i in a[1:] if i+pivot > pivot+i]) + [pivot] + sort([i for i in a[1:] if i+pivot <= pivot + i])
    
                    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sort(numbers)
    return str(int("".join((numbers))))