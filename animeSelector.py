# Filename: animeSelector.py
# Description: Create a drive menu that prompts the user to:
#                       -1. Login
#                       -2. New User? Sign Up!
#                       -3. Developer Settings
#                       -4. Shutdown

# Input: userChoice

# Processing: 
#       1. Prompt user with drive menu
#           - Case 1: Login
#               * Log user into hub screen where user can pick anime title and genre of choice
#               * Prompt user for username and password
#               * Prompt user with drive menu:
#                   1. Choose an anime
#                       * Prompt user with genre of anime they would like
#                   2. Previously watched anime
#                       * Direct to a file list to show what anime they have watched in the past
#                   3. User Settings
#                       * Allow user to delete subscription from database, change username, change password
#                   4. Sign out
#                       * Bring user back to main menu
#           - Case 2: New User? Sign Up!
#               * Prompt new user with name, birthdate, username, and password
#               * Send personal info to file and record time and date of when user was created
#               * Redirect user back to main screen once done
#           - Case 3: Developer Settings
#               * Allow the developer to delete users form database as they see fit
#               * Show user how many people are logged into system 
#               * Allow developer to change font size and color of program
#           - Case 4: Shutdown: 
#               * Program will stop running and cease to boot up

# Output: Display anime selector menu to user

# Create a class of menu choices for base drive menu
