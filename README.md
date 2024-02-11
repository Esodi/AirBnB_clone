**0x00. AirBnB clone - The console**
Description

This project is a command-line interpreter(CLI) designed to give an interface.
It allows users to execute various commands for managing data.

Command Interpreter
How to Start

To start the command interpreter, follow these steps:

    - Clone the repository to your local machine.
    - Navigate to the project directory.
    - Run the command `python3 console.py` to start the interpreter.

How to Use

Once the interpreter is running, you can enter commands to perform actions.
The commands are structured as follows:

    `command [options] [arguments]`

Replace command with the desired actions.
Examples

Here are some examples of commands you can use with the interpreter:

1. Create a new instance:

    `create BaseModel`

This command creates a new instance of the BaseModel class.

2. Show an instance:

    `show BaseModel 1234-5678`

This command prints the string representation of the instance with the ID.

3. Delete an instance:

    `destroy BaseModel 1234-5678`

This command deletes the instance with the specified ID.

4. Update an instance:

    `update BaseModel 1234-5678 name "New Name"`

This command updates the attribute "name" with ID to the value "New Name".

5. Print all instances:

    `all BaseModel`

This command prints the string representations of all instances.
