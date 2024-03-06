"""This module contains supporting functions.
"""
import os

class Script4Support:
    def __init__(self):
        pass

    def get_user_name(self) -> str:
        """Returns the username executing the file.
        
        Returns:
            The username
        """
        cwd = os.getcwd()
        cwd = cwd[7:]
        end = cwd.find("/")
        cwd = cwd[:end]
        return cwd
