def solution(x, n):
#   x + x*n
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer