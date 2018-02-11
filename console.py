#!/usr/bin/python3
"""
   This module contains the entry point into the AirBnB command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
        else:
            jesse = parse(arg)
            if not instance_list(jesse[0]):
                print("** class doesn't exist **")
            try:
                len(jesse) > 2
            except:
                print("** instance id missing **")
            try:
                store = FileStorage()
                obj = store.all()
                key = jesse[0] + "." + jesse[1]
                print(obj[key])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            jesse = parse(arg)
            if not instance_list(jesse[0]):
                print("** class doesn't exist **")
            elif len(jesse) != 2:
                print("** instance id missing **")
            else:
                try:
                    store = FileStorage()
                    obj = store.all()
                    key = jesse[0] + "." + jesse[1]
                    del obj[key]
                    store.save()
                except:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Quit out of the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Quit out of the command interpreter with EOF"""
        print()
        return True


def parse(arg):
    """Parse the string passed to a command"""
    return(tuple(map(str, arg.split())))


def instance_list(arg):
    """Master list of all instance types"""
    master_list = ["BaseModel"]
    if arg not in master_list:
        return False
    else:
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
