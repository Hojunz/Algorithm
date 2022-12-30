def solution(numbers):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result = 0
    for i in numbers:
        if i in arr:
            result += i
            # numbers.remove(i)
        else: 
            continue
    return 45 - result
        