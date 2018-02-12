#!/usr/bin/python3
"""
   This module contains the entry point into the AirBnB command interpreter.
"""
import cmd
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """This is the class definition of the command interpreter."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                #a = arg + "()"
                #new = eval(a)
                #new.save()
                #print(new.id)
                new = models.c_manager[arg]()
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
            elif len(jesse) < 2:
                print("** instance id missing **")
            else:
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

    def do_all(self, arg):
        """Prints the string representation of an instance."""
        jesse = parse(arg)
        obj_list = []
        if jesse and not instance_list(jesse[0]):
            print("** class doesn't exist **")
        elif jesse and instance_list(jesse[0]):
            name = jesse[0]
            store = FileStorage()
            obj = store.all()
            arg_len = len(name)
            for key, value in obj.items():
                if key[:arg_len] == name:
                    obj_list.append(value)
            print(obj_list)
        else:
            store = FileStorage()
            obj = store.all()
            for key, value in obj.items():
                obj_list.append(value)
            print(obj_list)

    def do_update(self, arg):
        """update instance based on the class name and id"""
        # TODO created_at, update_at, id may need to be protected
        # TODO if the tests try to change these values
        store = FileStorage()
        obj = store.all()
        key = ""
        if not arg:
            print("** class name missing **")
        else:
            jesse = parse(arg)
            if not instance_list(jesse[0]):
                print("** class doesn't exist **")
            elif len(jesse) < 2:
                print("** instance id missing **")
            key = jesse[0] + "." + jesse[1]
            if len(jesse) < 4 and len(jesse) > 2:
                if key in obj:
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                if key not in obj:
                    print("** no instance found **")
                else:
                    setattr(obj[key], jesse[2], jesse[3])
                    obj[key].save()

    def do_quit(self, arg):
        """Quit out of the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Quit out of the command interpreter with EOF"""
        print()
        return True


def emptyline():
    """ignores an empty line"""
    pass


def parse(arg):
    """Parse the string passed to a command"""
    return(tuple(map(str, arg.split())))


def instance_list(arg):
    """Master list of all instance types"""
    master_list = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
    if arg not in master_list:
        return False
    else:
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
