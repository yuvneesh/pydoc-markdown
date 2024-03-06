"""We use this module to greet the user running this module"""
import script_4_support as helpers
import datetime


def greeting() -> str:
    """Returns the time-appropriate greeting"""
    hour = datetime.datetime.now().hour
    if 5<hour<12:
        return "Good Morning"
    elif 12<hour<15:
        return "Good Afternoon"
    elif 15<hour<23:
        return "Burning the midnight oil?"


def message(name: str, greeting: str) -> str:
    """Returns a message string
    
    Args:
        name (str): The name of the user
        greeting (str): The greeting to be user
    Returns:
        A greeting message that can be show to user
    """
    return (f"{greeting} {name}")


print(message(helpers.get_user_name(), greeting()))
