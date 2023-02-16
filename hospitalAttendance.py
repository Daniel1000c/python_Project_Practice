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
PASS_MENU_PROMPT_TRIES = 3
MAX_MENU_TRIES = 2

class mainMenu:
    TAKE_ATTENDANCE = "1"
    MARK_CALENDER = "2"
    EXTRACURRICULARS = "3"
    QUIT_MENU = "4"

# Import random module to randomize employee hours and supervisors on staff
import random

# Import getpass module to hide user passwords
from getpass import getpass

# Import colorama module to change error texts to red to show error clearly
import colorama
from colorama import Fore
colorama.init(autoreset = True)

# Create class to store menu choice functions
class superChoiceMenu:
    SUPERVISOR_ON_CALL = "1"
    SUPERVISOR_HOSPITAL = "2"
    SUPERVISOR_QUIT = "3"    
    
# Create function to format title header for each section
def createTitleHeader(tabHeader):
    # Create newline space so that it makes it easier to read for user
    print()
    
    # Center header by 70 pixels
    centerHeader = tabHeader.center(100)

    # Convert header into a f string and underline for header sections
    print(centerHeader)

    # Create a whitespace for title header to organize better
    print()
    
# Create employee login homepage
def createHomePage():
    print("\nHello world")

# Create supervisor, payhours, and holidays function
def employeeWorkNews():
    # Constants
    class employeeTab:
        SUPERVISOR_TAB = "1"
        PAY_HOURS = "2"
        HOLIDAYS = "3"
        EMPLOYEE_OFF_DAYS ="4"
        QUIT_NEWS_MENU = "5"
    
    # Insert header function for tab
    createTitleHeader( tabHeader = "\033[1;4mWorker's News and Comp\033[0m")

    # Create tuple list for payhours, supervisors, holidays, and offdays
    # Create tuple list for work hours given for week
    workHours = ("10", "20", "30", "40", "50","60")
    
    # Create tuple list for offdays
    workDaysOff = ("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday", "Sunday")
    
    # Create list for holidays 
    workHolidays = ("Christmas","Thanksgiving","President's Day","Three King's Day")
    
    # Create drive menu for user to select employee options
    employeeDriveMenu = 0
    
    # Prompt user with drive menu
    while employeeDriveMenu != employeeTab.QUIT_NEWS_MENU:
        print(Fore.GREEN + "\033[1;4m\t\t\tPlease Enter One Of Following Options\033[0m")
        print("\t\t\t\tSupervisors On The Floor.")
        print("\t\t\t\tEmployee Work Hours.")
        print("\t\t\t\tHolidays.")
        print("\t\t\t\tEmployee Off Days.")
        print("\t\t\t\tExit Menu.")
        employeeNewsMenu = input("\nPlease Choose An Option(1-5): ")
    
        # Create menu options if user inputs one of drive menu options
        if employeeNewsMenu == employeeTab.SUPERVISOR_TAB:
            superVisorMenu = 0
            
            # Create tuple list for supervisors on hand
            #hospital_super_viser = random("George Gomez", "Jennifer Taylor", "Naomi Sakura","Tyler Durden","Brad Pitt" )
            
            # Create title header to signify that user is on supervisor tab
            createTitleHeader(tabHeader = Fore.BLUE + "\033[1;4mMemorial Supervisors\033[0m")
            
            # Create a menu to display supervisors available for each branch and who is on call on hosiptal floor
            while superVisorMenu != superChoiceMenu.SUPERVISOR_QUIT:
               # Prompt user for menu choice
               print("\t\t\t\tSupervisor On Call.") 
               print("\t\t\t\tSupervisor Hospital Location.")
               print("\t\t\t\tRevert To Previous Menu.")
               superVisorMenu = input("\nChoose An Option:")
               
               if superVisorMenu == superChoiceMenu.SUPERVISOR_ON_CALL:
                     # Create tuple list for supervisors on hand
                   hospital_super_viser = ("George Gomez", "Jennifer Taylor", "Naomi Sakura","Tyler Durden","Brad Pitt" )
                   
                   # Create tab header for branch section
                   createTitleHeader(tabHeader = Fore.BLUE + "\033[1;4mSupervisor On Call Today\033[0m")
                   
                   # Create a tuple list randomizer for supervisors on deck
                   supervisorRandomizer = random.choice(hospital_super_viser)
                   
                   # Use randomized list of supervisors to display a different supervisor each time when user logins into tab
                   print(f"The Supervisor On Call Today Is: {supervisorRandomizer}.")
                   
            
            
            
            
        elif employeeNewsMenu == employeeTab.PAY_HOURS:
            print("2") 
        elif employeeNewsMenu == employeeTab.HOLIDAYS:
            print("3")
        elif employeeNewsMenu == employeeTab.EMPLOYEE_OFF_DAYS:
            print("4")
        elif employeeNewsMenu == employeeTab.QUIT_NEWS_MENU:
            # set menu exit prompt to empty string
            menuExitPrompt = ""
            
            # Prompt user to either revert back to main menu or end program
            menuExitPrompt = input("\nPress M To Go Back To Main Menu Or E To End Program: ")
            
            # Create an if statement to branch the two statements
            # Create counter for exit menu prompt 
            exit_menu = 0 
            while menuExitPrompt != "M" or menuExitPrompt != "E": 
                # Reset counter if user picks prompt options
                if menuExitPrompt == "M" or menuExitPrompt == "E":
                    exit_menu = 0
                    
                if menuExitPrompt == "M":
                    # Send user back to main menu
                    main()    
                    
                elif menuExitPrompt == "E":
                    # End program if user picks E
                    exit()   
                    
                else:
                    # Print error message if user input is incorrect
                    print(Fore.RED + "\nError ... Incorrect Input!!!! Must be Either M or E")
                    print() 
                    
                    # Prompt user again if exit prompt is incorrect
                    menuExitPrompt = input("Press M To Go Back To Main Menu Or E To End Program: ")
                    
                    # Increase counter by one if user input is incorrect
                    exit_menu += 1 
                    
                # Print out error message if counter is the same as max menu tries
                if exit_menu == MAX_MENU_TRIES:
                    print(Fore.RED + "\nError ... Invalid User Choice!!! Going back To Previous Menu")
                    employeeWorkNews()
        else:
            # Print error message if user menu option is invalid
            print(Fore.RED + "\nError ... Invalid Input!!!! Must be option (1-5)")
            print()
            
    
    
