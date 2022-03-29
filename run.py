#Smolies - 90s style pet game

from random import randrange

class Pet(object):
    """
    Create a pet
    """
    fun_reduce = 3
    fun_max = 10
    fun_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grr..."']

    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.food = randrange(self.food_max)
        self.fun = randrange(self.fun_max)
        self.vocab = self.vocab[:]
