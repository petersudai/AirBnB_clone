#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class inherits from cmd.CMD"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line oes nothing"""
        pass

    def do_create(self, arg):
        """
        Creates new instance of BaseModel, saves it and prints id
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** instance id missing **")
            return
        elif len(args) == 1:
            print("** instance idd missing **")
            return

        objects = models.storage.all()
        key = args[0] + "." + args[1]
        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        key = args[0] + "," + args[1]
        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string rep of all instances
        """
        objects = models.storage.all()
        if not arg:
            print([str(v) for v in objects.values()])
        elif arg in self.classes:
            print([str(v) for k, v in objects.items() if arg in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        objects = models.storage.all()
        key = args[0] + "." + args[1]
        if key not in objects:
            print("** no instance found **")
            return

        instance = objects[key]
        setattr(instance, args[2], args[3])
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
