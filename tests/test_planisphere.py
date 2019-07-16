import pytest
from dragonb_game.planisphere import *



def test_dragonb_game_map():
    # Intro room
    start_room = load_room(START)
    assert start_room.name == "Welcome"
    assert start_room.go('player no play') == Intro
    assert start_room.go('player yes play') == Zuno_World
    # next room
    available_path = name_room(Zuno_World) 
    assert available_path == "zuno_world"

    # Zuno Room
    zuno_room = load_room(available_path)
    assert zuno_room.name == "Zuno World"
    assert zuno_room.go('player next play') == Map_World
    # next room
    available_path = name_room(Map_World)
    assert available_path == "map_world"


    # Map Room 
    map_room = load_room(available_path)
    assert map_room.name == "Map World"
    assert map_room.go('123') == Freeza_World
    assert map_room.go('*') == Boxmap_Death
    # next room
    available_path1 = name_room(Freeza_World)
    available_path2 = name_room(Boxmap_Death)
    assert available_path1 == "freeza_world"
    assert available_path2 == "bomb_death"

    # Freeza  Room
    freeza_room = load_room(available_path1)
    assert freeza_room.name == "Freeza World"
    assert freeza_room.go('player go up') == Freezas_Forest
    # next room
    available_path = name_room(Freezas_Forest)
    assert available_path == "freezas_forest"


    # Freezas Forest Room
    freezas_forest_room = load_room(available_path)
    assert freezas_forest_room.name == "Freezas Forest"
    assert freezas_forest_room.go("player go left") == Freezas_Grounds
    # next room
    available_path = name_room(Freezas_Grounds)
    assert available_path == "freezas_grounds"

    # Freezas Grounds Room
    freezas_grounds_room = load_room(available_path)
    assert freezas_grounds_room.name == "Freezas Grounds"
    assert freezas_grounds_room.go("player next play") == Enemy_Defeated
    assert freezas_grounds_room.go("player go back") == Freezas_Forest
    assert freezas_grounds_room.go("*") == Defeat_Death
    assert freezas_grounds_room.go("player fight play") == None
    #next room
    available_path1 = name_room(Enemy_Defeated)
    available_path2 = name_room(Freezas_Forest)
    available_path3 = name_room(Defeat_Death)
    assert available_path1 == "enemy_defeated"
    assert available_path2 == "freezas_forest"
    assert available_path3 == "defeat_death"

    



    


