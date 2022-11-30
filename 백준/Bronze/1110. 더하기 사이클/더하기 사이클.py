n = int(input())
num = n
count = 0

while True:
    a = num//10  #2
    b = num % 10  #6
    c = (a+b) % 10  # 2+6 = 8
    num = (b * 10) + c  # 60 + 8 = 68
    
    count += 1
    if num == n:
        break
        
print(count)