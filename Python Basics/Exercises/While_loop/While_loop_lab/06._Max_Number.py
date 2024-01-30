n = input()

max_number = -100000000000

while n != 'Stop':
    num = int(n)

    if num > max_number:
        max_number = num
    n = input()

print(max_number)