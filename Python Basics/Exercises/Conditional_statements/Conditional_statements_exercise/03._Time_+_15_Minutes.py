time = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    minutes -= 60
    time += 1

if time >= 24:
    time -= 24

if minutes < 10:
    print(f"{time}:0{minutes}")
else:
    print(f"{time}:{minutes}")