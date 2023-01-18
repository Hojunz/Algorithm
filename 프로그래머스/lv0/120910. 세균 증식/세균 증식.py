def solution(n, t):
    for i in range(t):
        n *= 2
    return n
    
#     def solution(n, t):
#     return n << t

#     *** 비트연산자 풀이 ***
    
#     <<	비트 왼쪽 시프트	a << b	a의 비트를 b번 왼쪽으로 이동시킴
#     >>	비트 오르쪽 시프트	a >> b	a의 비트를 b번 오른쪽으로 이동시킴
