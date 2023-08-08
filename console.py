#!/usr/bin/python3
import cmd


"""
Defines the HBNBCommand(cmd.Cmd):
    Attributes:
    prompt(str): The command prompt
"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do not execute anything when prompted
        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF signal to exit the program
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
