import sys
number = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(number):
    num = int(input())
    if num < min_number:
        min_number = num
    if num > max_number:
        max_number = num


print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

