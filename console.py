#!/usr/bin/python3
"""
   This module contains the entry point into the AirBnB command interpreter.
"""
import cmd
from models.engine.file_storage import FileStorage
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """This is the class definition of the command interpreter."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new = models.c_manager[arg]()
                new.save()
                print(new.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        jesse = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        else:
            if jesse[0] not in models.c_manager:
                print("** class doesn't exist **")
            elif len(jesse) == 1:
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
            jesse = shlex.split(arg)
            if jesse[0] not in models.c_manager:
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
        jesse = shlex.split(arg)
        obj_list = []
        store = FileStorage()
        obj = store.all()
        if len(jesse) == 0:
            for key, value in obj.items():
                obj_list.append(value)
            print(obj_list)
        elif jesse[0] not in models.c_manager:
            print("** class doesn't exist **")
        else:
            for key, value in obj.items():
                if jesse[0] in key:
                    obj_list.append(value)
            print(obj_list)

    def do_update(self, arg):
        """update instance based on the class name and id"""
        jesse = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif jesse[0] not in models.c_manager:
            print("** class doesn't exist **")
        elif len(jesse) == 1:
            print("** instance id missing **")
        else:
            store = FileStorage()
            obj = store.all()
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

    def emptyline(self):
        """ignores an empty line"""
        pass

    #def precmd(self, line):
    #    """checks commands for different type"""
    #    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
