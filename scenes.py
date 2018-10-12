from textwrap import dedent
import characters
import combat


class Scene(object):
    
    def enter(self):
        print("This is the parent class for all upcoming scenes subclasses")
        exit()

class Intro(Scene):
    
    def enter(self):
        print(dedent("""

        WELCOME TO DRAGONBZ TEXT GAME!!!

        This story begins in a very, very far planet named Vegeta which
        is about to be destroyed by powerful evil forces. A desperate
        father with little to no time puts his son into a spaceship 
        and sends it over into space and arrives into a new planetary
        destination named earth. 

        Years later he grows up, starts a family, and as he seems to be much
        stronger than average humans he finds a passion for helping people 
        escape the hands of evil villains. One day, returning home, he sees
        his entire village wiped out including his family.

        A survivor informs him that an evil dragon monster came in and took 
        the seven dragon balls which grand a single wish once a year.So, Goku 
        the warrior goes out to locate all seven dragon balls to bring them back 
        home and make a wish to have his family and village back to normality.

        Do you want to help by being Goku and start the quest of saving your 
        village and bring your family back to life?
        
        [ Yes / No ]

        """))

        action = input("> ")

        if action == "Yes":
            print(dedent("""
            Great!!!  You lose no time and start investigating where to find
            this evil dragon one and get back the dragon balls. You get informed
            that the evil dragon distributed two of the dragon balls to each of
            his best soldiers to keep them safe while he only held one.

            You quickly go out and find out that two of the dragon balls are
            held by one of this dragon's soldiers by the name of Freeza.
            
            Bravely you set out to space, find Freeza's planet and get ready to
            face him.
            """))
            return 'Freeza_world'
        
        else:
            print('GAME EXITED!')
            exit(1)

class Freezaworld(Scene):

    def enter(self):
        
        print(dedent('''
            You first find freeza's world and after fighting many of his
            guards, you are finally facing him!
            '''))
        while True:
            action = input("Are you ready to fight him? [Yes / No] >  ")

            if action == 'Yes':
                combat.attack(characters.Playerc(), characters.Freezac())
                return Cellworld()
            elif action == 'No':
                print("No rush, proceed when you are ready!")
                continue
            else:
                print("Sorry, I din't understand that. Try again!")
                continue  
    
class Cellworld(Scene):

    def enter(self):
        print("Now you are facing Cell!!")

        while True:
            action = input("Are you ready to fight him? [Yes / No] >  ")
            
            if action == 'Yes':
                combat.attack(characters.Playerc(), characters.Cellc())
                return 'Majimbu_world'
            elif action == 'No':
                print("No rush, proceed when you are ready!")
                continue
            else:
                print("Sorry, I din't understand that. Try again!")
                continue  
        

class Majimbuworld(Scene):

    def enter(self):
        print("worksssssss")

class Dragonworld(Scene):
    pass

class Makingwish(Scene):
    pass

class Death(Scene):
    pass

class Completed(Scene):
    pass