# Create function for employee login
def employeeLogin():
    # Insert header function for tab section
    createTitleHeader(tabHeader = "\033[1;4mEmployee Attendance\033[0m")
    
    # Create a counter for menu tries
    passwordMenuPromptTry = 0
    
    # Create empty list for employee usernames and password
    loginDatabase = []
    
    # Create while loop to return user to prompt screen to login as new user
    while True and passwordMenuPromptTry < PASS_MENU_PROMPT_TRIES:
        # Prompt user to see if they are registered user or not
        employeeLoginCheckpoint = str(input("Are you Already Registered To This Hospital (Yes/No) Or Enter M To Go To Main Screen: "))
        print()
        
        # Create input invalidation for password prompt menu
        if employeeLoginCheckpoint == "No" and employeeLoginCheckpoint == "Yes" and employeeLoginCheckpoint == "M":
            passwordMenuPromptTry = 0

        if employeeLoginCheckpoint == "No":
            print()
            createTitleHeader(tabHeader = Fore.GREEN + "Employee Register Information")

        # Prompt user for employee name, Id, birthday, occupation
            registerName = str(input("Please Enter Employee Name: "))
            registerBirthday = str(input("Please Enter Birthday: "))
            jobTitle = str(input("Please Enter Job Title: "))
            print()
        
        # Write employee personal info to a file
            fileObject = open("employeeInfoDatabase.txt","a")

        # Add items to file after information is inputed
        # Create newline to separate multiple pieces of employee info
            NEWLINE = "\n"
            fileObject.write(str(registerName))
            fileObject.write('          ')
            fileObject.write(str(registerBirthday))
            fileObject.write('          ')
            fileObject.write(str(jobTitle))
            fileObject.write(NEWLINE)
        
        # Close file 
            fileObject.close()

        # Prompt user for new password and username
            createUsername = str(input("Please Create New Username: "))
            createPassword = str(input("Please Create New Password: "))
            registerWorkerId = str(input("Please Enter Worker Id: "))
            print()
            
        # Append username, password, and worker id to empty list
            loginDatabase.append(createUsername)
            loginDatabase.append(createPassword)
            loginDatabase.append(registerWorkerId)
            loginDatabase.append(NEWLINE)

        elif employeeLoginCheckpoint == "Yes":
            createTitleHeader(tabHeader = Fore.GREEN + "\033[1;4mEmployee Login\033[0m")
            print()
            
            # Prompt user for username, password, and employee id number
            # Create while loop to run user through prompts again if either one is incorrect
            while True:
                #Prompt user for username
                employeeUsername = str(input("\nPlease Enter Username: "))
            
                if employeeUsername == createUsername and createUsername in loginDatabase:
                    # Prompt user for password once username is correct
                    employeePassword = getpass("\nPlease Enter Password: ")
                
                    if employeePassword == createPassword and createPassword in loginDatabase:
                        # Prompt user for worker id once password is correct
                        workerId = str(input("\nPlease Enter Worker Id: "))
                    
                        if workerId == registerWorkerId and registerWorkerId in loginDatabase:
                            # Direct user to login page once all prompts are correct
                            createHomePage()
                            
                            # Break out of loop once on loginpage
                            break
                        
                        else:
                            # Print error message if worker is incorrect
                            print(Fore.RED + "Error ... Worker Id Does Not Exist!!!")
                        
                    else:
                        # Print error message if password is not correct
                        print(Fore.RED + "Error ... Password Does Not Exist")
                        print()
                    
                else:
                    #print error message if username is not correct
                    print(Fore.RED + "Error ... Username Does Not Exist!!!!")

        elif employeeLoginCheckpoint == "M":
        # Call main function to return user back to main menu
            print()
            main()
        
        else:
            print(Fore.RED + "Error ... Invalid Input!!! Has To be Either Yes, No, or M.")
            passwordMenuPromptTry +=1
        
        # Lock user from entering more input after try limit and revert user back to main menu
        if passwordMenuPromptTry == PASS_MENU_PROMPT_TRIES:
            # Create error message for user and revert user back to menu
            print(Fore.RED + "\nError ... Invalid Number Of Inputs")
            print()
            main()

