type_of_flower = input()
number_of_flower = int(input())
budget = int(input())
total_sum = 0

if type_of_flower == "Roses":
    total_sum = 5 * number_of_flower
    if number_of_flower > 80:
        total_sum = total_sum * 0.9
elif type_of_flower == "Dahlias":
    total_sum = 3.80 * number_of_flower
    if number_of_flower > 90:
        total_sum = total_sum * 0.85
elif type_of_flower == "Tulips":
    total_sum = 2.80 * number_of_flower
    if number_of_flower > 80:
        total_sum = total_sum * 0.85
elif type_of_flower == "Narcissus":
    total_sum = 3 * number_of_flower
    if number_of_flower < 120:
        total_sum = total_sum * 1.15
elif type_of_flower == "Gladiolus":
    total_sum = 2.50 * number_of_flower
    if number_of_flower < 80:
        total_sum = total_sum * 1.20
diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f'Hey, you have a great garden with {number_of_flower} {type_of_flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
