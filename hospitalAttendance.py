""" Scenario: Create a system that takes track of staff attendance at a local hospital when ever they sign in to work. The program should be able to:
    1. Take employee attendance and send it to a file for database
        * Create password for employee login
        * keep track employee passwords in a database to check for input invalidation
        * lock user out of system if menu options if not equal to correct choice
    2. Mark calendar for when employees are off 
        * Highlight days for employees with colors like red or green to tell if a employee reported to work or not
        * Keep track of how many hours the employees worked during those days
        * Show the name of the employee that worked that day.
    3. Announce when there will be days off and employee bonuses.
        * one of the menu options will display certain days on which there will be bonuses and also showing when workers can take a day off 
"""
# Constants & Variables
TAKE_ATTENDANCE = "1"
MARK_CALENDER = "2"
EXTRACURRICULARS = "3"
QUIT_MENU = "4"

# Create function to format title header for each section
def createTitleHeader(tabHeader):
    # Center header by 70 pixels
    centerHeader = tabHeader.center(100)

    # Convert header into a f string and underline for header sections
    print(centerHeader)

    # Create a whitespace for title header to organize better
    print()

# Create function to house main body of program
def main():

# Set menu option for drive menu to zero
    drive_menu_option = 0

# Create intro
    createTitleHeader(tabHeader = "\033[1;4mMemorial Hospital Employee Login\033[0m")

# Create drive menu
    while drive_menu_option != QUIT_MENU:
        # Create options for menu
        print("\nChoose One Of The Following Options:")
        print("\t1. Take Employee Attendance.")
        print("\t2. Mark Worker Calendar.")
        print("\t3. Employee Bonuses And News.")
        print("\t4. Log Off.")
        drive_menu_option = input("Please Choose An Option: ")

        # Create tabs for menu choices
        if drive_menu_option == TAKE_ATTENDANCE:
            # Create title header for section
            createTitleHeader(tabHeader = "\033[1;4mEmployee Attendance\033[0m")

            # Create password system for user to enter to access worker interface
            

        elif drive_menu_option == MARK_CALENDER:
            # Create title header for section
            createTitleHeader(tabHeader = "\033[1;4mEmployee Calendar\033[0m")

        elif drive_menu_option == EXTRACURRICULARS:
            # Create title header for section
            createTitleHeader(tabHeader = "\033[1;4mEmployee News And Benefits\033[0m")

        elif drive_menu_option == QUIT_MENU:
            # Creating good bye message when user is done with program
            print("Logging Off. Good Bye")
            print()
        else:
            print("Error ... User Input Is Incorrect!!! Choose Options (1-4).") 

main()