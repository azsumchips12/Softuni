import math
from math import ceil

people = int(input())
elevator_space = int(input())

courses = math.ceil(people/elevator_space)
print(courses)
