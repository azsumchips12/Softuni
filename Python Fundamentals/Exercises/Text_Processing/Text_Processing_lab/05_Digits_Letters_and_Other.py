word = input()
while word != 'end':
    print(f"{word[::]} = {word[::-1]}")
    word = input()
    data = input()
print("".join(x for x in data if x.isdigit()))
print("".join(x for x in data if x.isalpha()))
print("".join(x for x in data if not x.isalpha() and not x.isdigit()))