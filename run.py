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

    @property
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
        Create string that pops the first message in console based on player's name choice and pet's mood
        """
        return "\n I'm " + self.name + "." + "\n I feel " + self.mood() + "."


