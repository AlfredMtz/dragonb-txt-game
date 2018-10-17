
# Characters and their corresponding attributes values

class Character(object):
    
    def center(self):
        print("This is the parent class for all upcoming subclasses")
        exit(1)

class Player(Character):

    def __init__(self):
        self.name = "Goku"
        self.health = 100
        self.attack = 10
        

class Freeza(Character):

    def __init__(self):
        self.name = "Freeza"
        self.health = 20
        self.attack = 10

class Cell(Character):

    def __init__(self):
        self.name = "Cell"
        self.health = 30
        self.attack = 10

class Majimbu(Character):

    def __init__(self):
        self.name = "Majimbu"
        self.health = 40
        self.attack = 10

class Dragon(Character):

    def __init__(self):
        self.name = "Dragon"
        self.health = 50
        self.attack = 10
