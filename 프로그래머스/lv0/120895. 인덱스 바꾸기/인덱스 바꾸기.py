def solution(my_string, num1, num2):
    answer = ''
    aaa = list(my_string)
    aaa[num1], aaa[num2] = aaa[num2], aaa[num1]
    return answer.join(aaa)

