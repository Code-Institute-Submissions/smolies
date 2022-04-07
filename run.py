from random import randrange
import pyfiglet
from termcolor import colored

# pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 6, "fun": 6, "toys": [], "vocab": ["Grrr..."]}

# pet toys data object
pet_toys = {"cat": ["cardboard box", "scratcher a.k.a your favorite chair", "laser pointer"], "dog": ["your new pair of shoes", "stick... just a stick", "annoying squeeky toy"],
"hamster": ["rainbow bridge", "climbing ladder", "super fast spinning wheel"], "fish": ["pirate's treasure chest", "undersea cave", "fluorescent non-toxic plants"],
"bird": ["luxurious bathtub bowl", "wooden playground", "cute swing"]}


def create_pet():
    """
    Prompt for different options of pet type
    """
    print(colored(pyfiglet.figlet_format("Smolies - pet game", width = 200,), 'green', attrs=['bold']))
    # get the input of what type of pet is this
    pet_type = ""

    pet_options = list(pet_toys.keys())
    # validate the input
    while pet_type not in pet_options:
        print("Hello! In this game you can choose one of the following pets: \n")
        for option in pet_options:
            print(option)
        pet_type = input("\nI bet you're excited! Which pet did you choose? ").lower()
        if pet_type not in pet_options:
            print(colored("Sorry, this animal is not available! Try again!", 'red'))

    # write the pet type into the database
    pet["type"] = pet_type

    # name the pet
    pet["name"] = input("Okay, one more question... What's the name of your " + pet["type"] + "? ")
    while not pet["name"].isalpha():
        print(colored("TRY AGAIN! Your pet's name can include ONLY letters.", 'red'))
        pet["name"] = input("What's the name of your " + pet["type"] + "? ")

    input("\nHello! I'm " + pet["name"] + ", your new pet!" + "\nPress enter to start. ")
    print(colored(r"""

_     /)---(\          /~~~\
\\   (/ . . \)        /  .. \
 \\__)-\(*)/         (_,\  |_)
 \_       (_         /   \@/    /^^^\
 (___/-(____) _     /      \   / . . \
              \\   /  `    |   V\ Y /V
               \\/  \   | _\    / - \
                \   /__'|| \\_  |    \
                 \_____)|_).\_).||(__V

         """, 'green', attrs=['bold']))
    print(colored(pyfiglet.figlet_format("Smolies - PET GAME", font = 'small', width = 800), 'cyan', attrs=['bold']))


def print_menu(menu_options):
    """
    Print menu with options for the player
    """
    option_keys = list(menu_options.keys())

    print(colored("\n***INERACT WITH YOUR PET***", 'yellow', attrs=['bold']))
    print(colored("-------------", 'yellow'))
    for key in option_keys:
        print(colored(key + ":\t" + menu_options[key]["text"], 'yellow'))

    print(colored("-------------", 'yellow'))
    print(colored("\n***REMEMBER TO FEED YOUR PET AND KEEP IT HAPPY***", 'yellow', attrs=['bold']))
    print(colored("\n***BE MINDFUL THAT THE PETS ARE AGING...***", 'yellow', attrs=['bold']))


def time_runs():
    """
    Timer
    """
    pet["age"] += 1
    pet["hunger"] += 2
    pet["fun"] -= 2
    
    #add death option due to the old age or starvation
    if pet["age"] == 16 or pet["hunger"] > 18:
        print()
        print(colored("Your pet was very weak and decided to take a looooong nap...", 'red', attrs=['bold']))
        print(r"""
            _____  zZzZzZz
          /~/~   ~\     zZzZz
         | |       \        zZZzZ
         \ \        \
          \ \        \
         --\ \       .\''
        --==\ \     ,,i!!i,
            ''"'',,}{,,
        
        """)
        exit()


def play_toys():
    """
    Play with toys
    """
    print(colored(pet["name"] + " really likes to play with the toys! Fun increased!", attrs=['bold']))
    print(r"""
                   ___  .-.
                  /   `~'. |
                  \__/   O`O_
                   |         D
                   \    .__U'
                    |,.,./
        ,_        _/`'`'`b
        \ `.__.-'`        \-._
         |            '.__ `'-;_
         |            _.:::'-.__)
          \    ;_..--'/::::://::\
          |   /  /   |::::://::::|
          \  \ \__)   \::://::::/
           \__)        '://::::'
                         `'-'`` """)
    joy = 3
    pet["fun"] += joy

    if pet["fun"] <= 0:
        pet["fun"] == 0
        print("I'm so bored...!")
    elif pet["fun"] >= 15:
        pet["fun"] == 15
        print("I'm having so much fun!")


