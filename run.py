import pyfiglet
from termcolor import colored

# pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

# pet toys data object
petToys = {"cat": ["cardboard box", "scratcher a.k.a your favorite chair", "laser pointer"], "dog": ["your new pair of shoes", "stick... just a stick", "annoying squeeky toy"], 
"hamster": ["rainbow bridge", "climbing ladder", "super fast spinning wheel"], "fish": ["pirate's treasure chest", "undersea cave", "fluorescent non-toxic plants"], 
"bird": ["luxurious bathtub bowl", "wooden playground", "cute swing"]}

# Prompt for different options of pet type
def createPet():
    print(colored(pyfiglet.figlet_format("Smolies - pet game", width = 200,), 'green'))
    # get the input of what type of pet is this
    petType = ""

    petOptions = list(petToys.keys())
    # validate the input
    while petType not in petOptions:
        print("Hello! In this game you can choose one of the following pets: \n")
        for option in petOptions:
            print(option)
        petType = input("\nI bet you're excited! Which pet did you choose? ").lower()

    # write the pet type into the database
    pet["type"] = petType

    # name the pet
    pet["name"] = input("Okay, one more question... What's the name of your " + pet["type"] + "? ")
    while not pet["name"].isalpha():
        print(colored("TRY AGAIN! Your pet's name can include ONLY letters.", 'red'))
        pet["name"] = input("What's the name of your " + pet["type"] + "? ")

    input("\nHello! I'm " + pet["name"] + ", your new pet!" + "\nPress enter to start. ")
    print(colored(r"""

                 .-.   .-.
                /   \ /   \ 
            .-. |    |    | .-.
           /   \ \  / \  / /   \
           |   |  '`.-.`'  |   |
            \_.' .-`   `-. '._/
              .-'         '-.       *** SMOLIES - PET GAME ***
             /               \
             |               |
              \             /
               '.___...___.'


         """, 'green'))

# Print menu with options for the player
def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print(colored("\n***INERACT WITH YOUR PET***", 'yellow', attrs=['bold']))
    print(colored("-------------", 'yellow'))
    for key in optionKeys:
        print(colored(key + ":\t" + menuOptions[key]["text"], 'yellow'))

    print(colored("-------------", 'yellow'))

# Play with toys
def playToys():
    print(pet["name"] + " really likes to play with the toys!")

# Get new toys
def getToys():
    print("Cool! Let's get some new toys for " + pet["name"] + "!")
    toyOptions = petToys[pet["type"]]
    
    # toy number that can be selected from the list of toys
    toyNumber = -1
    # get a valid toy for the input
    while toyNumber < 0 or toyNumber > len(toyOptions) - 1:
        for i in range(len(toyOptions)):
            print(str(i) + ": " + toyOptions[i])
        toyNumber = int(input("Select the number of a toy:"))

    # get the chosen toy option from the list
    chosenToy = toyOptions[toyNumber]
    pet["toys"].append(chosenToy)
    print("Great! You chose " + chosenToy + " for " + pet["name"] + ".")

# Quit the game
def quitGame():
    print("Done for today? Thanks for playing!")
    exit()

# Feeding the pet
def feedPet():
    # fixes the issue with negative hunger values
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
        newHunger = 0

    pet["hunger"] = newHunger
    print("\nYou just gave some food to " + pet["name"] + ". Hunger decreased by 10!")

# print current statistics about the pet
def printStats():
    print("\nYour " + pet["type"] + " " + pet["name"] + " is really awesome!")
    print("At the moment " + pet["name"] + " has: " + str(len(pet["toys"])) + " toys, which are: ")
    for toy in pet["toys"]:
        print(toy)
    print(pet["name"] + "'s hunger is reaching " + str(pet["hunger"]) + ", while the max is 100.")
    print(pet["name"] + " is " + str(pet["age"]) + " days old.")

# Main game loop
def main():
    # create the pet
    createPet()

    # menu options for interaction with pet in the console
    menuOptions = {"F": {"function": feedPet, "text": "Give some food to " + pet["name"] },
        "P": {"function": playToys, "text": "Play with your " + pet["type"] },
        "T": {"function": getToys, "text": "Get new toys for " + pet["name"] },
        "Q": {"function": quitGame, "text": "Quit the game for now"} }

    keepPlaying = True
    while keepPlaying:
        # print the menu in the console
        menuChoice = ""

        # get player's input on menu option and validate it
        while menuChoice not in menuOptions.keys():
            printMenu(menuOptions)
            menuChoice = input("\nSooo... what are we going to do? ").upper()

        # quit the game if player types in Q
        if menuOptions == "Q":
            keepPlaying = False

        # call the function that correspons to menu option chosen by the player
        menuOptions[menuChoice]["function"]()

        # increase pet's hunger level
        pet["hunger"] += 10
        pet["age"] += 1

        printStats()

        # print an extra line between the menu options
        print()


main()
