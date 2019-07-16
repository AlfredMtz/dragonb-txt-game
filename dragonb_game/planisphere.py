from sys import exit
import random

class Room(object):
    def __init__(self, name, description, helpsystem, character):

        self.name = name
        self.description = description
        self.helpsystem = helpsystem
        self.character = character
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


class Player(object):
    def __init__(self):
        self.name = "Goku"
        self.health = 100



Intro = Room("Welcome", 
"""
This story begins in a very, very distant planet named Vegeta, 
which is about to be destroyed by powerful evil forces. A desperate
father with little to no time puts his son Goku into a spaceship and 
sends it over into space and arrives into a new planetary destination 
named earth. 

Years later, he grows up, starts a family, and as he seems to be much
stronger than average humans, he finds a passion for helping people 
escape the hands of evil villains. One day, returning home, he finds
his entire village wiped out, including his family.

A survivor informs that unknown evil forces had been responsible
for this atrocity and had taken the seven dragon balls as well, of 
wich Goku had been assigned by the greater gods to take care of as
well since these dragon balls had the power to make a wish once a year.

Are you ready to face this challenge and bring
everything back to normality? 
""", "You can either answer yes or no", None)

Zuno_World = Room("Zuno World", 
"""
You lose no time and start investigating where to find
this heartless and evil forces and take back the dragon balls. 

You travel to Zuno's world knowing that he knows everything in the
universe and asked him about where to find these dragon balls. Zuno
informs you that these evil forces are coming from a group of villains 
and their leader. He tells you the leader distributed two of the dragon 
balls to each of his best soldiers and kept one himself.

Zuno gives you directions on where to find the universe's map, so you
should easily find each of these evils soldiers' planet. You thanked 
Zuno for all of its help and set out to find this map!""", None, None)

Map_World = Room("Map World",
"""
After a long two hours of travel, you arrived where this map is. Unfortunately,
the map is locked on a glass secured container which needs a three digit code 
to be open. The secure box has clear instructions that for security reasons you 
are only allowed to have ten attempts to crack open the secured box; otherwise,
it will explode, probably killing in the process. Try to open the container.
""", "You have 10 chances to open this box, the code is 3 digits long", None)

Freeza_World = Room("Freeza World", 
"""
PUFFF!! The box clicked open, and you quickly grab the map. You try to locate 
where each of these evil soldiers live. The closest planet seems to be run by 
one of these evil soldiers which goes by the name of Freeza. Quickly, you set 
yourself into space and land on its planet after a six-hours long trip.
""", "You can go up", None)

Freezas_Forest = Room("Freezas Forest",
"""
You are inside a forest, full of trees, you can hear birds everywhere, a little
bit of sun coming through the tall trees and hiting the ground. Out of a sudden, 
everything gets so quite, too quite indeed""", "You can go left or down", None)

Freezas_Grounds = Room("Freezas Grounds",
"""
Freeza is here, he saw you landing on his planet and went straight to see what your 
business was on his planet. You explained you are there to get the two stolen dragon 
balls he has on hand and get going to find the rest. He refuses and says that would
only happend over his death body, and gets ready to fight you!
""", """You can either type "fight" or go "left" back into the forest""", "Freeza")

Freeza_Defeated = Room("Freeza Defeated",
"""
You defeated him, obtained the dragon balls, 
and quickly set out to find the rest!
""", None, None)

King_Kai_Land = Room("King Kai Land",
"""
After checking on your map, you realize the next soldiers' planet is three days away, 
but also notice King-Kai, the king of the North Area of Universe 7 planet is only minutes
away. You decide to stop by really quick, say hi and tell him about your situation since 
he is a good old friend of yours.

The visit might pay off; he explains you don't have to travel for three long days, as
he could teletransport you there. However, you need to find a way to make him laugh first. 
How would you like to make him laugh?
""", "Maybe you can tell a joke?", None)

Cell_World = Room("Cell World",
"""
Luckily your joke was funny enough, and King Kai is rolling in the floor laughing. After a
few minutes of a good laugh he decides to make thing easy for you and teletransport you
directly where this evil soldier by the name of Cell is.

As soon as you guys get there. King Kai disappear and leave you right in front of Cell(
What a friend right!). Cell is coming quickly to attack you as someone informed him you
had destroyed Freeza and gave details about you may be coming to try to get the dragon balls
from him. Hurry, fight him!
""", None, "Cell")

Cell_Defeated = Room("Cell Defeated",
"""
You defeated him, obtained the dragon balls, 
and quickly set out once again to find the rest!
""", None, None)

Babidi_World = Room("Babidi World",
"""
Once back again in space and looking through your map, you set out again to find the rest
of the dragon balls. In your way to the next malignant soldier's planet, you are faced with
a very unusual asteroid storm full of toxic gases and space monsters, from where evil 
laughing voices can be heard as well. 

You made it right through the end, and find out this alien looking creature by the name of
Babidi was behind all this. He claims to be a powerful wizard, knows your full intentions, 
and is determined not to let you get any further. He cast a magic spell, multiplies himself 
into three and with a laughing voice says your body will turn into dust in space if your 
touch one of the fake version of himself. 

Which one would you like to attack? Version 1, 2, or 3. Choose carefully!
""", "Choose either 1,2, or 3",None)

