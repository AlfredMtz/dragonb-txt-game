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

[ yes / no ] """, None)

Zuno_World = Room(
    "Zuno world", """
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

Type [next] to continue
""")

Freeza_World = Room(
    "Freeza world", """
You finally arrived, you are at the Center of freeeza's world. 
There's a path going north and south.
""")

Intro.add_paths({
    'yes': Zuno_World, 
    'no': Intro
    })

Zuno_World.add_paths({'next': Freeza_World})

#Freeza_World.add_paths()

START = 'intro'

scences = {
    'intro': Intro,
    'yes': Zuno_World,
    'no': Intro,
    'next': Freeza_World,
}


# returns key value
def load_room(name):
    val = scences.get(name)
    return val


# returns specific scenes key if given room/parameter equals to a scenes' key value
def name_room(room):
    for key, value in scences.items():
        if value == room:
            return key


#room = load_room(START)
#print(room.name)