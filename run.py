from dragonb_game import app

'''
This will be the first script file run and will get the whole program
running, making the __name__ variable have the value of "__main__". Meaning the
starting point of the program(This is similar to the main method signature in
Java.) This is like saying if variable __name__ == "__main__" run the underlined
block of code; Else, if this is not the first script being run, but it shows as an
import within the script that is actually being run, then treat it as just an
import and set __name__ == run  -->which is the name of the file, and in turn not
executing the below line of code since at that point __name__ is not longer equals
to "__main__", but rather equals to "run", which is the name of the module.

The variable __name__ will always save its value to "__main__" within the first
script that you call/run directly.
'''
if __name__ == "__main__":
    # Conditon gets met and runs the following import
    app.run()
