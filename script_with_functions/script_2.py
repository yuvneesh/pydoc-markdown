class Script2:
    def __init__(self):
        pass
    def intro(self):
        """This is the function intro. 
        It will print few lines from variables defined in the function.

        Note that the docstring for variables defined within the function are not printed.
        """
        #: The first line to be printed
        first_line = "This is a simple function that has no parameters."

        #: The second line to be printed
        second_line = "There are however function-level variables."

        print(first_line)
        print(second_line)


    def func_with_args(self, name: str, greeting: str) -> None:
        """Here we have a function that takes two string arguments
        """
        print(f"Hello {name}! \n{greeting}")


    def age_calculator(self, date_of_birth: str, current_year: int, current_month: int, current_day: int) -> int:
        """Returns the age based on the #date_of_birth, **current_year**, **current_month**, and **current_day**

        Args:
            date_of_birth: The date of birth as a string
            current_year: must be of format YYYY
            current_month: must not have leading zeroes
            current_day: must not have leading zeroes

        Returns:
            age: The age as of today
        """
        dob = date_of_birth.split("-")
        year_diff = current_year - int(dob[0])
        month_diff = current_month - int(dob[1])
        day_diff = current_day - int(dob[2])

        age = year_diff

        if month_diff < 0:
            age -= 1
        elif month_diff == 0 and day_diff < 0:
            age -= 1

        return age

# intro()
# func_with_args("Yuvneesh", "Congrats on starting a new journey :)")
# print(f"You are {age_calculator('1999-03-11', 2024, 3, 5)} years old")
