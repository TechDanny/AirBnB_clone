#!/usr/bin/python3
import cmd


"""
Defines the HBNBCommand(cmd.Cmd):
"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Does not execute anything
        """
        pass

    def do_quit(self, line):
        """
        Exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
