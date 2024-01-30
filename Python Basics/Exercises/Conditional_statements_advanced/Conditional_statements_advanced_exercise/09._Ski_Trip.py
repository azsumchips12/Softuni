days_to_stay = int(input())  # дни за престой - цяло число
room = input()  # вид помещение - "room for one person", "apartment" или "president apartment"
grade = input()  # оценка за обслужване - "positive" или "negative".

amount_for_nights = 0
submit = 0

if room == 'room for one person':
    amount_for_nights = 18 * (days_to_stay-1)
    submit = amount_for_nights
elif room == 'apartment':
    amount_for_nights = 25 * (days_to_stay-1)
    if days_to_stay < 10:
        submit = amount_for_nights * 0.7
    elif 10 <= days_to_stay <= 15:
        submit = amount_for_nights * 0.65
    elif days_to_stay > 15:
        submit = amount_for_nights * 0.5
elif room == 'president apartment':
    amount_for_nights = 35 * (days_to_stay-1)
    if days_to_stay < 10:
        submit = amount_for_nights * 0.9
    elif 10 <= days_to_stay <= 15:
        submit = amount_for_nights * 0.85
    elif days_to_stay > 15:
        submit = amount_for_nights * 0.8

total_price = 0

if grade == 'positive':
    total_price = submit * 1.25
elif grade == 'negative':
    total_price = submit * 0.9

print(f'{total_price:.2f}')