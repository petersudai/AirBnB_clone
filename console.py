#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class inherits from cmd.CMD"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

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
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            new_instance = eval(class_name_)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("**  class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist**")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '_' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string rep of all instances
        """
        objects = storage.all()
        if arg:
            try:
                objects = {
                    k: v for k, v in objects.items()
                    if v.__class__.__name__ == arg
                }
            except AttributeError:
                print("**class doesn't exiat **")
                return
            print([str(v) for v in objects.values()])

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribbute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
