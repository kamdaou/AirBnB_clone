#!/usr/bin/python3
"""Console module"""
import cmd
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_names = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    class_instances = {}

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """Exit the program"""
        raise SystemExit

    def emptyline(self):
        pass

    def do_create(self, class_name):
        """Creates an instance.
        """
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        else:
            self.__create(class_name)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = shlex.split(arg)
        key = args[0] + "." + args[1]
        HBNBCommand.class_instances = storage.all()
        if not args[0]:
            print("** class name missing **")
        elif self.__is_class(args[0]):
            print("** class doesn't exist **")
        elif self.__has_id(key):
            print("** instance id missing **")
        elif self.__is_class_found(key):
            print("** no instance found **")
        else:
            self.__show(args[0] + "." + args[1])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
        args = shlex.split(arg)
        key = args[0] + "." + args[1]
        HBNBCommand.class_instances = storage.all()
        if not args[0]:
            print("** class name missing **")
        elif self.__is_class(args[0]):
            print("** class doesn't exist **")
        elif self.__has_id(key):
            print("** instance id missing **")
        elif self.__is_class_found(key):
            print("** no instance found **")
        else:
            self.__destroy(args[0] + "." + args[1])

    def do_all(self, class_name):
        """Prints all string representation of all instances.
        """
        HBNBCommand.class_instances = storage.all()
        if not class_name:
            self.__all()
        elif class_name not in self.class_names:
            print("** class doesn't exist **")
        else:
            self.__all_of(class_name)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.
        """
        args = shlex.split(arg)
        key = args[0] + "." + args[1]
        HBNBCommand.class_instances = storage.all()
        if not args[0]:
            print("** class name missing **")
        elif self.__is_class(args[0]):
            print("** class doesn't exist **")
        elif self.__has_id(key):
            print("** instance id missing **")
        elif self.__is_class_found(key):
            print("** no instance found **")
        else:
            self.__update(key + "." + args[0], args[2], args[3])

    @staticmethod
    def __is_class(class_name):
        return class_name not in HBNBCommand.class_names.keys()

    @staticmethod
    def __has_id(class_name):
        return not HBNBCommand.class_instances[class_name]

    @staticmethod
    def __is_class_found(class_name):
        print(HBNBCommand.class_instances)
        return class_name not in HBNBCommand.class_instances

    @staticmethod
    def __create(class_name):
        class_instance = HBNBCommand.class_names[class_name]()
        class_instance.save()
        print(class_instance.id)

    @staticmethod
    def __show(class_name):
        print(str(HBNBCommand.class_instances[class_name]))

    @staticmethod
    def __destroy(class_name):
        del HBNBCommand.class_instances[class_name]
        storage.save()

    @staticmethod
    def __all():
        res = []
        for key, value in HBNBCommand.class_instances.items():
            res.append(str(value))
        print(json.dumps(res))

    @staticmethod
    def __all_of(class_name):
        res = []
        for key, value in HBNBCommand.class_instances.items():
            if class_name in key:
                res.append(str(value))
            print(json.dumps(res))

    @staticmethod
    def __update(key, attribute_name, attribute_value):
        temp = HBNBCommand.class_instances[key].__dict__
        if attribute_name in temp.keys():
            temp[attribute_name] = type(temp[attribute_name])(attribute_value)
        else:
            temp[attribute_name] = attribute_value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