def get_toys():
    """
    Get new toys
    """
    print(colored("Cool! Let's get some new toys for " + pet["name"] + "!", attrs=['bold']))
    print(r"""
     .-.               .-.
    (   `-._________.-'   )
     >=     _______     =<
    (   ,-'`       `'-,   )
     `-'               `-'
    """)
    toy_options = pet_toys[pet["type"]]

    # toy number that can be selected from the list of toys
    toy_number = -1
    # get a valid toy for the input
    while toy_number < 0 or toy_number > len(toy_options) - 1:
        for i in range(len(toy_options)):
            print(str(i) + ": " + toy_options[i])
        toy_number = int(input("Select the number of a toy:"))

    # get the chosen toy option from the list
    chosen_toy = toy_options[toy_number]
    pet["toys"].append(chosen_toy)
    print("Great! You got a " + chosen_toy + " for " + pet["name"] + ".")


def quit_game():
    """
    Quit the game
    """
    print(r"""
         _,,_
       /`    `\
      / / o o\ \
      \/\  Y /\/       /\-/\
       / `'^` \       /o o  \               _
    , (  \   | \     =\ Y  =/-~~~~~~-,_____/ )
    |\|\_/   \_/       '^--'          ______/
    \/'.  \  /'\         \           /
     \    /=\  /         ||  |---'\  \
     /____)/____)       (_(__|   ((__|    
    """)
    print(colored("Done for today? Thanks for playing!", 'green', attrs=['bold']))
    print()
    exit()


def feed_pet():
    """
    Feeding the pet
    """
    print(colored("\nYou just gave some food to " + pet["name"] + ". Hunger decreased!", attrs=['bold']))
    print(r"""
             (
              )
         __..---..__
     ,-='  /  |  \  `=-.
    :--..___________..--;
     \.,_____________,./
    """)
    meal = 3
    pet["hunger"] -= meal

    if pet["hunger"] <= 0:
        pet["hunger"] == 0
        print(colored(pet["name"] + " is full!", attrs=['bold']))
    elif pet["hunger"] >= 10:
        print("I'm sooo hungry!")


def teach_words():
    """
    Teaches the pet new words
    """
    new_word = input("What would you like me to learn? ")
    pet["vocab"].append(new_word)
    print()
    print("Okaaaay! I think I got it!")
    print(colored("Now try to talk with me and see if I got it right.", attrs=['bold']))


def talk():
    """
    Talk with your pet
    """
    print()
    print("I am a " + pet["type"] + ". My name is " + pet["name"] + ".\n")
    print("I know how to say: " + pet["vocab"][randrange(len(pet["vocab"]))])


def print_stats():
    """
    Print current statistics about the pet
    """
    print("\nYour " + pet["type"] + " " + pet["name"] + " is really cool!")
    print("At the moment " + pet["name"] + " has: " + str(len(pet["toys"])) + " toys, which are: ")
    for toy in pet["toys"]:
        print(toy)
    print(pet["name"] + "'s hunger is reaching " + str(pet["hunger"]) + ", while the max is 15.")
    print(pet["name"] + "'s joy is reaching " + str(pet["fun"]) + ", while the max is 15.")
    print("Your " + pet["type"] + " is " + str(pet["age"]) + " days old.")

def main():
    """
    Main game loop
    """
    # create the pet
    create_pet()

    # menu options for interaction with pet in the console
    menu_options = {"1": {"function": feed_pet, "text": "Give some food to " + pet["name"]},
        "2": {"function": play_toys, "text": "Play with your " + pet["type"]},
        "3": {"function": get_toys, "text": "Get new toys for " + pet["name"]},
        "4": {"function": teach_words, "text": "Teach " + pet["name"] + " some new words"},
        "5": {"function": talk, "text": "Talk with your " + pet["type"]},
        "0": {"function": quit_game, "text": "Quit the game for now"}}

    keep_playing = True
    while keep_playing:
        # print the menu in the console
        menu_choice = ""

        # get player's input on menu option and validate it
        while menu_choice not in menu_options.keys():
            print_menu(menu_options)
            menu_choice = input("\nSooo... what are we going to do? ").upper()
            if menu_choice not in menu_options.keys():
                print(colored("Sorry, try something different! ", 'red'))

        # call the function that correspons to menu option chosen by the player
        menu_options[menu_choice]["function"]()
        # call other functions that afftect the game
        time_runs()

        print_stats()


main()
