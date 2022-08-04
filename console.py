#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, arg):
        """Exit the program"""
        raise SystemExit

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
