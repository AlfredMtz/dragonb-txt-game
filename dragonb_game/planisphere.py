from sys import exit


class Room(object):
    def __init__(self, name, description, helpsystem):
        self.name = name
        self.description = description
        self.helpsystem = helpsystem
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


Intro = Room("Intro", 
"""
WELCOME TO DRAGONBZ TEXT GAME!!!

This story begins in a very, very far planet named Vegeta which
is about to be destroyed by powerful evil forces. A desperate
father with little to no time puts his son into a spaceship 
and sends it over into space and arrives into a new planetary
destination named earth. 

Years later he grows up, starts a family, and as he seems to be much
stronger than average humans he finds a passion for helping people 
escape the hands of evil villains. One day, returning home, he sees
his entire village wiped out, including his family.

A survivor informs him that an evil dragon came in and took 
the seven dragon balls which grand a single wish once a year.So, Goku 
the warrior goes out to locate all seven dragon balls to bring them back 
home and make a wish to have his family and village back to normality.

Would you like to get on Goku's shoes and start the quest to saving your 
village and bring your family back to life?

[ yes / no ] """, "You can either answer yes or no")

Zuno_World = Room("Zuno World", 
"""
Great!!!  You lose no time and start investigating where to find
this heartless and evil dragon and take back the dragon balls. 

You travel to Zuno's world knowing that he knows everything in the
universe and asked him about where to find these dragon balls. Zuno
quickly informs you that this dragon distributed two of the dragon 
balls to each of his best soldiers to keep them safe while he keeps
only one.

You thanked Zuno for all of its help and leave quickly into space
setting directly to the closest planet where one of these dragon's 
soldiers by the name of Freeza is living.

Type 'next' to continue """, "You supposed to type 'next' to continue :-) ")

Freeza_World = Room("Freeza World", 
"""
You finally arrived, you are at the Center of freeeza's world. 
Everything seems so empty.""", "You can go north")

Freezas_Forest = Room("Freezas Forest",
"""
You are inside a forest, full of trees, you can hear birds everywhere, a little
bit of sun coming through the tall trees and hiting the ground. Out of a sudden, 
everything gets so quite, too quite indeed""", "You can go left or down")

Dodorias_Grounds = Room("Dodorias Grounds",
"""
Dodoria is here, one of Freeza's top solders, he knew you were going to get here
at some point and he is ready to fight you and not let you get any further or closer
to his emperor freeza. What would you like to do? """, """You can either fight him or
go back into the forest""")

Fight_File = Room(None,None,None)


Intro.add_paths({
    'yes': Zuno_World, 
    'no': Intro
})

Zuno_World.add_paths({
    'next': Freeza_World
})

Freeza_World.add_paths({
    'up': Freezas_Forest
})

Freezas_Forest.add_paths({
    'down': Freeza_World,
    'left': Dodorias_Grounds
})

Dodorias_Grounds.add_paths({
    'fight': Fight_File,
    'right': Freezas_Forest
})

START = 'intro'

# Recheck these keys
scences = {
    "intro": Intro,
    "zuno_world": Zuno_World,
    "freeza_world": Freeza_World,
    "freezas_forest": Freezas_Forest,
    "dodorias_grounds": Dodorias_Grounds
}


# returns key value
def load_room(name):
    val = scences.get(name)
    return val


# returns specific scenes key
def name_room(room):
    for key, value in scences.items():
        if value == room:
            return key


#room = load_room(START)
#print(room.name)