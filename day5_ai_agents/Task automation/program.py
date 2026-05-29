# task_automation.py

def send_email(to, subject):
    return f"Email sent to {to} with subject '{subject}'"


def create_report(topic):
    return f"Report created for topic: {topic}"


def automate_task(user_request):

    request = user_request.lower()

    if "email" in request:
        return send_email(
            "manager@company.com",
            "Daily Update"
        )

    elif "report" in request:
        return create_report("Sales Analysis")

    else:
        return "Task not recognized"


# User Input
task = input("Enter task: ")

# Run Automation
result = automate_task(task)

print("\nAutomation Result:")
print(result)