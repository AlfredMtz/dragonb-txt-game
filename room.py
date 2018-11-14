import characters


class Room(object):
     
     def __init__(self, name, description, character):
         self.name = name
         self.description = description
         self.character = character
         self.paths = {}

     def go(self, direction):
         while True:
            # If there is a path on that direction
            if direction in self.paths:
                return self.paths.get(direction, None)
            # if direction is given and is other than 'north', 'south', 'west', 'east'
            elif direction not in ['north', 'south', 'west', 'east']:
                print("I don't understand the action named " + direction + ".", "Try again!")
                direction = input("Which way do you want to go?\n> ")
                continue
            # if direction is given, but nothing exists on that direction
            else:
                print("You can't go on that direction. Try again!")
                direction = input("Which way do you want to go?\n> ")
                continue
            
     def add_paths(self, paths):
         self.paths.update(paths)