#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class inherits from cmd.CMD"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line oes nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
