number_lines = int(input())
total_sum = 0
for number in range(number_lines):
    char = input()
    total_sum += ord(char)
print(f"The sum equals: {total_sum}")