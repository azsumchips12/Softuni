num = int(input())

even_nums = 0
odd_nums = 0

for loop_index in range(num):
    loop_num = int(input())
    if loop_index % 2 == 0:
        even_nums += loop_num
    else:
        odd_nums += loop_num

if even_nums == odd_nums:
    print(f'Yes\nSum = {even_nums}')
else:
    diff = abs(even_nums - odd_nums)
    print(f'No\nDiff = {diff}')