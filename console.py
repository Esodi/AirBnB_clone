#!/usr/bin/python3
"""HBNB console application for airbnb"""

import cmd
from datetime import datetime
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """This is command line interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, argument):
        """Exit console"""
        return True

    def do_EOF(self, argument):
        """Exit console on EOF"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        try:
            if not arg:
                print("** class name missing **")
                return
            class_name = arg.split()[0]
            if class_name not in [
                    "BaseModel",
                    "User",
                    "Place",
                    "State",
                    "City",
                    "Amenity",
                    "Review"
                    ]:
                print("** class doesn't exist **")
                return
            if class_name == "BaseModel":
                module = __import__(
                        'models.' + 'base_model',
                        fromlist=['base_model']
                        )
            else:
                module = __import__(
                        'models.' + class_name.lower(),
                        fromlist=[class_name]
                        )
            class_ = getattr(module, class_name)
            storage = FileStorage()
            new_instance = class_()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the ID and value of instances based on class name"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
                key = "{}.{}".format(class_name, instance_id)
                if key in data:
                    for j in data[key]:
                        if j in ['created_at', 'updated_at']:
                            data[key][j] = datetime.fromisoformat(data[key][j])
                    print("[{}] ({}) {}\
".format(class_name, instance_id, data[key]))
                else:
                    print("** no instance found **")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        try:
            if not arg:
                print("** class name missing **")
                return
            args = arg.split()
            class_name = args[0]
            if class_name not in [
                    "BaseModel",
                    "User",
                    "Place",
                    "State",
                    "City",
                    "Amenity",
                    "Review"
                    ]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            try:
                with open("file.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = {}
            key = f"{class_name}.{instance_id}"
            if key not in data:
                print("** no instance found **")
                return
            del data[key]
            with open("file.json", "w") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representations of instances"""
        class_name = None
        lst = []
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
                if not arg:
                    instances = data.values()
                else:
                    args = arg.split()
                    class_name = args[0]
                    if class_name not in [
                            "BaseModel",
                            "User",
                            "Place",
                            "State",
                            "City",
                            "Amenity",
                            "Review"
                            ]:
                        print("** class doesn't exist **")
                        return
                    instances = ([value for key,
                                  value in data.items()
                                  if key.startswith(class_name + ".")])
                if not instances:
                    lst = []
                    print(lst)
                    return
                for i in instances:
                    for j in i:
                        if j in ['created_at', 'updated_at']:
                            i[j] = datetime.fromisoformat(i[j])
                    lst.append(f"[{i['__class__']}] ({i['id']}) {i}")
                print(lst)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("[]")

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        try:
            with open("file.json", "r+") as file:
                data = json.load(file)
                key = "{}.{}".format(class_name, instance_id)
                if key in data:
                    instance_data = data[key]
                    instance_data[attribute_name] = eval(attribute_value)
                    with open("file.json", "w") as file:
                        data[key] = instance_data
                        json.dump(data, file, indent=4)
                else:
                    print("** no instance found **")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
