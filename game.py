import characters
import scenes


class Engine(object):
    # gives scene name to be run
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # traces-in and saves scene into variable 'current_scene'
        current_scene = self.scene_map.open_scene()
        # Last scene to be run once the game is succesfully completed
        last_scene = self.scene_map.next_scene('Completed')

        # runs the game until 'current_scene becomes equal the last_scene
        # than brakes the loop.
        while current_scene != last_scene:
            # Runs and saves return value from enter() function into 'next_scene_variable'.
            next_scene_name = current_scene.enter() 
            # Runs the next scene in the game and saves it into 'current_scene' variable.
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        # After breaking from loop run the last scene and restart the game if asked by user
        if current_scene == last_scene:
            last_scene.enter()
            a_game.play()
        else:
            pass

class Map(object):
    # Reference scenes via diccionary values
    scenes = {
        'Intro': scenes.Intro(),
        'Freeza_world': scenes.FreezaWorld(),
        'Cell_world': scenes.CellWorld(),
        'Majimbu_world': scenes.MajimbuWorld(),
        'Dragon_world': scenes.DragonWorld(),
        'Secret_box': scenes.SecretBox(),
        'Make_wish': scenes.MakingWish(),
        'Completed': scenes.Completed(),
    }
    # Saves given paramete to class into variable/attribute
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Returns value from given key parameter in 'open_scene' function.
    def next_scene(self, scene_name):
        # Take specefic key value from scenes diccionary
        val = Map.scenes.get(scene_name)
        return val

    # Runs given parameter value inside 'next_scene()' function
    def open_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Intro')
a_game = Engine(a_map)
a_game.play()