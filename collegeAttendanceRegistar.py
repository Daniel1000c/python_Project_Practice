""" Problem: Professor mobasher needs a attendance system that takes roll call for student names and deem them absent, late, or present. The program should be able to:

    1. Take Student Attendance:
        - Prompt professor for student name, last name.
        - Prompt professor if student is late, absent, or present
        - Save student personal info to file and mark to each name with P, L, or A
        - Mark down at what time and date this attendance occurred
        
    2. Display student file
        - Prompt professor for which attendance file she needs for a certain class
        - Display file to professor when input is entered
        - Save data after program is finished running 
    
    3. Quit Menu
        - End program after professor is done using application
"""
# Import colorama for comestic applications
import colorama
from colorama import Fore
colorama.init(autoreset = True)

# Constants and variables
TAKE_ATTENDANCE = "1"
DISPLAY = "2"
LOG_OFF = "3"

# Create fucntion to center header for each branch section
def createSectionHeader(tabHeader):
    # Create newline for each section to make it easier to read
    print()
    
    # Center the header by 70 pixels
    sectionHeader = tabHeader.center(150)
    
    # Display title to user 
    print(sectionHeader)
    
    # Create anoter new line to separate better and make it more readable
    print()

# Create function to prompt user for student name and if tardy, present, or absent
def createAttendance(studentName, studentRollCall):
    # Prompt professor if they want to take attendance
    professorAttendanceChoice = input("Do You Want To Take Attendance (Y/N): ")
    
    if professorAttendanceChoice == "Y":
        # Prompt user if they want to add a student
        attendance =  input("\nDo You Want To Add A Student (Yes/No): ")
        
        if attendance == "Yes":
            while attendance != "No":
            # Prompt professor for student name
                studentName = str(input("\nPlease Enter Full Student Name: "))  
    
                # Prompt professor if student is late, absent, present
                studentRollCall = str(input("\nPlease Enter Choices (P,A,L) For Present, Absent, Or Late: "))
                
                # Prompt user again to add another student
                attendance =  input("\nDo You Want To Add A Student (Yes/No): ")
                
        elif attendance == "No":
            # Revert user back to main menu
            main()
                
            return studentName, studentRollCall
    elif professorAttendanceChoice == "N":
        # Revert professor back to main menu
        main()
        
# Create placeholder value for drop down menu option choice
attendanceOption = 0

# Display drop down menu to user
def main():
    while attendanceOption != LOG_OFF:
        # Create title header for section
        createSectionHeader(tabHeader = Fore.BLUE + "\033[1;4mProfessor Maha's Attendance Taker\033[0m")
    
        # Display options to user
        print(Fore.GREEN + "\t\t\t\t\t\t1. Take Attendance.")
        print(Fore.CYAN + "\t\t\t\t\t\t2. Display Student Class File.")
        print(Fore.RED + "\t\t\t\t\t\t3. Log Off.")
    
        # Prompt user for option choice
        menuOption = input("\nPlease Choose An Action: ")
        print()
    
        # Create drive branches for user
        if menuOption == TAKE_ATTENDANCE:
            # Call create attendance function in drive menu and set student name and roll call to empty strings
            createAttendance(studentName = "", studentRollCall = "")
            
        elif menuOption == DISPLAY:
            print("2")
        elif menuOption == LOG_OFF:
            # Display good bye message to user 
            print("Logging Off ... Good Bye.")
        
            # Shut down program after user is finished
            exit()
        else:
            # Display error message is user option is invalid
            print(Fore.RED + "Error ... Invalid User Option!!!! Must Be Options (1-3).\n")
main()