# Create function to house main body of program
def main():
# Set menu option for drive menu to zero
    drive_menu_option = 0

# Create intro
    createTitleHeader(tabHeader = "\033[1;4mMemorial Hospital Employee Login\033[0m")

# Create drive menu
# Create limit counter for amount of tries user has to type
    driveMenuTries = 0  
    while drive_menu_option != mainMenu.QUIT_MENU and driveMenuTries < MAX_MENU_TRIES:
        # Create options for menu
        print("\nChoose One Of The Following Options:")
        print("\t1. Take Employee Attendance.")
        print("\t2. Mark Worker Calendar.")
        print("\t3. Employee Bonuses And News.")
        print("\t4. Log Off.")
        drive_menu_option = input("\nPlease Choose An Option: ")

        # Create input invalidation if user provides bad input
        if drive_menu_option >= mainMenu.TAKE_ATTENDANCE and drive_menu_option <= mainMenu.QUIT_MENU:
            # Resets tries counter if user does provide good input
            driveMenuTries = 0

        # Create tabs for menu choices
        if drive_menu_option == mainMenu.TAKE_ATTENDANCE:
           employeeLogin()
        elif drive_menu_option == mainMenu.MARK_CALENDER:
            print()
        elif drive_menu_option == mainMenu.EXTRACURRICULARS:
            employeeWorkNews()
        elif drive_menu_option == mainMenu.QUIT_MENU:
            # Creating good bye message when user is done with program
            print("Logging Off. Good Bye")
            print()
            
            # Exit out the loop to end program
            exit()
        else:
            print(Fore.RED + "Error ... User Input Is Incorrect!!! Choose Options (1-4).") 
            print()
            driveMenuTries += 1
    
        # Create error message for user if they put too many bad inputs
    if driveMenuTries == MAX_MENU_TRIES:
        print(Fore.RED + "Error!!!! User Did Too Many Bad Input. Too Many Bad Inputs.")

main()