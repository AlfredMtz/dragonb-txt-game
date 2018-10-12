# Characters for the game
class Character(object):
    
    def center(self):
        print("This is the parent class for all upcoming subclasses")
        exit(1)

class Playerc(Character):

    def __init__(self):
        self.name = "Goku"
        self.health = 100
        self.attack = 10
        

class Freezac(Character):

    def __init__(self):
        self.name = "Freeza"
        self.health = 50
        self.attack = 10

class Cellc(Character):

    def __init__(self):
        self.name = "Cell"
        self.health = 60
        self.attack = 10

class Majimbuc(Character):

    def __init__(self):
        self.name = "Majimbu"
        self.health = 70
        self.attack = 10

class Dragonc(Character):

    def __init__(self):
        self.name = "Dragon"
        self.health = 90
        self.attack = 10
