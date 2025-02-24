import math
name_serial = input()
one_episode = int(input())
rest = int(input())

lunch = rest / 8
rest_time = rest / 4
time_left = rest - lunch - rest_time
diff = abs(time_left - one_episode)
rounded_diff = math.ceil(diff)

if time_left >= one_episode:
    print(f'You have enough time to watch {name_serial} and left with {rounded_diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {rounded_diff} more minutes.")