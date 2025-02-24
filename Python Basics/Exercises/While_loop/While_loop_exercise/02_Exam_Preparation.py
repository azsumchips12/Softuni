failed = int(input())
failed_times = 0
solved_problems = 0
all_grades = 0
last_problem = ""
ever_failed = True

while failed_times < failed:
    problem_name = input()
    if problem_name == "Enough":
        ever_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    all_grades += grade
    solved_problems += 1
    last_problem = problem_name
if ever_failed:
    print(f"You need a break, {failed} poor grades.")
else:
    print(f"Average score: {all_grades / solved_problems:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")