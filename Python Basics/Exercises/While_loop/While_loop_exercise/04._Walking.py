sum_steps = 0
goal_steps = 10000
text = input()
while text != 'Going home':
    steps = int(text)
    sum_steps += steps

    if sum_steps >= goal_steps:
        break

    text = input()

if text == 'Going home':
    steps_dom = int(input())
    sum_steps += steps_dom

difeti = abs(goal_steps - sum_steps)
if sum_steps >= goal_steps:
    print('Goal reached! Good job!')
    print(f'{difeti} steps over the goal!')
else:
    print(f'{difeti} more steps to reach goal.')