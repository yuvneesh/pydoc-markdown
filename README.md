<a id="docify"></a>

# docify

<a id="docify.Script4"></a>

## Script4

<a id="docify.Script4Support"></a>

## Script4Support

<a id="docify.Docify"></a>

## Docify Objects

```python
class Docify()
```

An example class consisting of instances of other classes in the project.

Note: It is not a good practice to write the docstring for a class as "This is a class for..."
Remember: DRY - Don't Repeat Yourself

**Attributes**:

- `get_name` _function_ - A function to obtain the name of the user
- `greeting` _str_ - THe greeting to be used to greet the user

<a id="docify.Docify.greet"></a>

#### greet

```python
def greet() -> None
```

Greets the user

<a id="docify.zd"></a>

#### zd

<a id="script_1"></a>

# script\_1

<a id="script_1.Script1"></a>

## Script1 Objects

```python
class Script1()
```

<a id="script_2"></a>

# script\_2

<a id="script_2.Script2"></a>

## Script2 Objects

```python
class Script2()
```

<a id="script_2.Script2.intro"></a>

#### intro

```python
def intro()
```

This is the function intro.
It will print few lines from variables defined in the function.

Note that the docstring for variables defined within the function are not printed.

<a id="script_2.Script2.func_with_args"></a>

#### func\_with\_args

```python
def func_with_args(name: str, greeting: str) -> None
```

Here we have a function that takes two string arguments

<a id="script_2.Script2.age_calculator"></a>

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

<a id="script_3.sys"></a>

## sys

<a id="script_3.Path"></a>

## Path

<a id="script_3.s"></a>

## s

<a id="script_3.Script3"></a>

## Script3 Objects

```python
class Script3()
```

<a id="script_3.Script3.where_am_i"></a>

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

<a id="script_4.datetime"></a>

## datetime

<a id="script_4.Script4"></a>

## Script4 Objects

```python
class Script4()
```

<a id="script_4.Script4.greeting"></a>

#### greeting

```python
def greeting() -> str
```

Returns the time-appropriate greeting

<a id="script_4.Script4.message"></a>

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

<a id="script_4_support.Script4Support"></a>

## Script4Support Objects

```python
class Script4Support()
```

<a id="script_4_support.Script4Support.get_user_name"></a>

#### get\_user\_name

```python
def get_user_name() -> str
```

Returns the username executing the file.

**Returns**:

  The username

