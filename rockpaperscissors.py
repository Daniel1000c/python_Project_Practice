"""
Filename: rockpaperscissors.py

Program Description: Create a rock paper scissors game where user goes up against the computer in a best of three match up. Then after game is finished take score and put it in to a database table to show to user how many a games that they have won against the computer.

    Overview:
        - Input: playerInput
        
        - Processing:
            *Prompt user with drive menu that gives the following options:
                1. Play Rock, Paper, Scissors
                    - Create a score board for player and computer
                        * To tell which is the player and computer use the colorama module to highlight the score board for each win or loss
                    
                    - Prompt player with a choice of "Rock, Paper, and Scissor" for game options
                    
                    - Display to user if they have won or lost the round to the computer
                    
                    - After user has concluded the game, create a database to store date, time, score, and winner of each game
                    
                    - Prompt player if they want to play again or log off the game and return back to main menu
                    
                2. View Score Stats
                    - Dispaly to user the time, date, score, and winner of game when looking at game stats
                    
                    - Create File if user game data does not exist
                        * Create an error message to show file data does not exist
                        * Prompt user if they want to create a new file or return back to the main menu if finished
                        
                3. Exit From Game
                    - Log off from game and program will prompt user that game is shut down 
        
        - Output: rockpaperscissors.py
"""

# Import colorama module to game
import colorama
from colorama import Fore
# Reset the color every time when Fore is used 
colorama.init(autoreset = True)

# Import datetime module to view the time game was started
import datetime

# Create class for game menu options
class gameOption:
    PLAY = "1"
    STATS = "2"
    QUIT = "3"
    
# Create header function to format each section header
def headerFormat(sectionHeader):
    # Separate each header with a new line in order to make is easier to read for user
    print()
    
    # Center header section by 170 pixels
    headerSection = sectionHeader.center(120)
    
    # Display section header
    print(headerSection)
    
    # Create new line
    print()
    
    
# Create placeholder for player drive menu
gameMenu = 0 
  
# Create menu options for main body framework funtion
def playerMenu():
    # Create while loop for player to return back to screen if entered wrong choice
    while gameMenu != gameOption.QUIT:
        
        headerFormat(sectionHeader = Fore.BLUE + "\033[1;4mExtreme Rock, Paper Scissors \033[0m")
    
        # Drive drive menu for player when program first boots up
        print("Choose One Of The Following Options: \n")
        print("1. Play Rock, Paper Scissors.")
        print("2. View Player Stats.")
        print("3. Log Off.")
    
        # Prompt user to choose any option
        gameOptionMenu = input("\n What is Your Choice? ")
        
        # Create branches from menu options
        if gameOptionMenu == gameOption.PLAY:
            print("1")
            
        elif gameOptionMenu == gameOption.STATS:
            print("2")
            
        elif gameOptionMenu == gameOption.QUIT:
            # Display goodbye message and log off program
            print("Good Bye")
            
            # Exit out of program
            exit()
        else:
            # Display error message if user picks wrong option
            headerFormat(Fore.RED + "Error Wrong Option, Pick Options (1-3).")
            
    
# Create a main function for the body framework of program 
def main():
    playerMenu()
main()