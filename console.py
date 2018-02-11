#!/usr/bin/python3
"""
   This module contains the entry point into the AirBnB command interpreter.
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This is the class definition of the command interpreter."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                a = arg + "()"
                new = eval(a)
                new.save()
                print(new.id)
            except:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit out of the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Quit out of the command interpreter with EOF"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
