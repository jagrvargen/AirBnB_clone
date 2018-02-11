#!/usr/bin/python3
"""
   This module contains the entry point into the AirBnB command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class definition of the command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit out of the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Quit out of the command interpreter with EOF"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
