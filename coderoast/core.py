"""
Core functionality of the CodeRoast library.
"""

import sys
import random
from .insults import (
    GENERAL_INSULTS, 
    ERROR_INSULTS, 
    ERROR_TYPE_MAP, 
    RoastLevel
)
from .handlers import (
    get_insult_for_error,
    roast_exception_handler, 
    roast_function_decorator, 
    original_excepthook
)


class CodeRoast:
    """
    Main class for CodeRoast functionality.
    """
    # Store insults for easy access
    INSULTS = GENERAL_INSULTS[RoastLevel.MEDIUM].copy()
    CATEGORIZED_INSULTS = ERROR_INSULTS.copy()
    
    # Current roast level
    _roast_level = RoastLevel.MEDIUM
    
    # Flag to track activation status
    _active = False
    
    @classmethod
    def get_insult(cls):
        """
        Return a random insult from the collection.
        
        Returns:
            str: A random insult.
        """
        return random.choice(cls.INSULTS)
    
    @classmethod
    def get_insult_by_error(cls, error_type):
        """
        Return an insult appropriate for the given error type.
        
        Args:
            error_type (type or str): The error type or name.
            
        Returns:
            str: An insult tailored to the error type.
        """
        if isinstance(error_type, type):
            error_type = error_type.__name__
            
        main_insult, _ = get_insult_for_error(error_type, cls._roast_level)
        return main_insult
    
    @classmethod
    def get_insult_by_category(cls, category):
        """
        Return an insult from a specific category.
        
        Args:
            category (str): The category of insult to retrieve.
            
        Returns:
            str: A random insult from the specified category.
            
        Raises:
            ValueError: If the category does not exist.
        """
        if (category in cls.CATEGORIZED_INSULTS and 
            cls.CATEGORIZED_INSULTS[category].get(cls._roast_level)):
            return random.choice(cls.CATEGORIZED_INSULTS[category][cls._roast_level])
        else:
            available = ", ".join(sorted(cls.CATEGORIZED_INSULTS.keys()))
            raise ValueError(f"Unknown insult category: {category}. Available categories: {available}")
    
    @classmethod
    def add_insults(cls, insults):
        """
        Add custom insults to the general insults collection.
        
        Args:
            insults (list or str): An insult or list of insults to add.
            
        Returns:
            int: The number of insults added.
        """
        if not isinstance(insults, list):
            insults = [insults]
        
        cls.INSULTS.extend(insults)
        return len(insults)
    
    @classmethod
    def add_categorized_insult(cls, category, insults, level=RoastLevel.MEDIUM):
        """
        Add custom insults to a specific category.
        
        Args:
            category (str): The category to add insults to.
            insults (list or str): An insult or list of insults to add.
            level (RoastLevel, optional): The roast level for these insults. Defaults to MEDIUM.
            
        Returns:
            int: The number of insults added.
        """
        if not isinstance(insults, list):
            insults = [insults]
        
        if category not in cls.CATEGORIZED_INSULTS:
            cls.CATEGORIZED_INSULTS[category] = {}
            
        if level not in cls.CATEGORIZED_INSULTS[category]:
            cls.CATEGORIZED_INSULTS[category][level] = []
        
        cls.CATEGORIZED_INSULTS[category][level].extend(insults)
        return len(insults)
    
    @classmethod
    def set_roast_level(cls, level):
        """
        Set the severity level of insults.
        
        Args:
            level (RoastLevel): The severity level to use.
            
        Returns:
            RoastLevel: The new roast level.
        """
        if not isinstance(level, RoastLevel):
            raise TypeError(f"Level must be a RoastLevel enum, got {type(level)}")
            
        cls._roast_level = level
        
        # Update the general INSULTS list to match the new level
        cls.INSULTS = GENERAL_INSULTS[level].copy()
        
        return cls._roast_level
    
    @classmethod
    def get_roast_level(cls):
        """
        Get the current roast level.
        
        Returns:
            RoastLevel: The current roast level.
        """
        return cls._roast_level
    
    @classmethod
    def activate(cls):
        """
        Activate the CodeRoast exception handler.
        
        Returns:
            bool: True if activation was successful.
        """
        def current_handler(exc_type, exc_value, exc_traceback):
            roast_exception_handler(exc_type, exc_value, exc_traceback, cls._roast_level)
            
        sys.excepthook = current_handler
        cls._active = True
        print("CodeRoast activated! Prepare to be roasted for your mistakes.")
        return True
    
    @classmethod
    def deactivate(cls):
        """
        Deactivate the CodeRoast exception handler.
        
        Returns:
            bool: True if deactivation was successful.
        """
        sys.excepthook = original_excepthook
        cls._active = False
        print("CodeRoast deactivated. Your coding errors will now be treated with respect they don't deserve.")
        return True
    
    @classmethod
    def is_active(cls):
        """
        Check if CodeRoast is active.
        
        Returns:
            bool: True if CodeRoast is active, False otherwise.
        """
        return cls._active
    
    @classmethod
    def roast_function(cls, func=None, level=None):
        """
        Decorator to roast a specific function if it raises an exception.
        
        Can be used as @CodeRoast.roast_function or @CodeRoast.roast_function(level=RoastLevel.BRUTAL)
        
        Args:
            func: The function to decorate (or None if used with parameters)
            level (RoastLevel, optional): The severity level for this function's roasts.
            
        Returns:
            The decorated function or a decorator
        """
        if func is None:
            # Called with parameters: @roast_function(level=...)
            def decorator(function):
                return roast_function_decorator(function, level or cls._roast_level)
            return decorator
        else:
            # Called without parameters: @roast_function
            return roast_function_decorator(func, cls._roast_level)
    
    @classmethod
    def get_available_categories(cls):
        """
        Get a list of all available insult categories.
        
        Returns:
            list: A sorted list of available insult categories.
        """
        return sorted(cls.CATEGORIZED_INSULTS.keys())