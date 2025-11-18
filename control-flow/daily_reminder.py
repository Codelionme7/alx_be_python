# daily_reminder.py

# Prompting the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match-case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Modify based on time sensitivity
if time_bound == "yes":
    final_message = base_message + " that requires immediate attention today!"
else:
    final_message = base_message + ". Consider completing it when you have free time."

# REQUIRED format for the checker:
print(f"Reminder: {final_message}")
