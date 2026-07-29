import csv
from datetime import datetime

print("Welcome to the Goal Map!")

profile = {}
goals = []
logged_in = False


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
    name = input("Please enter your name: ").strip()
    email = input("Please enter your email: ").strip().lower()

    if name == "" or email == "":
        print("Name and email cannot be blank.")
        return False

    if "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        return False

    password = input("Please create a password: ")
    confirm_password = input("Please confirm your password: ")

    if len(password) < 4:
        print("Password must contain at least four characters.")
        return False

    if password != confirm_password:
        print("Passwords do not match!")
        return False

    profile["name"] = name
    profile["email"] = email
    profile["password"] = password

    print(f"Account created successfully for {name}!")
    return True


def login():
    global logged_in

    if len(profile) == 0:
        print("Please create an account first.")
        return False

    email = input("Please enter your email: ").strip().lower()
    password = input("Please enter your password: ")

    if email == profile["email"] and password == profile["password"]:
        logged_in = True
        print(f"Login successful! Welcome, {profile['name']}!")
        return True

    print("Invalid email or password.")
    return False


def check_login():
    if not logged_in:
        print("Please log in before using this feature.")
        return False

    return True


def get_category():
    categories = ["School", "Personal", "Career", "Health", "Financial"]

    print("\nGoal Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    category_choice = input("Please select a category: ")

    try:
        category_number = int(category_choice)

        if 1 <= category_number <= len(categories):
            return categories[category_number - 1]

        print("Invalid category number.")

    except ValueError:
        print("Please enter a number.")

    return None


def get_due_date():
    due_date = input("Enter target date (MM/DD/YYYY): ").strip()

    try:
        datetime.strptime(due_date, "%m/%d/%Y")
        return due_date

    except ValueError:
        print("Invalid date. Please use MM/DD/YYYY.")
        return None


def add_goal():
    if not check_login():
        return

    goal_title = input("Enter your goal: ").strip()

    if goal_title == "":
        print("Goal title cannot be blank.")
        return

    category = get_category()

    if category is None:
        return

    due_date = get_due_date()

    if due_date is None:
        return

    goal = {
        "title": goal_title,
        "category": category,
        "due_date": due_date,
        "status": "Not Started"
    }

    goals.append(goal)
    print("Goal added successfully!")


def view_goals():
    if not check_login():
        return

    if len(goals) == 0:
        print("No goals available!")
        return

    print("\n== Your Goals ==")

    for index, goal in enumerate(goals, start=1):
        print(f"\nGoal {index}")
        print(f"Title: {goal['title']}")
        print(f"Category: {goal['category']}")
        print(f"Due Date: {goal['due_date']}")
        print(f"Status: {goal['status']}")


def update_goal():
    if not check_login():
        return

    if len(goals) == 0:
        print("No goals available!")
        return

    view_goals()

    try:
        goal_number = int(
            input("\nPlease select the goal number you want to update: ")
        )

        if goal_number < 1 or goal_number > len(goals):
            print("Invalid goal number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nChoose a new status:")
    print("1. Not Started")
    print("2. In Progress")
    print("3. Completed")

    status_choice = input("Please select your option: ")

    if status_choice == "1":
        new_status = "Not Started"
    elif status_choice == "2":
        new_status = "In Progress"
    elif status_choice == "3":
        new_status = "Completed"
    else:
        print("Invalid status option!")
        return

    goals[goal_number - 1]["status"] = new_status
    print("Goal updated successfully!")


def view_goal_progress():
    if not check_login():
        return

    if len(goals) == 0:
        print("No goals available!")
        return

    statuses = ["Not Started", "In Progress", "Completed"]

    print("\n== Goal Progress ==")

    for status in statuses:
        matching_goals = []

        for goal in goals:
            if goal["status"] == status:
                matching_goals.append(goal)

        print(f"\n{status} ({len(matching_goals)}):")

        if len(matching_goals) == 0:
            print("- No goals")
        else:
            for goal in matching_goals:
                print(f"- {goal['title']}")

    completed_count = 0

    for goal in goals:
        if goal["status"] == "Completed":
            completed_count += 1

    progress_percentage = completed_count / len(goals) * 100

    print(
        f"\nOverall Progress: "
        f"{completed_count} of {len(goals)} goals completed "
        f"({progress_percentage:.0f}%)"
    )


def save_goals():
    if not check_login():
        return

    if len(goals) == 0:
        print("No goals available!")
        return

    try:
        with open("goals.csv", "w", newline="") as file:
            field_names = ["title", "category", "due_date", "status"]

            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(goals)

        print("Goals saved successfully!")

    except OSError:
        print("An error occurred while saving the goals.")


def load_goals():
    if not check_login():
        return

    try:
        with open("goals.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            loaded_goals = []

            for row in reader:
                if all(
                    field in row
                    for field in ["title", "category", "due_date", "status"]
                ):
                    loaded_goals.append({
                        "title": row["title"],
                        "category": row["category"],
                        "due_date": row["due_date"],
                        "status": row["status"]
                    })

        goals.clear()
        goals.extend(loaded_goals)

        print(f"{len(goals)} goal(s) loaded successfully!")

    except FileNotFoundError:
        print("No saved goals file was found.")

    except (OSError, csv.Error):
        print("The goals file could not be read.")


def main():
    while True:
        display()
        choice = input("Please select your option: ").strip()

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
            print("Invalid option. Please select a number from 1 through 9.")


main()