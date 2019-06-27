import pytest
from dragonb_game.planisphere import *



def test_dragonb_game_map():
    # Intro room
    start_room = load_room(START)
    assert start_room.name == "Intro"
    assert start_room.go('no') == Intro
    assert start_room.go('yes') == Zuno_World
    # next room
    available_path = name_room(Zuno_World) 
    assert available_path == "zuno_world"



    # Zuno Room
    zuno_room = load_room(available_path)
    assert zuno_room.name == "Zuno World"
    assert zuno_room.go('next') == Freeza_World
    # next room
    available_path = name_room(Freeza_World)
    assert available_path == "freeza_world"


    # Freeza Room 
    freeza_room = load_room(available_path)
    assert freeza_room.name == "Freeza World"
    assert freeza_room.go('up') == Freezas_Forest
    # next room
    available_path = name_room(Freezas_Forest)
    assert available_path == "freezas_forest"


    # Freezas Forest Room
    freezas_forest_room = load_room(available_path)
    assert freezas_forest_room.name == "Freezas Forest"
    assert freezas_forest_room.go('down') == Freeza_World
    assert freezas_forest_room.go('left') == Dodorias_Grounds
    # next room
    available_path1 = name_room(Dodorias_Grounds)
    available_path2 = name_room(freezas_forest_room)
    assert available_path1 == "dodorias_grounds"
    assert available_path2 == "freezas_forest"


    # Dodorias Grounds Room
    dodorias_room = load_room(available_path1)
    assert dodorias_room.name == "Dodorias Grounds"
    assert dodorias_room.go("fight") == Fight_File
    assert dodorias_room.go("right") == Freezas_Forest



    


