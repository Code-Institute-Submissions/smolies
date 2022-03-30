#Smolies - 90s style pet game

from random import randrange


class Pet(object):
    """
    Create a default pet abilities
    """
    fun_reduce = 3
    fun_max = 10
    fun_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grr..."']

    def __init__(self, name, pet_type):
        """
        Create pet's initial functions
        """
        self.name = name
        self.pet_type = pet_type
        self.food = randrange(self.food_max)
        self.fun = randrange(self.fun_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):
        """
        Create time passing that affects pet's fun and food levels
        """
        self.fun -= 1
        self.food -= 1

    def mood(self):
        """
        Create pet's default mood based on fun and food levels
        """
        if self.food > self.food_warning and self.fun > self.fun_warning:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "sad"

    def __str__(self):
        """
        Create string that pops the first message in console
        based on player's name choice and pet's mood
        """
        return "\nI'm " + self.name + "." + "\nI feel " + self.mood() + "."

    def teach(self, word):
        """
        Create a function that teaches the pet new words
        """
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        """
        Create a function that allows the pet to talk about themselves
        - overview for the player
        """
        print(
            "I am a " + self.pet_type + " named " + self.name + ".\n" +
            "I feel " + self.mood() + " now.\n"
        )

        print(self.vocab[randrange(len(self.vocab))])

        self.__clock_tick()

    def feed(self):
        """
        Create a function that determines the food level during feeding
        """
        print("Munch, munch...\n Yummm! Thank you!")
        meal = randrange(self.food, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("I am SOOO hungry!")
        elif self.food >= self.food_max:
            self.food = self.food_max
            print("My belly is full!")
        self.__clock_tick()

    def play(self):
        """
        Create a function that determines the joy level during playing
        """
        print("Playing together is really fun!")
        joy = randrange(self.fun, self.fun_max)
        self.fun += joy
        if self.fun < 0:
            self.fun = 0
            print("I'm sad!")
        elif self.fun >= self.fun_max:
            self.fun = self.fun_max
            print("I'm sooo happy!")
        self.__clock_tick()


def main():
    """
    Main game function
    """
    pet_name = input("I'm your new pet. What's my name? ")
    pet_type = input("What type of animal am I? ")

    # Create a new pet
    my_pet = Pet(pet_name, pet_type)

    input("Hello! I'm " + my_pet.name + ", your new pet!" + "\nPress enter to start. ")

    choice = None

    while choice != 0:
        print(
            """
            *** INTERACT WITH YOUR PET ***

            1 - Feed your pet
            2 - Talk with your pet
            3 - Teach your pet some new words
            4 - Play with your pet
            0 - Quit the game
            """
        )

        choice = input("Choice: ")

        if choice == "0":
            print("See you next time!")
        elif choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word = input("What word would you like me to learn? ")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else:
            print("Sorry, can't do that! Try a different option. ")


main()
