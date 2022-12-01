def solution(n):
    num = 0
    
    for i in range(n+1):
        if i % 2 == 0:
            num += i
    return num
