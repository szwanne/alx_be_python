task = input("What is the task description?")
priority = input("Task's priority (high, medium, low):")
time_bound = input("Is it time-bound? (yes or no):")

# if priority == "high":
#     if time_bound == "yes":
#         print(
#             f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
#     else:
#         print(
#             f"Note: {task} {priority} priority task. Consider completing it when you have free time.")
# if priority == "Medium":
#     if time_bound == "yes":
#         print(
#             f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
#     else:
#         print(
#             f"Note: {task} {priority} priority task. Consider completing it when you have free time.")
# if priority == "low":
#     if time_bound == "yes":
#         print(
#             f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
#     else:
#         print(
#             f"Note: {task} {priority} priority task. Consider completing it when you have free time.")


match priority.lower():
    case "high" | "medium" | "low":
        if time_bound.lower() == "yes":
            print(
                f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(
                f"Note: {task} {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority level.")
