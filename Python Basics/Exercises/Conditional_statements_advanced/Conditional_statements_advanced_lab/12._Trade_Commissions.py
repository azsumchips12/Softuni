city = input()
sales = float(input())
commission = 0


if city == 'Sofia':
    if sales > 10000:
        commission = 12
    elif sales > 1000:
        commission = 8
    elif sales > 500:
        commission = 7
    elif sales >= 0:
        commission = 5
if city == 'Varna':
    if sales > 10000:
        commission = 13
    elif sales > 1000:
        commission = 10
    elif sales > 500:
        commission = 7.5
    elif sales >= 0:
        commission = 4.5
if city == 'Plovdiv':
    if sales > 10000:
        commission = 14.5
    elif sales > 1000:
        commission = 12
    elif sales > 500:
        commission = 8
    elif sales >= 0:
        commission = 5.5
if commission > 0:
    print(f"{sales * commission / 100:.2f}")
else:
    print("error")
