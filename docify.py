from __future__ import annotations
from modular_scripts.script_4 import Script4
from modular_scripts.script_4_support import Script4Support

class Docify:
    """An example class consisting of instances of other classes in the project.
    
    Note: It is not a good practice to write the docstring for a class as "This is a class for..."
    Remember: DRY - Don't Repeat Yourself

    Attributes:
        get_name (function): A function to obtain the name of the user
        greeting (str): THe greeting to be used to greet the user
    """

    def __init__(self, name_getter: function, greeting: str):
        self.get_name = name_getter
        self.greeting = greeting

    def greet(self) -> None:
        """Greets the user"""
        print(f"Hi {self.get_name()}, {self.greeting}")

zd = Docify(Script4Support().get_user_name, Script4().greeting())
zd.greet()
