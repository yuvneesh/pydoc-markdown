<a id="script_4"></a>

# script\_4

We use this module to greet the user running this module

<a id="script_4.helpers"></a>

## helpers

<a id="script_4.datetime"></a>

## datetime

<a id="script_4.greeting"></a>

#### greeting

```python
def greeting() -> str
```

Returns the time-appropriate greeting

<a id="script_4.message"></a>

#### message

```python
def message(name: str, greeting: str) -> str
```

Returns a message string

**Arguments**:

- `name` _str_ - The name of the user
- `greeting` _str_ - The greeting to be user

**Returns**:

  A greeting message that can be show to user
  

**Todo**:

  * Make the name Initial case.
  * Missing greetings for 11pm - 5 am

<a id="script_4_support"></a>

# script\_4\_support

This module contains supporting functions.

<a id="script_4_support.os"></a>

## os

<a id="script_4_support.get_user_name"></a>

#### get\_user\_name

```python
def get_user_name() -> str
```

Returns the username executing the file.

**Returns**:

  The username

