<a id="script_1"></a>

# script\_1

<a id="script_1.os"></a>

## os

<a id="script_1.variable_without_docstring"></a>

#### variable\_without\_docstring

<a id="script_1.name"></a>

#### name

This is a special comment.
We can use this to tell us about the variable in use i.e. name

<a id="script_1.last_name"></a>

#### last\_name

Alternatively, we can add as many lines of comment we want.
It will work as long as the last line has "#:" symbol.

<a id="script_2"></a>

# script\_2

<a id="script_2.intro"></a>

#### intro

```python
def intro()
```

This is the function intro.
It will print few lines from variables defined in the function.

Note that the docstring for variables defined within the function are not printed.

<a id="script_2.func_with_args"></a>

#### func\_with\_args

```python
def func_with_args(name: str, greeting: str) -> None
```

Here we have a function that takes two string arguments

<a id="script_2.age_calculator"></a>

#### age\_calculator

```python
def age_calculator(date_of_birth: str, current_year: int, current_month: int,
                   current_day: int) -> int
```

Returns the age based on the #date_of_birth, **current_year**, **current_month**, and **current_day**

**Arguments**:

- `date_of_birth` - The date of birth as a string
- `current_year` - must be of format YYYY
- `current_month` - must not have leading zeroes
- `current_day` - must not have leading zeroes
  

**Returns**:

- `age` - The age as of today

<a id="script_3"></a>

# script\_3

Demonstrating how we can include names of imported modules in documentation.
Either we can use the filter processor with documented_only: false
OR we can use the google processor.

<a id="script_3.os"></a>

## os

<a id="script_3.sys"></a>

## sys

<a id="script_3.Path"></a>

## Path

<a id="script_3.s"></a>

## s

<a id="script_3.where_am_i"></a>

#### where\_am\_i

```python
def where_am_i(n: int) -> str
```

Tells your current workind directory **n** times

**Arguments**:

- `n` _int_ - The number of times you wanna know

**Returns**:

  A string with your pwd on multiple number of lines

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

