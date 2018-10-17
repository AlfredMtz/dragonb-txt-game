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
        his entire village wiped out, including his family.

        A survivor informs him that an evil dragon came in and took 
        the seven dragon balls which grand a single wish once a year.So, Goku 
        the warrior goes out to locate all seven dragon balls to bring them back 
        home and make a wish to have his family and village back to normality.

        Would you like to get on Goku's shoes and start the quest to saving your 
        village and bring your family back to life?
        
        [ Yes / No ]

        """))

        action = input("> ")

        if action == "Yes":
            print(dedent("""
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
            """))
            return 'Freeza_world'
        
        else:
            print('GAME EXITED!')
            exit(1)

class FreezaWorld(Scene):

    def enter(self):
        
        print(dedent('''
            After several hours you find Freeza's planet, landed and turns out he
            was already waiting for your arrival. He knows what you are there for
            and he is ready to fight you!
            '''))
        while True:
            action = input(f"Are you ready to fight {characters.Freeza().name}? [Yes / No] >  ")

            if action == 'Yes':
                combat.attack(characters.Player(), characters.Freeza())
                print(dedent('''
                He pleads for mercy and gives you the 2 dragon balls he had. You decide
                to leave him alive as long as he tells you the quickest route to
                Cell's planet which is another of these dragon's best soldiers. So
                he ends up telling you where to find him and you move fastly on to 
                find this warrior named Cell!
                '''))
                return 'Cell_world'
            elif action == 'No':
                print("No rush, proceed when you are ready!")
                continue
            else:
                print("Sorry, I din't understand that. Try again!")
                continue  
    
class CellWorld(Scene):

    def enter(self):
        print(dedent('''
        You arrive to Cell's planet and battled with two androids that 
        were trying to stop you from reaching to Cell's place. You end 
        up defeating them and reached to Cell. He refuses to give
        you the 2 dragon balls you came in for!!
        '''))

        while True:
            action = input(f"Are you ready to fight {characters.Cell().name}? [Yes / No] >  ")
            
            if action == 'Yes':
                combat.attack(characters.Player(), characters.Cell())
                print(dedent('''
                GREAT JOB!
                Cell was destroyed after the last attack, so you did not
                get a chance to ask him where to find the third soldier. You
                picked up the 2 dragon balls he had and set out to try to find
                this oponent yourself!
                '''))
                return 'Secret_box'
            elif action == 'No':
                print("No rush, proceed when you are ready!")
                continue
            else:
                print("Sorry, I din't understand that. Try again!")
                continue  

class SecretBox(Scene):

    def enter(self):
        print(dedent('''
        While searching for this third soldier, you get across a wizard
        who tells you about a secret box a couple miles away which contains
        the addresses of all of these dragon's soldiers. So you set out to
        find this box!
        
        You finally arrive and find this secret box to be lock, so you need to
        guess the right 3 digit password withing the first 10 times or the box
        will explode and return back time to have you fight Cell again! You
        decide to give a shot and try to open the box
        '''))

        key_num = 123
        count = 0

        while True:
            
            code = int(input("Code: "))
            
            if code != key_num:
                print("Wrong code, try again!")
                count += 1
                if count == 10:
                    print(dedent('''
                    The secret box exploded and you are sent back
                    in time to fight Cell again!
                    '''))
                    return 'Cell_world'
                else:
                    continue
            else:
                print(dedent('''
                Great, you unlocked the box and quickly find the address of the
                last soldier which goes by the name of Majimbu and its 
                not too far away from where you are. You quickly set out in space 
                in his direction!
                '''))
                return 'Majimbu_world'


class MajimbuWorld(Scene):

    def enter(self):    
        print(dedent('''
        As you enter majinbuu's world you are face with Dabura the king of the Demond
        Realm and have a long fight, but you end up defeating him. You then travel
        further into the planet and find majinbuu eating and completly ignoring you.

        You take away his food and now he is furious and want to fight you!
        '''))

        while True:
            action = input("Are you ready to fight him? [Yes / No] >  ")
            
            if action == 'Yes':
                combat.attack(characters.Player(), characters.Majimbu())
                print(dedent('''
                You beat majimbuu and you have now 6 dragon balls. You are now ready to
                find this evil dragon which is holding the last dragon ball.
                '''))
                return 'Dragon_world'
            elif action == 'No':
                print("No rush, proceed when you are ready!")
                continue
            else:
                print("Sorry, I din't understand that. Try again!")
                continue 

class DragonWorld(Scene):
    
    def enter(self):
        print(dedent('''
        After three days you finally find his location and go straight to his 
        castle. He is a brave oponent and comes out from his castle rather 
        having his troopers help him!
        '''))

        while True:
            action = input("Are you ready to fight him? [Yes / No] >  ")
            
            if action == 'Yes':
                combat.attack(characters.Player(), characters.Dragon())
                print(dedent('''
                YOU BEAT THE EVIL DRAGON!!
                You take the last dragon ball and set back home!
                '''))
                return 'Make_wish'
            elif action == 'No':
                print("No rush, proceed when you are ready!")
                continue
            else:
                print("Sorry, I din't understand that. Try again!")
                continue 

class MakingWish(Scene):

    def enter(self):
        print(dedent('''
        You arrived home and quickly call shenron to come out and grand
        you a wish! He goes out in the sky and asks you what your wish is.
        You let him know you want your village and family back the way it
        was before that evil dragon came in and destroyed everything!

        He says -"That is easy, wish granded!"

        Your family run into your arms and say how much they missed you, as
        you get many many thanks for everyone in the village.

        You live happly ever after and keep your word the keep
        everyone safe from any future treat.
        '''))
        return 'Completed'
    
class Completed(Scene):
    
    def enter(self):
        print(dedent('''
        YOU FINISHED THE WHOLE GAME. GOOD JOB!
        HOPE TO SEE YOU SOON!
        '''))

        action = input("Do you want to play again: ")

        if action == 'Yes':
            pass
        else:
            print('Good Bye!!')
            exit()