Majinbu_Grounds = Room("Majinbu Grounds", 
"""
Outstanding, you hit the right real Babidi out of all three. You quickly land on the planet
in search of the dragon balls. After a long search, you find them mixed in a pile of all 
types of chocolates, cakes, and candies and quickly approached to grab them.

Right before you get there, A big round, pink, and sea star looking monster get on your face
thinking you are trying to steal his candies. You explained you want no candy, but the two
dragon balls which are not even candies. However, he is very stubborn and decides not to 
listen still thinking you are trying to steal his candy and gets ready to fight you.

Fight him!
""", None,"Majinbu")

Majinbu_Defeated = Room("Majinbu Defeated", 
"""
You defeated Majinbu, obtained the two dragon balls and get 
ready to fly away and find the last missing dragon ball.
""",None,None)

SynShenron = Room("SynShenron",
"""
Before you set out to find the last dragon ball, the sky turns dark, gets cover in dark gray 
clouds and a massive lighting thunder hits the floors bringing an evil dragon which is 
holding the last missing dragon ball in his right hand. He claims to be the emperor and lord 
of all surrounding planets, knows you have exterminated his best soldiers, and enjoys to tell 
you he was that one responsible for what happened within your village and family. 

You are both here for the same reason and are ready to fight and give everything within each
other's power to obtain all the dragon balls.

Are you ready to fight for the last missing dragon ball?
""", None, "SynShenron")

SynShenron_Defeated = Room("SynShenron Defeated",
"You defeated SynShenron, obtained the last dragon ball and set back home!", None,None)

Raise_EternalDragon = Room("Unexpected Challenge!",
"""
You are finally back home, set the seven dragon balls all together on the floor but nothing 
happens. You hear a voice within the sky from your good old friend King Kai letting you know
that there is a secret phrase to have the dragon balls work and make you a wish.

Yo need to guess and call the complete secret phrase "R*ise Et*rnal D****n." 
""", "What specie was your last opponent?", None)

Game_Fihished = Room("The End",
"""
The sky darkens up, and a vast green, red-eye dragon comes up to ask you what your wish is. 
You informed him you want to bring your village and family back to normality and he exclaims
with a deep voice "That is easy-As You Wish." Everything comes back to normal, and your 
family comes running to give a huge hug and tell you how much they love you!
""", None, None)

Boxmap_Death = Room("BOOOMM!!", """You tried one last time, and the box exploded, 
you loose!""", None, None)

Player_Death = Room("KNOCKOUT!!","""You lost the fight :-/""",None,None)

Intro.add_paths({
    'player yes play': Zuno_World, 
    'player no play': Intro
})

Zuno_World.add_paths({
    'player next play': Map_World
})

Map_World.add_paths({
    "123": Freeza_World,
    '*': Boxmap_Death
})
Freeza_World.add_paths({
    'player go up': Freezas_Forest
})

Freezas_Forest.add_paths({
    'player go down': Freeza_World,
    'player go left': Freezas_Grounds
})

Freezas_Grounds.add_paths({
    '*': Player_Death,
    'player go back': Freezas_Forest,
    'player next play': Freeza_Defeated
})

Freeza_Defeated.add_paths({
    'player next play': King_Kai_Land
})

King_Kai_Land.add_paths({
    'player tell joke': Cell_World
})

Cell_World.add_paths({
    '*': Player_Death,
    'player next play': Cell_Defeated
})

Cell_Defeated.add_paths({
    'player next play': Babidi_World
})

Babidi_World.add_paths({
    '1': Player_Death,
    '2': Majinbu_Grounds,
    '3': Player_Death
})

Majinbu_Grounds.add_paths({
    '*': Player_Death,
    'player next play': Majinbu_Defeated
})

Majinbu_Defeated.add_paths({
    'player next play': SynShenron
})

SynShenron.add_paths({
    '*': Player_Death,
    'player next play': SynShenron_Defeated
})

SynShenron_Defeated.add_paths({
    'player next play': Raise_EternalDragon
})

Raise_EternalDragon.add_paths({
    'player raise eternal': Game_Fihished
})

Game_Fihished.add_paths({})
START = 'intro'

# Recheck these keys
scences = {
    "intro": Intro,
    "zuno_world": Zuno_World,
    "map_world": Map_World,
    "bomb_death": Boxmap_Death,
    "freeza_world": Freeza_World,
    "freezas_forest": Freezas_Forest,
    "freezas_grounds": Freezas_Grounds,
    "freeza_defeated": Freeza_Defeated,
    "kind_kai_land": King_Kai_Land,
    "cell_world": Cell_World,
    "cell_defeated": Cell_Defeated,
    "babidi_world": Babidi_World,
    "majinbu_grounds": Majinbu_Grounds,
    "majinbu_defeated": Majinbu_Defeated,
    "synshenron": SynShenron,
    "synshenron_defeated": SynShenron_Defeated,
    "raise_eternaldragon": Raise_EternalDragon,
    "game_finished": Game_Fihished,
    "player_death": Player_Death
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

def combat(p_health, e_health):

    # p_health = p_health
    # e_health = e_health

    if p_health >= 10 or e_health >= 10:

        player_attack = random.choice([10, 5])
        enemy_attack = random.choice([5, 2])

        if player_attack == 10:
            p_health = p_health - enemy_attack
        else:
            e_health = e_health - player_attack
    
    return p_health, e_health
    

# p_health, e_health = combat(100, 40)
# print(p_health, e_health)
