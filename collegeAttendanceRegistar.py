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
# Import datetime module to get accurate time of when attendance was taken.
import datetime

# Import colorama for comestic applications
import colorama
from colorama import Fore
colorama.init(autoreset = True)

# Constants and variables
TAKE_ATTENDANCE = "1"
DISPLAY = "2"
LOG_OFF = "3"

# Create function to display file contents of student attendance
def displayAttendance():
    # Create title header for section
    createSectionHeader(tabHeader = Fore.CYAN + "\033[1;4mClass Attendance\033[0m\n")
    
    # Create input invalidation if user file does not exist
    try:
        # Open file
        fileObject = open("mahaStudentAttendance.txt")
        
        # Read objects from file
        fileContent = fileObject.read()
        
        # Print contents from file
        print(fileContent)
        
        # Close file
        fileObject.close()
        
    except FileNotFoundError:
        # Create error message if user file does not exist
        print(Fore.RED + "Error !!! File Not Found." )
        
        # Prompt user if they want to create a file
        userFile = input("Do You Want To Create A File (Yes/No): ")
        
        # Create while loop to create choice
        while userFile != "No":
            if userFile == "Yes":
                # Open New file
                fileObject = open("mahaStudentAttendance.txt","w")
                
                # Close file
                fileObject.close()
                
                # Print out creating file message 
                print("Creating New File.")
                
                # Revert user back to main menu
                main()
                
            elif userFile == "No":
                # Revert user back to main menu
                main()
            else:
                # Print error message
                print(Fore.RED + "Error !!! Invalid User Option, Must Use (Yes/No).") 
                
                # Prompt user again  
                userFile = input("\nDo You Want To Create A File (Yes/No): ")    
    
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
    # Create a list of valid inputs
    valid_inputs = ["A","P","L"]
    
    # Prompt professor if they want to take attendance
    professorAttendanceChoice = input("Do You Want To Take Attendance (Y/N): ")
    
    while professorAttendanceChoice != "N":
        
        if professorAttendanceChoice == "Y":
            # Create title header for section
            createSectionHeader(tabHeader = Fore.BLUE + "\033[1;4mStudent Attendance\033[0m")
            
            # Prompt user if they want to add a student
            attendance =  input("\nDo You Want To Add A Student (Yes/No): ")
            
            while attendance != "No":
                if attendance == "Yes":
                    while attendance != "No":
                        # Prompt professor for student name
                        studentName = str(input("\nPlease Enter Full Student Name: "))  
    
                        # Prompt professor if student is late, absent, present
                        studentRollCall = str(input("\nPlease Enter Choices (P,A,L) For Present, Absent, Or Late: "))
                        
                        # Create input invalidation for present, late, tardy
                        while studentRollCall not in valid_inputs:
                            # Create error message
                            print(Fore.RED + "Error !!! Invalid Input, Must Be (A/L/P).")
                            
                            # Prompt user for choice again
                            studentRollCall = str(input("\nPlease Enter Choices (P,A,L) For Present, Absent, Or Late: "))
                
                        # Create a file to store student attendance information
                        fileObject = open("mahaStudentAttendance.txt","a")
                
                        # Write items to file 
                        # Create newline variable to space between names
                        NEWLINE = "\n"
                        # Create title header for section for file for better formatting
                        fileObject.write("|StudentName|        |Student Status|          |Time Recorded|")
                        fileObject.write(NEWLINE)
                        fileObject.write(studentName)
                        fileObject.write("              ")
                        fileObject.write(studentRollCall)
                        fileObject.write("                     ")
                        fileObject.write(str(datetime.datetime.now()))
                        fileObject.write(NEWLINE)
                        fileObject.write(NEWLINE)
                
                        # Close file once done
                        fileObject.close()
                
                        # Prompt user again to add another student
                        attendance =  input("\nDo You Want To Add A Student (Yes/No): ")
                
                elif attendance == "No":
                    # Revert user back to main menu
                    main()
                else:
                    # Print error message if user input is incorrect
                    print(Fore.RED + "\nError !!! Invaild user Choice, Please Enter (Yes/No).")
                
                    # Prompt user again for choice
                    attendance =  input("\nDo You Want To Add A Student (Yes/No): ")
            
            return studentName, studentRollCall
    
        elif professorAttendanceChoice == "N":
            # Revert professor back to main menu
            main()
        else:
            # Print out error message for incorrect user option
            print(Fore.RED + "Error !!! Invalid User Option, Must be (Y/N).")
            
            # Prompt user again for choice
            professorAttendanceChoice = input("\nDo You Want To Take Attendance (Y/N): ")
        
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
            # Call display attendance function to display class to user
            displayAttendance()
            
        elif menuOption == LOG_OFF:
            # Display good bye message to user 
            print("Logging Off ... Good Bye.")
        
            # Shut down program after user is finished
            exit()
            
        else:
            # Display error message is user option is invalid
            print(Fore.RED + "Error ... Invalid User Option!!!! Must Be Options (1-3).\n")
main()