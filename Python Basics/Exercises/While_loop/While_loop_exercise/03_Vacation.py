needed_pari = float(input())
money_she_have = float(input())
day_counter = 0
spending_counter = 0

while money_she_have < needed_pari and spending_counter < 5:
    command = input()
    money = float(input())
    day_counter += 1
    if command == 'save':
        money_she_have += money
        spending_counter = 0
    elif command == 'spend':
        money_she_have -= money
        spending_counter += 1
        if money_she_have < 0:
            money_she_have = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(day_counter)

if money_she_have >= needed_pari:
    print(f'You saved the money for {day_counter} days.')
