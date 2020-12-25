def sort(a):
    if not a:
        return []
    pivot = a[0]
    return sort([i for i in a[1:] if i+pivot > pivot+i]) + [pivot] + sort([i for i in a[1:] if i+pivot <= pivot + i])
    
_ = input()
numbers = list(map(str, input().split()))
result = sort(numbers)
print(str(int("".join((numbers)))))