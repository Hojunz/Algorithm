def solution(n, k):
    r = n // 10
    if k <= r:
        return 12000*n
    return 12000*n + 2000*(k-r)
