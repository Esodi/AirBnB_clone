#!/usr/bin/python3
"""HBNB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is command line interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, argument):
        """Exit console"""
        return True

    def do_EOF(self, argument):
        """Exit console on EOL"""
        print()
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Exit console on EOL")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
