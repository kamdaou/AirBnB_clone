#!/usr/bin/python3
"""Console module"""
import cmd
import json

from models import storage, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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

    def do_EOF(self, arg):
        """Exit the program"""
        raise SystemExit

    def emptyline(self):
        pass

    def do_create(self, class_name):
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        else:
            self.__create(class_name)

    def do_show(self, class_name):
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        elif self.__has_id(class_name):
            print("** instance id missing **")
        elif self.__is_class_found(class_name):
            print("** no instance found **")
        else:
            HBNBCommand.class_instances = storage.all()
            self.__show(class_name)

    def do_destroy(self, class_name):
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        elif self.__has_id(class_name):
            print("** instance id missing **")
        elif self.__is_class_found(class_name):
            print("** no instance found **")
        else:
            HBNBCommand.class_instances = storage.all()
            self.__destroy()

    def do_all(self, class_name):
        HBNBCommand.class_instances = storage.all()
        if class_name not in self.class_names:
            print("** class doesn't exist **")
        elif not class_name:
            self.__all()
        else:
            self.__all_of()

    def do_update(self, class_name, id, attribute_name, attribute_value):
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        elif self.__has_id(class_name):
            print("** instance id missing **")
        elif self.__is_class_found(class_name):
            print("** no instance found **")
        elif self.__is_class_found(class_name):
            print("** no instance found **")
        else:
            HBNBCommand.class_instances = storage.all()
            key = class_name + "." + id
            self.__update(key, attribute_name)

    @staticmethod
    def __is_class(class_name):
        return class_name not in HBNBCommand.class_names.keys()

    @staticmethod
    def __has_id(class_name):
        return not HBNBCommand.class_instances[class_name].id

    @staticmethod
    def __is_class_found(class_name):
        return class_name not in HBNBCommand.class_instances

    @staticmethod
    def __create(class_name):
        class_instance = HBNBCommand.class_names[class_name]()
        class_instance.save()
        print(class_instance.id())

    @staticmethod
    def __show(class_name):
        print(str(HBNBCommand.class_instances[class_name]))

    def __destroy(class_name):
        del HBNBCommand.class_instances[class_name]
        storage.save()

    def __all(self):
        res = []
        for key, value in HBNBCommand.class_instances.items():
            res.append(str(value))
        print(json.dumps(res))

    def __all_of(class_name):
        res = []
        for key, value in HBNBCommand.class_instances.items():
            if class_name in key:
                res.append(str(value))
            print(json.dumps(res))

    def __update(key, attribute_name, attribute_value):
        temp = HBNBCommand.class_instances[key].__dict__
        if attribute_name in temp.keys():
            temp[attribute_name] = type(temp[attribute_name])(attribute_value)
        else:
            temp[attribute_name] = attribute_value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
