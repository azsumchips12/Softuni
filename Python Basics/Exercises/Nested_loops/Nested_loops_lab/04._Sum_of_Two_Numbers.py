start = int(input())
end = int(input())
magic_number = int(input())
combination_counter = 0
break_condition = False
for first_num in range(start, end + 1):
    for second_num in range(start, end + 1):

        combination_counter += 1

        if first_num + second_num == magic_number:
            print(f"Combination N:{combination_counter} ({first_num} + {second_num} = {magic_number})")
            break_condition = True
            break

    if break_condition:
        break


else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
