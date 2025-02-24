divisior = int(input())
boundary = int(input())
current_num = boundary

for curr_num in range(boundary, divisior, - 1):
    if 0 < current_num <= boundary and current_num % divisior == 0:
        print(current_num)
        break
    current_num -= 1