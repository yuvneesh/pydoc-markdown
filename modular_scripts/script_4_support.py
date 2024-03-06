"""This module contains supporting functions.
"""
import os

def get_user_name() -> str:
    """Returns the username executing the file.
    
    Returns:
        The username
    """
    cwd = os.getcwd()
    cwd = cwd[7:]
    end = cwd.find("/")
    cwd = cwd[:end]
    return cwd
