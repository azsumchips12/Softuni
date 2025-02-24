import re

data = input()
furnitures = []
total_result = 0

while data != "Purchase":
    match = re.match(r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)", data)

    if match:
        furnitures.append(match['furniture'])
        total_result += float(match['price']) * int(match['quantity'])

    data = input()

print("Bought furniture:")
if furnitures:
    print(*furnitures, sep='\n')
print(f"Total money spend: {total_result:.2f}")
