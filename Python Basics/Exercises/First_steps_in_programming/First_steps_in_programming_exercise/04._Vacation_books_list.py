pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_for_1_book = pages // pages_per_hour
day = time_for_1_book // days
print(day)