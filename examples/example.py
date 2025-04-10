"""
Example usage of the CodeRoast library.
"""

from coderoast import CodeRoast, RoastLevel


def demonstrate_basic_usage():
    """Demonstrate basic usage of CodeRoast."""
    print("=== Basic Usage ===")
    
    # Activate CodeRoast
    CodeRoast.activate()
    
    # Try a simple error
    print("\nGenerating a simple error:")
    try:
        1 / 0  # ZeroDivisionError
    except:
        print("Error caught and handled with a roast")


def demonstrate_insults_api():
    """Demonstrate the insults API."""
    print("\n=== Insults API ===")
    
    # Get a random insult
    print("\nRandom insult:")
    print(CodeRoast.get_insult())
    
    # Get insults by category
    print("\nSyntax error insult:")
    try:
        print(CodeRoast.get_insult_by_category('syntax'))
    except ValueError as e:
        print(f"Error: {e}")
    
    # Get insult by error type
    print("\nInsult for ZeroDivisionError:")
    print(CodeRoast.get_insult_by_error(ZeroDivisionError))
    
    # List available categories
    print("\nAvailable insult categories:")
    categories = CodeRoast.get_available_categories()
    print(", ".join(categories))


def demonstrate_decorator():
    """Demonstrate the roast function decorator."""
    print("\n=== Function Decorator ===")
    
    @CodeRoast.roast_function
    def force_error():
        """Function that will raise an error."""
        x = [1, 2, 3]
        return x[10]  # IndexError
    
    print("\nCalling function with decorator:")
    try:
        force_error()
    except:
        print("Error caught from decorated function")
    
    # Demonstrate decorator with custom roast level
    @CodeRoast.roast_function(level=RoastLevel.BRUTAL)
    def force_another_error():
        """Function that will raise a different error with brutal roasting."""
        return int("not a number")  # ValueError
    
    print("\nCalling function with brutal roast level:")
    try:
        force_another_error()
    except:
        print("Error caught from decorated function with brutal roast")


def demonstrate_custom_insults():
    """Demonstrate adding custom insults."""
    print("\n=== Custom Insults ===")
    
    # Add custom general insults
    custom_insults = [
        "This code is so bad it made my CPU cry.",
        "Have you considered a career in interpretive dance instead?"
    ]
    num_added = CodeRoast.add_insults(custom_insults)
    print(f"\nAdded {num_added} custom insults")
    
    # Add custom categorized insults
    custom_category_insults = [
        "Your code's logic is more questionable than a politician's promises.",
        "This logic wouldn't pass a kindergarten 'if-then' test."
    ]
    num_added = CodeRoast.add_categorized_insult('logic', custom_category_insults)
    print(f"Added {num_added} custom insults to 'logic' category")
    
    # Show an example of a custom insult
    print("\nRandom insult (might be custom):")
    print(CodeRoast.get_insult())


def demonstrate_roast_levels():
    """Demonstrate different roast levels."""
    print("\n=== Roast Levels ===")
    
    # Show mild insults
    CodeRoast.set_roast_level(RoastLevel.MILD)
    print(f"\nCurrent roast level: {CodeRoast.get_roast_level().name}")
    print("\nMild insult example:")
    print(CodeRoast.get_insult())
    
    # Show medium insults (default)
    CodeRoast.set_roast_level(RoastLevel.MEDIUM)
    print(f"\nCurrent roast level: {CodeRoast.get_roast_level().name}")
    print("\nMedium insult example:")
    print(CodeRoast.get_insult())
    
    # Show brutal insults
    CodeRoast.set_roast_level(RoastLevel.BRUTAL)
    print(f"\nCurrent roast level: {CodeRoast.get_roast_level().name}")
    print("\nBrutal insult example:")
    print(CodeRoast.get_insult())
    
    # Generate an error with brutal roasting
    print("\nGenerating error with brutal roasting:")
    try:
        1 / 0  # ZeroDivisionError with brutal roasting
    except:
        print("Error caught with brutal roast")
    
    # Reset to default medium level
    CodeRoast.set_roast_level(RoastLevel.MEDIUM)
    print(f"\nReset to roast level: {CodeRoast.get_roast_level().name}")


def demonstrate_deactivation():
    """Demonstrate deactivating CodeRoast."""
    print("\n=== Deactivation ===")
    
    # Check if active
    print(f"\nCodeRoast active: {CodeRoast.is_active()}")
    
    # Deactivate CodeRoast
    CodeRoast.deactivate()
    print(f"CodeRoast active after deactivation: {CodeRoast.is_active()}")
    
    # Generate an error without roasting
    print("\nGenerating error after deactivation:")
    try:
        int("not a number")  # ValueError
    except:
        print("Error caught without roasting")
    
    # Reactivate for any future demos
    CodeRoast.activate()
    print(f"CodeRoast active after reactivation: {CodeRoast.is_active()}")


def demonstrate_different_errors():
    """Demonstrate different error types with appropriate insults."""
    print("\n=== Different Error Types ===")
    
    # SyntaxError demonstration
    print("\nSyntaxError demonstration:")
    try:
        exec("if True print('Hello')")  # SyntaxError
    except:
        print("SyntaxError caught with relevant roast")
    
    # TypeError demonstration
    print("\nTypeError demonstration:")
    try:
        len(5)  # TypeError
    except:
        print("TypeError caught with relevant roast")
    
    # FileNotFoundError demonstration
    print("\nFileNotFoundError demonstration:")
    try:
        with open("nonexistent_file.txt", "r") as f:  # FileNotFoundError
            f.read()
    except:
        print("FileNotFoundError caught with relevant roast")


if __name__ == "__main__":
    print("CodeRoast Example Program\n")
    
    # Run all demonstrations
    demonstrate_basic_usage()
    demonstrate_insults_api()
    demonstrate_decorator()
    demonstrate_custom_insults()
    demonstrate_roast_levels()
    demonstrate_deactivation()
    demonstrate_different_errors()
    
    print("\nAll examples completed. Better luck with your real code!")