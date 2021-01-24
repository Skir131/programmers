def convert(n, base):
    if n <= 3:
        print(n)
        return "124"[n-1]
    else:
        q, r = divmod(n-1, 3)
        print(q, r)
        return convert(q, 3) + "124"[r]

def solution(n):
    return convert(n, 3)

print(solution(40))

# 1/20 해결