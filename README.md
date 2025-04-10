# CodeRoast

A Python library that insults programmers when their code throws errors. Because sometimes you need a reality check.

## Overview

CodeRoast is a humorous Python library that catches exceptions and provides snarky commentary on your programming skills. Great for adding a bit of levity to the debugging process or for teaching humility to overconfident programmers.

## Features

* Automatically adds insults to exceptions
* Provides a decorator for roasting specific functions
* Includes insults categorized by error type
* Can be enabled/disabled at runtime
* Supports custom insults and personalization
* Provides "roast levels" from mild to brutal

## Installation

```bash
pip install coderoast
```

## Usage

### Basic Usage

Simply import the library and activate the roasting:

```python
from coderoast import CodeRoast

# Activate the roasting globally
CodeRoast.activate()

# Now any unhandled exception will trigger an insult
def broken_function():
    return 1 / 0

try:
    broken_function()
except:
    pass  # The exception will be printed with an insult
```

### Function Decorator

You can use the decorator to roast specific functions:

```python
from coderoast import CodeRoast

# Only roast specific functions
@CodeRoast.roast_function
def another_broken_function():
    x = [1, 2, 3]
    return x[10]  # Index error

try:
    another_broken_function()
except:
    pass  # This function will be roasted
```

### Setting Roast Level

Choose the severity of insults from mild to brutal:

```python
from coderoast import CodeRoast, RoastLevel

# Set roast level
CodeRoast.set_roast_level(RoastLevel.MILD)  # More polite insults
# OR
CodeRoast.set_roast_level(RoastLevel.MEDIUM)  # Default level
# OR
CodeRoast.set_roast_level(RoastLevel.BRUTAL)  # No mercy
```

### Getting Insults Directly

```python
# Get a random insult
insult = CodeRoast.get_insult()
print(insult)

# Get an insult for a specific error type
insult = CodeRoast.get_insult_by_error(ValueError)
print(insult)
```

### Customizing Insults

You can add your own insults to the library:

```python
from coderoast import CodeRoast

# Add general insults
CodeRoast.add_insults([
    "This code is so bad it made my CPU cry.",
    "Have you considered a career in interpretive dance instead?",
])

# Add insults for specific error types
CodeRoast.add_categorized_insult('syntax', [
    "Your syntax is like abstract art - innovative but completely non-functional.",
    "I've seen more structure in a kindergarten finger painting than in your code.",
])
```

### Enable/Disable

You can enable or disable the roasting at runtime:

```python
# Disable roasting
CodeRoast.deactivate()

# Re-enable roasting
CodeRoast.activate()
```

## Sample Output

```
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    broken_function()
  File "example.py", line 7, in broken_function
    return 1 / 0
ZeroDivisionError: division by zero

🔥 ROASTED 🔥
👉 Your code has more bugs than a tropical rainforest.
👉 Maybe try again when you know what you're doing.
```

## Insult Categories

CodeRoast includes specialized insults for different error types:

* Syntax errors
* Logic errors
* Runtime errors
* Mathematical errors
* Type errors
* And more!

## Why Use CodeRoast?

* To add humor to your debugging process
* To humble yourself or your teammates
* For educational purposes (teaching new programmers to handle exceptions)
* Because normal error messages are too polite
* To build character and resilience in coding

## Pair with JediDebug

For a good cop/bad cop debugging experience, try pairing CodeRoast with its gentler counterpart, [JediDebug](https://github.com/notarealprogrammer001/jedidebug)!

## Contributing

Feel free to contribute additional insults or features by submitting a pull request. The more creative the insults, the better!

## License

MIT License