"""
Creator: Daniel Velez

Date: 7/8/24

Objective: Create a user input program that will let people vote for a candidate of their choosing from the choices below

    Part 1: Ask user for input:
        * Are you a Us citizen? * Checked
        * How old are you
        * What state are you voting from
        
    Part 2: Provide the user with candidates to vote from
        * Do you want to vote for republican ,democrats or third party?
        * If they give a choice, print("Thank you for voting")
        
    Input Invalidation:
        * If not us citizen, print("you must be a us citizen to vote in the us elections") * Checked
        * If not old enough, print("You must be a at least 18 years old to vote.!!!") * Checked
        * If too old, print("You are dead and cannot vote!!!")
        * If state is not in choice, print("Choice must be a valid us state")
        * If party not valid, print("Please pick a valid party")
        
Goal: have the program let the user pick their voting state and let them vote their candidate    
"""
# Create list or dictionary to store voter states:
statesDict = {"Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
    "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
    "Wisconsin": "WI", "Wyoming": "WY"}

# Create title for voting program
print("Welcome To Voting Poll")

#Create main function to house rest of code
def main():
    userCitizenship = input("Are you a US Citizen? (Yes/No): ") 
    
    # Create if statement if user is us citizen or not
    if userCitizenship == "Yes":
        try: 
            #If user says yes then prompt user for age
            voterAge = int(input("What is your age?: "))
            
            #Create if statement is user is able to vote or not
            if voterAge < 18:
                #Print statement that user is not able to vote yet
                print("You are not able to vote yet, You are too young!!!!")
                
            elif voterAge >= 18 and voterAge <= 99:
                # Prompt user their voting state if over 18 
                voterState = str(input("What is your State?: "))
                
                # Normalize input to match dictionary keys
                voterStateFormat = voterState.title()
                
                try:
                    if voterState.isdigit():
                        raise ValueError("State input must be a string, not a number.")
                    
                    # Create if statement for voter state   
                    if voterStateFormat  in statesDict:
                        # Prompt user with which party they want to vote for 
                        voterParty = str(input("What party do you chose? (Republican/Democrat/Third party): "))
                        
                        # Create if statement for user choosing party
                        
                        if voterParty == "Republican":
                            # Print statement telling user thank you for voting
                            print("Thank you for voting, Good Bye!!")
                        elif voterParty == "Democrat":
                            # Print statement telling user thank you for voting
                            print("Thank you for voting, Good Bye!!")
                        elif voterParty == "Third Party":
                            # Print statement telling user thank you for voting
                            print("Thank you for voting, Good Bye!!")
                        else:
                            # Create error message if user party is not on list
                            print("Must be party on the ballot!")
                    else:
                        # Print error statement that user must pick valid us voter state
                        print("Must be a valid voter state!!!")
                        
                except ValueError:
                    #Print error that user must input a string and not a number
                        print("Error!!!!")
                    
            elif voterAge >= 100:
                # Print statement that says user is already dead and can't vote
                print("You are dead and cannot vote!!!")
                
            else:
                print("Error has occurred")
                
        except ValueError:
            # Print statement that user must input whole int number
            print("Error!!! option must be a whole number and not a string!!")
            
    elif userCitizenship == "No":
        #Print statement that user must be a us citizen to vote
        print("You must be a USA citizen to vote!!!")
        
    else:
        #Print error if user inputs a answer that is not yes or no
        print("Option must be either Yes or No!!!!")


# Call main function that houses rest of code
main()



