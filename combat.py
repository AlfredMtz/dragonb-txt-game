import random
from textwrap import dedent    

'''
Combat system function 'attack()', two parameter given (Player Character Class, Enemy Character Class)
return weather player win, lose, or exits the game
'''

def attack(player_class, enemy_class):
    Player = player_class
    Enemy = enemy_class
    
    print("\nOk,Ready!!")
    print(f"{Player.name}'s health:{Player.health} | {Enemy.name}'s health:{Enemy.health}")

    while Player.health >= 10 and Enemy.health >= 10:
        print(dedent('''
        SELECT ACTION:
        1.) Attack
        2.) Ask a question
        3.) Exit game
        '''))
        action = input("Answer #: ")
        if action == '1':
            # Player's attack
            print("YOU ATTACKED")
            player_attack = random.choice([Player.attack//2, Player.attack])
            enemy_attack = random.choice([Enemy.attack//2, Enemy.attack])

            print(f"{Player.name}'s current health:{Player.health}% | {Enemy.name}'s current health:{Enemy.health}%") 
            if player_attack == Player.attack//2:
                Player.health = Player.health - enemy_attack
                print(f"You missed! {Enemy.name} caused you a {Enemy.attack}% demaged")   
            else:
                Enemy.health = Enemy.health - Player.attack
                print(f"You caused {Enemy.name} a {player_attack}% demage")
            # Enemy's attack    
            print("\nENEMY ATTACKED")
            player_attack = random.choice([Player.attack//2, Player.attack])
            enemy_attack = random.choice([Enemy.attack//2, Enemy.attack])
                
            print(f"{Player.name}'s current health:{Player.health}% | {Enemy.name}'s current health:{Enemy.health}%")
            if enemy_attack == Enemy.attack//2:
                Enemy.health = Enemy.health - player_attack
                print(f"He missed! you attacked {Enemy.name} causing him a {Player.attack}% demaged")
            else:
                Player.health = Player.health - enemy_attack
                print(f"{Enemy.name} caused you a {Enemy.attack}% demage")
            
        elif action == '2':
            print("There is not time to ask questions!")
            print("One of his soldiers stabs you and you die!  Good bye!")
            exit()
        elif action == '3':
            print("You exited the game. Hope to see you soon, Goodbye!")
            exit()
        else:
            print("Sorry, I didn't understand that! Try again!")
            continue
            
    if Player.health < 10:
        #die()
        print("You die!")
        print("GAME OVER!")
        exit()
    elif Enemy.health < 10:
        print("\nYOU WIN!") 