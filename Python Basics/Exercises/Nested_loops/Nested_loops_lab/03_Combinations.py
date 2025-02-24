n = int(input())
combination_counter = 0
for first_num in range (0, n + 1):
    for second_num in range (0, n + 1):
        for third_num in range(0, n + 1):
            if first_num + second_num + third_num == n:
                combination_counter += 1
print(combination_counter)