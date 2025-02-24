num = int(input())

first_number = 0
second_number = 0

for loop_index in range(0, num * 2):
    loop_num = int(input())
    if loop_index < num:
        first_number += loop_num
    elif loop_index >= num:
        second_number += loop_num

if first_number == second_number:
    print(f'Yes, sum = {first_number}')
else:
    diff_nums = abs(first_number - second_number)
    print(f'No, diff = {diff_nums}')