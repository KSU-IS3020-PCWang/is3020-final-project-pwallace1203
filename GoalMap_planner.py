print("Welcome to the Goal Map!")

profile = {}
goals = []

def display():
    print("\n=== GoalMap ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Add Goal")
    print("4. View Goals")
    print("5. Update Goal Status")
    print("6. View Goal Progress")
    print("7. Save Goals")
    print("8. Load Goals")
    print("9. Exit")

def create_account():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    password = input("Please create password: ")
    confirm_password = input("Please confirm password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return False

    profile["name"] = name
    profile["email"] = email
    profile["password"] = password

    print("Account Created Successfully!")
    return None


def login():
    if len(profile) == 0:
        print("Please create an account")
        return False

    email = input("Please enter your email: ")
    password = input("Please enter password: ")

    if email == profile["email"] and password == profile["password"]:
        print("Login Successful!")
        return True

    print("Invalid email or password.")
    return False

def add_goal():
    goal_title = input("Enter your goal: ")
    category = input("Enter goal category (School, Personal, Career, Health, Financial): ")
    due_date = input("Enter target date (MM/DD/YYYY): ")
    goal = {
        "title": goal_title,
        "category": category,
        "due_date": due_date,
        "status": "Not Started"
    }
    goals.append(goal)
    print("Goal Added Successfully!")

def main():
    while True:
        display()
        choice = input("Please select your option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            add_goal()

        elif choice == "4":
            view_goals()

        elif choice == "5":
            update_goal()

        elif choice == "6":
            view_goal_progress()

        elif choice == "7":
            save_goals()

        elif choice == "8":
            load_goals()

        elif choice == "9":
            print("Thank you for using GoalMap!")
            break

        else:
            print("Invalid  option. Please select from 1 through 9.")

def view_goals():
    if len(goals) == 0:
        print("No Goals Available!")
        return

    print("\n== Your Goals ==")

    for index, goal in enumerate(goals, start=1):
        print(f"\nGoal {index}")
        print(f"Title:, {goal['title']}")
        print(f"Category:, {goal['category']}")
        print(f"Due Date:, {goal['due_date']}")
        print(f"Status:, {goal['status']}")

def update_goal():
    if len(goals) == 0:
        print("No Goals Available!")
        return

    print("\n== Your Goals ==")

    for index, goal in enumerate(goals, start=1):
        print(f"\nGoal {index}")
        print(f"Title: {goal['title']}")
        print(f"Category: {goal['category']}")
        print(f"Due Date: {goal['due_date']}")
        print(f"Status: {goal['status']}")

    goal_number = int(input("Please select your goal number: "))
    if goal_number < 1 or goal_number > len(goals):
        print("Invalid goal number!")
        return

    print("\nChoose a new status:")
    print("1. Not Started")
    print("2. In Progress")
    print("3. Completed")

    status_choice = input("Please select your option: ")
    if status_choice == "1":
        goals[goal_number-1]["status"] = "Not Started"
    elif status_choice == "2":
        goals[goal_number-1]["status"] = "In Progress"
    elif status_choice == "3":
        goals[goal_number-1]["status"] = "Completed"
    else:
        print("Invalid option!")

    print("Goal Updated Successfully!")

def view_goal_progress():
    if len(goals) == 0:
        print("No Goals Available!")
        return

    print("\n== Goal Progress ==")

    print("\nNot started:")
    for goal in goals:
        if goal ["status"] == "Not Started":
            print(f"- {goal['title']}")
    print(f"\nIn Progress:")
    for goal in goals:
        if goal["status"] == "In Progress":
            print(f"- {goal['title']}")
    print(f"\nCompleted:")
    for goal in goals:
        if goal["status"] == "Completed":
            print(f"- {goal['title']}")

def save_goals():
    if len(goals) == 0:
        print("No Goals Available!")
        return

    file = open("goals.csv", "w")

    for goal in goals:
        file.write(goal["title"] + ","+
                   goal["category"] + "," +
                   goal["due_date"] + "," +
                   goal["status"] + "\n"
                   )
    file.close()
    print("Goals Saved Successfully!")

def load_goals():
    goals.clear()

    try:
        file = open("goals.csv", "r")

        for line in file:
            data = line.strip().split(",")

        goal = {
            "title": data[0],
            "category": data[1],
            "due_date": data[2],
            "status": data[3],
        }
        goals.append(goal)
        file.close()
        print("Goals Loaded Successfully!")

    except FileNotFoundError:
        print("No saved goals file was found.")

main()

