text = input()
balance = 0.0
while text != 'NoMoreMoney':
    amount = float(text)
    if amount < 0:
        print('Invalid operation!')
        break

    balance += amount
    print(f'Increase: {amount:.2f}')
    text = input()

print(f'Total: {balance:.2f}')