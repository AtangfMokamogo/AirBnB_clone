#!/usr/bin/env python3
"""Command interpreter for the HBNB project"""

import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""

    prompt = '(hbnb) '

    valid_classes = {
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review'}

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objs = []

        if not args:
            for obj in storage.all().values():
                objs.append(str(obj))
        elif args[0] in self.valid_classes:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    objs.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        print("[{}]".format(", ".join(objs)))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        # Check if attr_value is a string with a space between double quotes

        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        # Convert attr_value to its appropriate type
        try:
            attr_value = int(attr_value)

        except ValueError:
            try:
                attr_value = float(attr_value)

            except ValueError:
                pass  # leave attr_value as a string

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == arg:
                count += 1

        print(count)

    def default(self, arg):
        """Called when an invalid command is entered"""
        args = arg.split(".")
        if len(args) != 2:
            print("*** Unknown syntax: {}".format(arg))
            return

        if len(args) == 2:
            class_name = args[0]
            method_name = args[1].split('(')[0]
            if class_name in self.valid_classes and method_name == 'destroy':
                id_str = args[1].split('(')[1].split(')')[0]
                if id_str:
                    self.do_destroy('{} {}'.format(class_name, id_str))
                    return
            if class_name in self.valid_classes and method_name == 'show':
                id_str = args[1].split('(')[1].split(')')[0]
                if id_str:
                    self.do_show('{} {}'.format(class_name, id_str))
                    return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if args[1] != "all()" and args[1] != "count()":
            print("*** Unknown syntax: {}".format(arg))
            return

        objs = []
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                objs.append(obj)

        if args[1] == "all()":
            print("[{}]".format(", ".join(str(obj) for obj in objs)))
        else:
            print(len(objs))

    def precmd(self, line):
        """Prepares the line to be interpreted"""
        in_quotes = False
        for i, char in enumerate(line):
            if char == '"':
                in_quotes = not in_quotes

            elif char == '.' and not in_quotes:
                cmd, arg = line[:i], line[i+1:]
                line = "{} {}".format(cmd.strip(), arg.strip())
                break
            return line

    def postcmd(self, stop, line):
        """Executes after a command is interpreted"""
        storage.save()
        return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
