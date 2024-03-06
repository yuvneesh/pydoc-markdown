"""
Demonstrating how we can include names of imported modules in documentation.
Either we can use the filter processor with documented_only: false 
OR we can use the google processor.
"""
import os
import sys
from pathlib import Path
import shutil as s


class Script3:
    def __init__(self):
        pass

    def where_am_i(self, n: int) -> str:
        """Tells your current workind directory **n** times
        
        Args:
            n (int): The number of times you wanna know
        Returns:
            A string with your pwd on multiple number of lines
        """
        s = ""
        for i in range(n):
            s += os.getcwd()
            s += "\n"
        s = s[:-1]
        return s

# print(where_am_i(3))