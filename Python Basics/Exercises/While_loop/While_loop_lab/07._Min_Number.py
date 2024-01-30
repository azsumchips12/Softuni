n = input()

min_number = 100000000000

while n != 'Stop':
    num = int(n)

    if num < min_number:
        min_number = num
    n = input()

print(min_number)