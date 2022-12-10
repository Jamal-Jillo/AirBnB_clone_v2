#!/usr/bin/python3
"""Console module for the AirBnB project."""
import cmd
import models
import shlex  # For splitting arguments passed
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Place": Place, "Amenity": Amenity, "Review": Review}
# -- needs to be updated with all classes


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for AirBnB project."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help for quit command."""
        print("Type 'quit' command to exit the program")

# ! Does not work
    def do_clear(self, args):
        """Clear the console."""
        pass

    def do_EOF(self, args):
        """Use 'CTRL + D' command to exit the program."""
        return True

    def help_EOF(self):
        """Help for EOF command."""
        print("Use 'CTRL + D' command to exit the program")

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, line):
        """Create a new instance of a BaseModel."""
        # Functions of New codeBase
        # Will update this function to allow object
        # creation with given parameters
        # param syntax:
        # <class name> <param1 name>=<param1 value> <param2 name>=<param2
        # value> ...
        # create User name="jamal" age=25
        # Value syntax:
        #  - string: "<value>" must be surrounded by double quotes
        #   - any double quotes in the value must be escaped with a backslash
        #   - all underscores must be replaced with spaces
        # (e.g. "my_name" becomes "my name")
        #  - integer: <value> must be an integer
        #  - float: <unit>.<decimal> must be a float => contains a dot
        # if any param doesn't follow the syntax or cant be recognized,
        # it must be skipped

        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")  # Split arguments
            obj = eval("{}()".format(my_list[0]))
            # New code
            for index in range(1, len(my_list)):
                param_val = self.valid_param(my_list[index])
                # Validate parameter
                if param_val:
                    obj.__dict__[param_val[0]] = param_val[1]
            # End new code
            obj.save()
            print("successfully created {} model"
                  .format(obj.__class__.__name__))
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

        # ? Previous codebase
        # try:
        #    args = shlex.split(arg)
        #    if len(args) == 0:
        #        print("** class name missing **")
        #        # return False
        #    elif args[0] in classes:
        #        print(eval(args[0])().id)
        #        models.storage.save()
        #        print("** Created successfully! **")
        #    else:
        #        print("** class doesn't exist **")
        # except Exception:
        #    print("** class doesn't exist **")

    # New code
    def valid_param(self, arg):
        """Validate parameter and returns either None or a tuple."""
        if "=" not in arg:
            print("** No value for parameter '{}' **".format(arg))
            return None
        args = arg.split("=")
        param, value = args[0], args[1]
        try:
            value = eval(args[1])
        except Exception:
            return None
        if type(value) is str:
            value = value.replace("_", " ")
        return (param, value)
    # End new code

    def help_create(self):
        """Help for create command."""
        print("Create new instances of a class by using the <create> command\n\
            >>> create <class name>")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)  # Split arguments passed
        if len(args) == 0:  # If no arguments passed
            print("** class name missing **")
            return False
        if args[0] in classes:  # If class name is valid (in classes)
            if len(args) > 1:  # Check If id is passed
                # Create key to search for in storage
                key = args[0] + "." + args[1]
                # Check If key exists in storage
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """Help for show command."""
        print("Get the string representation of an instance\n\
            >>> show <class name> <id>")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)  # Split arguments passed
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                # Check If key exists in storage
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                    print("** Deleted successfully! **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_destroy(self):
        """Help for destroy command."""
        print("Delete an instance based on the class name and id\n\
            >>> destroy <class name> <id>")

    def do_all(self, arg):
        """Print all string representation of all instances."""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj_dict = []
            for obj in models.storage.all().values():
                # Checks if class name exists
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    # Append string representation of object
                    obj_dict.append(obj.__str__())
                elif len(args) == 0:  # For all objects
                    obj_dict.append(obj.__str__())
            # print(obj_dict) -- Rollback to this if not working
            # Added this Feature to print each object in a new line
            for i in range(len(obj_dict)):
                print(obj_dict[i])
                if i == len(obj_dict) - 1:
                    break

    def help_all(self):
        """Help for all command."""
        print("Print the string representation of all instances\n\
            >>> all <class name>")

    def do_update(self, arg):
        """
        Summary: Update an instance based on the class name and id.

        Update an instance based on the class name and
        id by adding or updating attribute.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key], args[2],
                                    args[3])
                            models.storage.save()
                            print("** Updated successfully! **")
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_update(self):
        """Help for update command."""
        print("Update an instance based on the class name and id")
        print(">> update <class name> <id> <attribute name> <attribute value>")
        print("Example: update User 1234-1234-1234 email user@email.com")

    def default(self, line):
        """Accept class name followed by command."""
        args = line.split(".", 1)
        class_args = args[0]
        if len(args) == 1:
            print("** Unknown syntax: {}".format(line))
            return
        try:
            args1 = args[1].split("(")
            command = args1[0]
            if command == "all":
                self.do_all(class_args)
            elif command == "count":
                self.do_count(class_args)
            elif command == "show":
                args = args1[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_args + " " + id_arg
                self.do_show(arg)
            elif command == "destroy":
                args = args1[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_args + " " + id_arg
                self.do_destroy(arg)
            elif command == "update":
                args = args1[1].split(')')
                args = args[0].split(',')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                attr_name = args[1]
                attr_name = attr_name.strip()
                attr_name = attr_name.strip("'")
                attr_name = attr_name.strip('"')
                attr_value = args[2]
                attr_value = attr_value.strip()
                attr_value = attr_value.strip("'")
                attr_value = attr_value.strip('"')
                arg = class_args + " " + id_arg + " " + attr_name + " " + \
                    attr_value
                self.do_update(arg)
            else:
                pass
        except IndexError:
            print("** Unknown syntax: {}".format(line))
            return

    def help_default(self):
        """Help for default command."""
        print("Accept class name followed by command")
        print(">>> <class name>.<command>")
        print("Example: BaseModel.all()")

    def do_count(self, arg):
        """Count the number of instances of a class."""
        if arg in classes:
            count = 0
            for obj in models.storage.all().values():
                if arg == obj.__class__.__name__:
                    count += 1
            print(count)

    def help_count(self):
        """Help for count command."""
        print("Count the number of instances of a class")
        print(">>> <class name>.count()")
        print("Example: BaseModel.count()")


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
