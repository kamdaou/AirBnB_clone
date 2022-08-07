#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_names = ["BaseModel"]
    class_instances = []

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
            pass

    def do_show(self, class_name):
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        elif self.__has_id(class_name):
            print("** instance id missing **")
        elif self.__is_found(class_name):
            print("** no instance found **")
        eelse:
            pass

    def do_destroy(self, class_name):
        if not class_name:
            print("** class name missing **")
        elif self.__is_class(class_name):
            print("** class doesn't exist **")
        elif self.__has_id(class_name):
            print("** instance id missing **")
        elif self.__is_found(class_name):
            print("** no instance found **")
        else:
            pass

    def do_all(self, class_name):
        if class_name not in self.class_names:
            print("** class doesn't exist **")
        else:
            pass

    @staticmethod
    def do_update(self, class_name, id, attribute_name, attribute_value):
        pass

    @staticmethod
    def __is_class(class_name):
       return class_name not in self.class_names 

    @staticmethod
    def __has_id(class_name):
        return not self.class_instances[class_name].id

    @staticmethod
    def __is_found(class_name):
        return class_name not in self.class_instances


if __name__ == '__main__':
    HBNBCommand().cmdloop()
