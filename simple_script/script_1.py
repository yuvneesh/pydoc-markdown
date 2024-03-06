import os

class Script1:
    def __init__(self):
        # This is just a simple comment before a variable.
        # This won't be registered in documentation
        variable_without_docstring = "Hi, World"

        #: This is a special comment.
        #: We can use this to tell us about the variable in use i.e. name
        name = "Yuvneesh"

        # Alternatively, we can add as many lines of comment we want.
        # It will work as long as the last line has "#:" symbol.
        #:
        last_name = "Kashyap"

        #: Without a variable, this won't do anything.
        print(name + last_name)
