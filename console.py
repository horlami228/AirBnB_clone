#!/usr/bin/python3
"""
    This module defines the shell
    interactive console
"""

import cmd
import re
import models
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Defines a class HBNBCommand that inherits
        from the Cmd Class
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, line):
        """quit program"""
        return True

    def do_EOF(self, line):
        """ end with a new line"""
        print()
        return True

    def help_quit(self):
        """helper for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """helper for EOF"""
        print("EOF command to exit the program")

    def emptyline(self):
        """do nothing for empty line"""
        pass

    def validate_line(self, line):
        """ Validate not empty line"""
        if line == "":
            print("** class name missing **")
            return False

    def validate_base_model(self, line):
        """validate class name"""
        parts = line.split(" ")
        if parts[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(parts) == 1 and parts[0] == "BaseModel":
            print("** instance id missing **")
            return False

    def validate_id(self, line):
        """validate the id"""
        parts = line.split(" ")
        model_id = "{}.{}".format(parts[0], parts[1])
        all_object = models.storage.all()
        if model_id not in all_object.keys():
            print("** no instance found **")
            return False

    def validate_attribute_value(self, line):
        """ validate the attribute and value"""
        parts = line.split(" ")
        if len(parts) == 2:
            print("** attribute name missing **")
            return False
        elif len(parts) == 3:
            print("** value missing **")
            return False

    def do_create(self, line):
        """ create new class instance"""
        check = self.validate_line(line)
        if check is False:
            return
        if line == "BaseModel":
            base_model = BaseModel()
            base_model.save()
            print(base_model.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """helper function for create doc"""
        print("Create command to make a new BaseModel Instance")

    def do_show(self, line):
        """Show object string representation"""
        check = self.validate_line(line)
        if check is False:
            return
        check = self.validate_base_model(line)
        if check is False:
            return
        check = self.validate_id(line)
        if check is False:
            return
        else:
            parts = line.split(" ")
            model_id = "{}.{}".format(parts[0], parts[1])
            get_obj = models.storage.all()
            print(get_obj[model_id])

    def help_show(self):
        """helper function for show"""
        print("Show Command to"
              " Print the string repr of an instance based"
              " on the class name and id")

    def do_destroy(self, line):
        """Destroy an object"""
        check = self.validate_line(line)
        if check is False:
            return

        check = self.validate_base_model(line)
        if check is False:
            return

        check = self.validate_id(line)
        if check is False:
            return

        else:
            parts = line.split(" ")
            model_id = "{}.{}".format(parts[0], parts[1])
            get_obj = models.storage.all()
            del get_obj[model_id]
            models.storage.save()

    def help_destroy(self):
        """Helper function for destroy"""
        print("destroy command"
              " deletes an instance based on the"
              " class name and id")

    def do_all(self, line):
        """print all objects available"""
        if line == "BaseModel" or line == "":
            get_obj = models.storage.all()
            all_obj = ["{}".format(value) for value in get_obj.values()]
            print(all_obj)
        else:
            print("** class doesn't exits **")

    def help_all(self):
        """helper for all"""
        print("all command prints all instances"
              " in a list format")

    def do_update(self, line):
        """update <class name> <id> <attribute name> '<attribute value>'"""

        check = self.validate_line(line)
        if check is False:
            return

        check = self.validate_base_model(line)
        if check is False:
            return

        check = self.validate_id(line)
        if check is False:
            return

        check = self.validate_attribute_value(line)
        if check is False:
            return

        else:
            parts = line.split(" ")
            model_id = "{}.{}".format(parts[0], parts[1])
            attr_name = parts[2]
            attr_val = parts[3].strip('"')  # remove the forward slash

            if attr_val.isdigit():
                attr_val = int(attr_val)
            else:
                try:
                    attr_val = float(attr_val)
                except Exception:
                    pass

            get_obj = models.storage.all()
            setattr(get_obj[model_id], attr_name, attr_val)
            get_obj[model_id].save()

    def help_update(self):
        """helper for update"""
        print("command updated to update with attribute")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
