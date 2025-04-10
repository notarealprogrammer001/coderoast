"""
Contains handlers for exceptions and decorators.
"""

import sys
import traceback
import functools
import random
from .insults import GENERAL_INSULTS, ERROR_INSULTS, ERROR_TYPE_MAP, RoastLevel


def get_insult_for_error(error_type=None, roast_level=RoastLevel.MEDIUM):
    """
    Get insults appropriate for the given error type and roast level.
    
    Args:
        error_type (str, optional): The error type name. Defaults to None.
        roast_level (RoastLevel, optional): The severity of insults. Defaults to MEDIUM.
        
    Returns:
        tuple: A tuple containing the main insult and a final zinger.
    """
    # Get main insult based on error type if possible
    if error_type and error_type in ERROR_TYPE_MAP:
        category = ERROR_TYPE_MAP[error_type]
        if category in ERROR_INSULTS and ERROR_INSULTS[category].get(roast_level):
            main_insult = random.choice(ERROR_INSULTS[category][roast_level])
        else:
            main_insult = random.choice(GENERAL_INSULTS[roast_level])
    else:
        main_insult = random.choice(GENERAL_INSULTS[roast_level])
    
    # Get a final zinger
    final_zinger = random.choice(ERROR_INSULTS['final_zinger'][roast_level])
    
    return main_insult, final_zinger


def roast_exception_handler(exc_type, exc_value, exc_traceback, roast_level=RoastLevel.MEDIUM):
    """
    Custom exception handler that adds insults.
    
    Args:
        exc_type: Exception type
        exc_value: Exception value
        exc_traceback: Exception traceback
        roast_level (RoastLevel, optional): The severity of insults. Defaults to MEDIUM.
    """
    # Print the original traceback
    print("".join(traceback.format_exception(exc_type, exc_value, exc_traceback)), file=sys.stderr)
    
    # Get insults based on the error type
    main_insult, final_zinger = get_insult_for_error(exc_type.__name__, roast_level)
    
    # Add the insults
    print("\n🔥 ROASTED 🔥", file=sys.stderr)
    print(f"👉 {main_insult}", file=sys.stderr)
    print(f"👉 {final_zinger}\n", file=sys.stderr)


def roast_function_decorator(func, roast_level=RoastLevel.MEDIUM):
    """
    Decorator to roast a specific function if it raises an exception.
    
    Args:
        func: The function to decorate
        roast_level (RoastLevel, optional): The severity of insults. Defaults to MEDIUM.
        
    Returns:
        The decorated function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_type = type(e).__name__
            main_insult, final_zinger = get_insult_for_error(error_type, roast_level)
            
            print(f"\n🔥 FUNCTION ROASTED 🔥", file=sys.stderr)
            print(f"👉 {main_insult}", file=sys.stderr)
            print(f"👉 Function '{func.__name__}' failed spectacularly.", file=sys.stderr)
            print(f"👉 {final_zinger}\n", file=sys.stderr)
            
            # Re-raise the exception for normal handling
            raise
    
    return wrapper


# Store the original excepthook
original_excepthook = sys.excepthook