n = int(input())
word = input()
lists = []

for i in range(n):
    current_text = input()
    lists.append(current_text)
print(lists)

for i in range(len(lists) - 1, -1, -1):
    element = lists[i]
    if word not in element:
        lists.remove(element)
print(lists)
