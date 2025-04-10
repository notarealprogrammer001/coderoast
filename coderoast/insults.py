"""
Contains the database of insults for CodeRoast.
"""

from enum import Enum


class RoastLevel(Enum):
    """Enum representing the severity of insults."""
    MILD = 1     # Lighthearted teasing
    MEDIUM = 2   # Standard roasting
    BRUTAL = 3   # No mercy


# General insults
GENERAL_INSULTS = {
    # Mild insults
    RoastLevel.MILD: [
        "Your code seems like it was written in a hurry. Maybe take a deep breath next time?",
        "This code could use a bit more attention to detail.",
        "I think your algorithm might need a second look.",
        "There's room for improvement in your error handling strategy.",
        "Have you considered more testing before deploying?",
        "Your logic is creative, but perhaps not optimal.",
        "This code is working hard, but not smart.",
        "You're on the right track, but not quite there yet.",
        "Close, but no cigar. Maybe try a different approach?",
        "This solution is... interesting. But maybe not for the reasons you'd hope.",
    ],
    
    # Medium insults (default level)
    RoastLevel.MEDIUM: [
        "Seriously? That's the code you wrote? My calculator has better logic.",
        "Your code is like a mystery novel, except the only mystery is how it ever worked.",
        "I've seen better code written by a cat walking on a keyboard.",
        "If your code was any more broken, it would qualify for workers' compensation.",
        "Your algorithm is so inefficient, it makes government bureaucracy look fast.",
        "Your code has more bugs than a tropical rainforest.",
        "This code is why Stack Overflow exists.",
        "Your variable naming convention appears to be 'keyboard smash'.",
        "This function is more convoluted than the plot of a telenovela.",
        "Your code runs like a sloth swimming through peanut butter.",
    ],
    
    # Brutal insults
    RoastLevel.BRUTAL: [
        "Ah, I see the problem. You're trying to program while being stupid.",
        "Did you get your programming license from a cereal box?",
        "ERROR: Intelligence module failed to load. User incompetence detected.",
        "Maybe programming isn't for everyone. Have you considered gardening?",
        "I'm not saying your code is bad, but it made Skynet reconsider its attack on humanity.",
        "ERROR: Brain not found. Have you tried turning it on and off again?",
        "You're the reason we have coding standards.",
        "Your code is like a train wreck, except trains have a purpose.",
        "If programming skills were currency, you'd be asking for spare change.",
        "I've seen more logic in a conspiracy theorist's YouTube comments.",
    ],
}


