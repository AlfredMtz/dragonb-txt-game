import pytest
from dragonb_game.parser import *
from dragonb_game.lexicon import *


def test_parser_input():
    # First couple of steps
    play_game = parse_sentence(scan('yes')).__str__()
    dont_play_game = parse_sentence(scan('no')).__str__()
    next_move  = parse_sentence(scan('next')).__str__()
    assert play_game == 'player yes play'
    assert dont_play_game == 'player no play'
    assert next_move == 'player next play'
    
    # Directions
    # Up
    going_up0 = parse_sentence(scan('go up')).__str__()
    going_up1 = parse_sentence(scan('up')).__str__()
    assert going_up0 == 'player go up'
    assert going_up1 == 'player go up'

    # Down
    going_down0 = parse_sentence(scan('go down')).__str__()
    going_down1 = parse_sentence(scan('down')).__str__()
    assert going_down0 == 'player go down'
    assert going_down1 == 'player go down'

    # Left
    going_left0= parse_sentence(scan('go left')).__str__()
    going_left1 = parse_sentence(scan('left')).__str__()
    assert going_left0 == 'player go left'
    assert going_left1 == 'player go left'

    # Right
    going_right0 = parse_sentence(scan('go right')).__str__()
    going_right1= parse_sentence(scan('right')).__str__()
    assert going_right0 == 'player go right'
    assert going_right1 == 'player go right'
    
    


