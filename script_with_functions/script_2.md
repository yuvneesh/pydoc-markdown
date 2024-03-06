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

