#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import models
from models.user import User

def parse(arg):
    """
    Splits the input argument and return a list of components.
    """
    return arg.split()


"""
Defines the HBNBCommand(cmd.Cmd):
"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel
            "User": User
            }

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

    def do_create(self, className=None):
        """
        Creates a new instance of BaseModel and prints its id
        """
        if not className:
            print("** class name missing **")
        elif not self.__classes.get(className):
            print("** class doesn't exist **")
        else:
            obj = self.__classes[className]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string rep of an instance based on the class name and id
        """
        arg = parse(arg)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        arg = parse(arg)
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string rep of all instances based or not on the
        class name
        """
        if not arg:
            print([str(value) for key, value in models.storage.all().items()])
        else:
            if not self.__classes.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(value) for key, value in models.storage.all().items()
                  if type(value) is self.__classes.get(arg)])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arg = parse(arg)
        objdict = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
            return False

        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(arg) == 1:
            print("** instance id missing **")
            return False

        if "{}.{}".format(arg[0], arg[1]) not in objdict.keys():
            print("** no instance found **")
            return False

        if len(arg) == 2:
            print("** attribute name missing **")
            return False

        if len(arg) == 3 and not isinstance(eval(arg[2]), dict):
            print("** value missing **")
            return False

        if len(arg) == 4:
            obj = objdict["{}.{}".format(arg[0], arg[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valuetype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valuetype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
        elif isinstance(eval(arg[2]), dict):
            obj = objdict["{}.{}".format(arg[0], arg[1])]
            for m, n in eval(arg[2]).items():
                if (m in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[m]) in {str, int, float}):
                    valuetype = type(obj.__class__.__dict__[m])
                    obj.__dict__[m] = valuetype(n)
                else:
                    obj.__dict__[m] = n
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
