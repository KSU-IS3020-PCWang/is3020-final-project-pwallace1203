# IS 3020 Final Project

## Student and Project Information

- Student name: Isabella Wallace
- GitHub username: pwallace1203
- Project title: GoalMap: Goal Management Planner
- Application purpose: GoalMap is a goal management application that helps students organize, track, and manage personal and academic goals.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.
To run this application Python 3.14 (or later version) is required.

Required Files:
GoalMap_planner.py
goals.txt

To Run Application:
1. Clone or Download the repository from GitHub
2. Open in PyCharm (3.14 Version or better)
3. Open GoalMap_planner.py file
4. Click the RUN button (green triangle) or right-click file and select RUN 'GoalMap_Planner'
5. Follow prompts to create account, log-in, add goals, manage goals, save goals, and load goals.
6. Exit


## Major Features

Account creation- Users will be able to create an account by entering their name, email, and password.

User Login- Authenticates users by verifying email and passwords before accessing the application.

Goal Management- Users can add, view, and update goals once an account has been created.
Users will be able to categorize goals, enter due dates, and update goal progress.

Progress Tracking- The application will group goals by current status for users to easily monitor progress.

Data Storage- Users will be able to save goals to text file and load previous goals when returning to application.


## Python Concepts Used

GoalMap uses functions to organize the application into separate tasks. There are 8 features and each feature has it own 
function. These features include the main feature () that controls the menu and will call a function based on the user selection. 
Additional selections includes create_account, login, add goals, view goals, update goals, save goals, and load goals.

The application collects and stores in the form of dictionaries and list. 
Profiles and goals will be stored as dictionaries and then the dictionaries will be stored together inside a goal list.

The application includes the conditionals of if, elif, and else statements. These statements will help make decisions throughout the program.
The application uses a while loop to keep the main menu running until a slection has been made or the user select exiting the application. 

GoalMap wil use the text file goals.csv to save goal information.
## Data File

The application uses a CSSV file, goals.cvs to store goal list. This file will store the user goals by separying goals by commas, with each line representing a one goal. 

## Testing Summary

During testing I tested each function to ensure applciation ran smoothly. Initially application crashed out due to not having the correct break in place. Coding was corrected and was rerun. Each function properly and when an incorrect input was entered the application did not continue. 
## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.
