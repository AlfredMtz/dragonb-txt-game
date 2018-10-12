import characters
import scenes


class Engine(object):
    # Contructor for class to take arguments and assign them
    # to variables, and be run inside as commanded.
    def __init__(self, scene_map):
        self.scene_map = scene_map
        print(self.scene_map)

    # Function will run automatically if not any other parameters
    # are given besides itself.
    def play(self):
        # first run returns backs to the same scene 'Intro()'
        # since it is the first run.
        current_scene = self.scene_map.open_scene()
        # Last message when yo finish the whole game succesfully
        last_scene = self.scene_map.next_scene('Completed')
        #print("current_scene and last_scene before while-loop:")
        #print(current_scene)
        #print(last_scene) 

        # while this statement is true keep running the loop
        # otherwise exit the loop
        while current_scene != last_scene:
            # The enter() function needs to get define on
            # each scene class so it can be implemented here.
            print(">>current_scene:", current_scene)
            next_scene_name = current_scene.enter()
            print(">>next_scene_name:", next_scene_name) 
            # Current scene calls the next_scene function inheritaded
            # from Map() and the va lue on next_scene_name is given as
            # input
            current_scene = self.scene_map.next_scene(next_scene_name)
            print(">>current_scene:", current_scene)
            # The enter() function is call to start executing the code
            # and it is enter inside of the play() fucntion, it only gets
            # executed when the play function get executed.
            current_scene = current_scene.enter() 
            print(">>current_scene1: ", current_scene)


class Map(object):
    # Reference scenes via diccionary values
    scenes = {
        'Intro': scenes.Intro(),
        'Freeza_world': scenes.Freezaworld(),
        'Cell_world': scenes.Cellworld(),
        'Majimbu_world': scenes.Majimbuworld(),
        'One_start_dragon_world': scenes.Dragonworld(),
        'Making_a_wish': scenes.Makingwish(),
        'Death': scenes.Death(),
        'Completed': scenes.Completed(),
    }
    # Initialize a constructor
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Define next scene fucntion
    def next_scene(self, scene_name):
        # Take specefic key value from scenes diccionary
        val = Map.scenes.get(scene_name)
        return val

    # Runs next_scene function() for opening scene
    def open_scene(self):
        return self.next_scene(self.start_scene)


# Intro class becomes an object of the Map class
# a_map becomes an instance of a Map class
# At this point
a_map = Map('Intro')
print(a_map)
a_game = Engine(a_map)
a_game.play()