# Insults for specific error types
ERROR_INSULTS = {
    # Syntax errors
    'syntax': {
        RoastLevel.MILD: [
            "Your syntax could use a little polish.",
            "Maybe double-check your syntax next time?",
            "The syntax fairy is not impressed with your offering.",
            "Those brackets seem to be in a complicated relationship status.",
            "Your indentation strategy is... creative.",
        ],
        RoastLevel.MEDIUM: [
            "Your syntax is why code highlighters were invented.",
            "The compiler took one look at your syntax and gave up.",
            "I've seen toddlers with better grammar than your code.",
            "Your syntax is like abstract art - interesting but completely non-functional.",
            "Did you just mash the keyboard and hope for the best?",
        ],
        RoastLevel.BRUTAL: [
            "Your syntax is so bad it should be classified as a war crime.",
            "If syntax were a person, yours would be filing a restraining order against you.",
            "The language designers didn't anticipate someone using syntax this incorrectly.",
            "Your syntax makes COBOL look elegant.",
            "Congratulations, you've invented a new language. Unfortunately, it's incompatible with computers.",
        ],
    },
    
    # Logic errors
    'logic': {
        RoastLevel.MILD: [
            "Your logic could use a second opinion.",
            "This algorithm took a wrong turn somewhere.",
            "The logical flow of this code is... unconventional.",
            "I think your conditional statement might be confused.",
            "Your logic is enthusiastic but misguided.",
        ],
        RoastLevel.MEDIUM: [
            "Your logic is more circular than a roundabout.",
            "This code's logic is more twisted than a pretzel.",
            "If this logic were a map, you'd end up in the ocean.",
            "Your conditional statements are having an existential crisis.",
            "This algorithm has more holes than Swiss cheese.",
        ],
        RoastLevel.BRUTAL: [
            "Your logic makes flat-earthers seem reasonable.",
            "This function's logic is so flawed it's practically gaslighting the compiler.",
            "I've seen more coherent logic from a random number generator.",
            "Your code's logic is breaking the laws of computer science.",
            "This algorithm is so bad it's making mathematicians cry.",
        ],
    },
    
    # Type errors
    'type': {
        RoastLevel.MILD: [
            "Types exist for a reason, you know.",
            "It seems you're being creative with your data types.",
            "Type checking isn't just a suggestion.",
            "Perhaps consider what type of data you're working with?",
            "Your type handling could use a refresher.",
        ],
        RoastLevel.MEDIUM: [
            "You're treating types like suggestions rather than rules.",
            "Your code is playing type roulette, and it just lost.",
            "Types and your code are like oil and water - they don't mix.",
            "Did you just try to add a string to a datetime? Bold move.",
            "This code thinks Python is JavaScript. It's not.",
        ],
        RoastLevel.BRUTAL: [
            "Your understanding of types is as non-existent as your debugging skills.",
            "If types were traffic laws, you'd have lost your license years ago.",
            "You've transformed type errors into an art form. A very ugly art form.",
            "Your code's type system is like the Wild West, but with fewer rules.",
            "The ghost of strong typing has come back to haunt you.",
        ],
    },
    
    # Math errors
    'math': {
        RoastLevel.MILD: [
            "Your math might need a double-check.",
            "This calculation seems a bit off.",
            "The numbers don't quite add up here.",
            "Your algorithm's math is a little wobbly.",
            "Maybe try using a calculator first?",
        ],
        RoastLevel.MEDIUM: [
            "Your math skills make common core look sensible.",
            "This calculation is more wishful thinking than mathematics.",
            "Division by zero? Really? That's like rule #1 of what not to do.",
            "Your code's math would make a statistician weep.",
            "This algorithm's calculations are more fantasy than reality.",
        ],
        RoastLevel.BRUTAL: [
            "Your mathematical abilities would disappoint Pythagoras.",
            "This function does to math what a blender does to fruit.",
            "Your understanding of numbers is theoretical at best.",
            "This code's math would fail a 3rd-grade arithmetic test.",
            "If your math skills were currency, you'd be bankrupt.",
        ],
    },
    
    # Runtime errors
    'runtime': {
        RoastLevel.MILD: [
            "Something went wrong at runtime. Surprising, I know.",
            "Your code was doing fine until it actually had to run.",
            "Runtime is when theory meets reality, and your theory lost.",
            "This code is having an existential crisis at runtime.",
            "The runtime environment doesn't seem to appreciate your style.",
        ],
        RoastLevel.MEDIUM: [
            "Your code runs like a car with square wheels.",
            "This program crashes more often than a test dummy.",
            "Runtime? More like ruin-time for your code.",
            "Your program's runtime behavior is more unpredictable than the weather.",
            "This code runs about as well as a three-legged elephant.",
        ],
        RoastLevel.BRUTAL: [
            "Your code's runtime behavior is the digital equivalent of spontaneous combustion.",
            "This program crashes so reliably you could set your watch by it.",
            "The only thing running here is my patience - running out.",
            "Your code runs like it's allergic to processors.",
            "This program has the runtime stability of a house of cards in a hurricane.",
        ],
    },
    
    # I/O errors
    'io': {
        RoastLevel.MILD: [
            "Your file handling could use some work.",
            "Did you check if that file actually exists?",
            "The file system doesn't seem to be cooperating with your code.",
            "I/O operations need a bit more care than this.",
            "It seems your code and the file system have a communication problem.",
        ],
        RoastLevel.MEDIUM: [
            "Your file I/O code is playing hide and seek with the actual files.",
            "This code treats file paths like a treasure hunt with no map.",
            "File not found? Maybe look where you actually saved it.",
            "Your program's relationship with the file system is 'it's complicated'.",
            "This I/O code is more hopeful than realistic.",
        ],
        RoastLevel.BRUTAL: [
            "Your file handling makes a toddler with crayons look organized.",
            "The file system took one look at your code and filed a restraining order.",
            "Your I/O operations are so bad they've been reported for disk abuse.",
            "This code searches for files like a drunk person looking for their keys.",
            "Your program and the file system are like divorced parents who aren't speaking.",
        ],
    },
    
    # Final zingers for all error types
    'final_zinger': {
        RoastLevel.MILD: [
            "Maybe take a coffee break and try again?",
            "Don't worry, we all have off days.",
            "Keep at it, you'll get there eventually.",
            "A fresh pair of eyes might help with this one.",
            "Good effort, but not quite there yet.",
        ],
        RoastLevel.MEDIUM: [
            "Maybe try again when you know what you're doing.",
            "Have you considered a career change?",
            "This code is a compelling argument for AI replacing programmers.",
            "Let me know when you're ready to write actual working code.",
            "I'd tell you to fix it, but I'm not sure you can.",
        ],
        RoastLevel.BRUTAL: [
            "Please return your keyboard and go back to using a pencil and paper.",
            "The best fix for this code would be to delete it entirely.",
            "Your code has been selected as a cautionary tale for CS students.",
            "Your IDE should have a panic button for code like this.",
            "The only solution here is to reformat your drive and start fresh.",
        ],
    },
}


# Map error types to insult categories
ERROR_TYPE_MAP = {
    'SyntaxError': 'syntax',
    'IndentationError': 'syntax',
    'TabError': 'syntax',
    
    'ValueError': 'logic',
    'AttributeError': 'logic',
    'AssertionError': 'logic',
    'KeyError': 'logic',
    'IndexError': 'logic',
    
    'TypeError': 'type',
    
    'ZeroDivisionError': 'math',
    'OverflowError': 'math',
    'FloatingPointError': 'math',
    
    'RuntimeError': 'runtime',
    'RecursionError': 'runtime',
    'TimeoutError': 'runtime',
    'StopIteration': 'runtime',
    
    'FileNotFoundError': 'io',
    'PermissionError': 'io',
    'FileExistsError': 'io',
    'IsADirectoryError': 'io',
    'IOError': 'io',
}