"""
Tests for the CodeRoast package.
"""

import sys
import unittest
import io
from contextlib import redirect_stderr

from coderoast import CodeRoast, RoastLevel
from coderoast.insults import GENERAL_INSULTS, ERROR_INSULTS


class TestCodeRoast(unittest.TestCase):
    """Test cases for CodeRoast package."""

    def setUp(self):
        """Set up for tests."""
        # Make sure CodeRoast is activated with default settings
        CodeRoast.set_roast_level(RoastLevel.MEDIUM)
        CodeRoast.activate()

    def tearDown(self):
        """Clean up after tests."""
        # Reset to original state after each test
        CodeRoast.deactivate()

    def test_activate_deactivate(self):
        """Test activating and deactivating CodeRoast."""
        # Test activate
        original_excepthook = sys.excepthook
        
        CodeRoast.activate()
        self.assertNotEqual(sys.excepthook, original_excepthook)
        self.assertTrue(CodeRoast.is_active())
        
        # Test deactivate
        CodeRoast.deactivate()
        self.assertEqual(sys.excepthook, original_excepthook)
        self.assertFalse(CodeRoast.is_active())

    def test_get_insult(self):
        """Test getting a random insult."""
        insult = CodeRoast.get_insult()
        self.assertIsInstance(insult, str)
        self.assertGreater(len(insult), 10)  # Insult should be non-empty
        self.assertTrue(insult in CodeRoast.INSULTS)

    def test_get_insult_by_category(self):
        """Test getting an insult by category."""
        # Test with a valid category
        if 'syntax' in CodeRoast.CATEGORIZED_INSULTS:
            insult = CodeRoast.get_insult_by_category('syntax')
            self.assertIsInstance(insult, str)
            self.assertGreater(len(insult), 10)
            self.assertTrue(insult in CodeRoast.CATEGORIZED_INSULTS['syntax'][RoastLevel.MEDIUM])
        
        # Test with an invalid category
        with self.assertRaises(ValueError):
            CodeRoast.get_insult_by_category('not_a_real_category')

    def test_get_insult_by_error(self):
        """Test getting an insult for a specific error type."""
        # Test with an error class
        insult = CodeRoast.get_insult_by_error(ValueError)
        self.assertIsInstance(insult, str)
        self.assertGreater(len(insult), 10)
        
        # Test with an error name as string
        insult = CodeRoast.get_insult_by_error('ZeroDivisionError')
        self.assertIsInstance(insult, str)
        self.assertGreater(len(insult), 10)

    def test_add_insults(self):
        """Test adding custom insults."""
        # Initial count
        initial_count = len(CodeRoast.INSULTS)
        
        # Add a single insult
        new_insult = "This is a test insult that would never be in the default list."
        num_added = CodeRoast.add_insults(new_insult)
        self.assertEqual(num_added, 1)
        self.assertEqual(len(CodeRoast.INSULTS), initial_count + 1)
        self.assertIn(new_insult, CodeRoast.INSULTS)
        
        # Add multiple insults
        new_insults = ["Test insult 1", "Test insult 2", "Test insult 3"]
        num_added = CodeRoast.add_insults(new_insults)
        self.assertEqual(num_added, 3)
        self.assertEqual(len(CodeRoast.INSULTS), initial_count + 4)
        for insult in new_insults:
            self.assertIn(insult, CodeRoast.INSULTS)

    def test_add_categorized_insult(self):
        """Test adding categorized insults."""
        # Test adding to existing category
        category = 'syntax'
        if category in CodeRoast.CATEGORIZED_INSULTS:
            initial_count = len(CodeRoast.CATEGORIZED_INSULTS[category][RoastLevel.MEDIUM])
            new_insult = "This is a new test insult for syntax errors."
            num_added = CodeRoast.add_categorized_insult(category, new_insult)
            self.assertEqual(num_added, 1)
            self.assertEqual(len(CodeRoast.CATEGORIZED_INSULTS[category][RoastLevel.MEDIUM]), initial_count + 1)
            self.assertIn(new_insult, CodeRoast.CATEGORIZED_INSULTS[category][RoastLevel.MEDIUM])
        
        # Test adding to new category
        new_category = 'test_category'
        if new_category not in CodeRoast.CATEGORIZED_INSULTS:
            new_insults = ["Test category insult 1", "Test category insult 2"]
            num_added = CodeRoast.add_categorized_insult(new_category, new_insults)
            self.assertEqual(num_added, 2)
            self.assertIn(new_category, CodeRoast.CATEGORIZED_INSULTS)
            self.assertEqual(len(CodeRoast.CATEGORIZED_INSULTS[new_category][RoastLevel.MEDIUM]), 2)
            for insult in new_insults:
                self.assertIn(insult, CodeRoast.CATEGORIZED_INSULTS[new_category][RoastLevel.MEDIUM])
        
        # Test adding with specific roast level
        new_category = 'another_test_category'
        if new_category not in CodeRoast.CATEGORIZED_INSULTS:
            new_insult = "A brutal test insult"
            num_added = CodeRoast.add_categorized_insult(new_category, new_insult, RoastLevel.BRUTAL)
            self.assertEqual(num_added, 1)
            self.assertIn(new_category, CodeRoast.CATEGORIZED_INSULTS)
            self.assertEqual(len(CodeRoast.CATEGORIZED_INSULTS[new_category][RoastLevel.BRUTAL]), 1)
            self.assertIn(new_insult, CodeRoast.CATEGORIZED_INSULTS[new_category][RoastLevel.BRUTAL])

    def test_set_get_roast_level(self):
        """Test setting and getting the roast level."""
        # Test getting the default level
        current_level = CodeRoast.get_roast_level()
        self.assertEqual(current_level, RoastLevel.MEDIUM)
        
        # Test setting to MILD
        CodeRoast.set_roast_level(RoastLevel.MILD)
        self.assertEqual(CodeRoast.get_roast_level(), RoastLevel.MILD)
        self.assertTrue(all(insult in GENERAL_INSULTS[RoastLevel.MILD] for insult in CodeRoast.INSULTS))
        
        # Test setting to BRUTAL
        CodeRoast.set_roast_level(RoastLevel.BRUTAL)
        self.assertEqual(CodeRoast.get_roast_level(), RoastLevel.BRUTAL)
        self.assertTrue(all(insult in GENERAL_INSULTS[RoastLevel.BRUTAL] for insult in CodeRoast.INSULTS))
        
        # Test with invalid type
        with self.assertRaises(TypeError):
            CodeRoast.set_roast_level("BRUTAL")

    def test_is_active(self):
        """Test the is_active function."""
        CodeRoast.activate()
        self.assertTrue(CodeRoast.is_active())
        
        CodeRoast.deactivate()
        self.assertFalse(CodeRoast.is_active())

    def test_roast_function_decorator(self):
        """Test the roast_function decorator."""
        # Test basic decorator
        @CodeRoast.roast_function
        def function_that_raises():
            """Function that will raise an error."""
            raise ValueError("Test error")

        # Capture stderr to check for roast
        err = io.StringIO()
        with redirect_stderr(err):
            try:
                function_that_raises()
            except ValueError:
                pass

        output = err.getvalue()
        self.assertIn("FUNCTION ROASTED", output)
        self.assertIn("👉", output)
        self.assertIn("function_that_raises", output)
        
        # Test decorator with custom level
        @CodeRoast.roast_function(level=RoastLevel.BRUTAL)
        def function_with_brutal_roast():
            """Function that will raise an error and get brutally roasted."""
            raise ValueError("Another test error")
            
        # Capture stderr to check for brutal roast
        err = io.StringIO()
        with redirect_stderr(err):
            try:
                function_with_brutal_roast()
            except ValueError:
                pass
                
        output = err.getvalue()
        self.assertIn("FUNCTION ROASTED", output)
        # Note: We can't check for specific brutal insults as they're randomly selected

    def test_exception_handler(self):
        """Test the exception handler with various errors."""
        # Activate CodeRoast
        CodeRoast.activate()
        
        # Test with ValueError
        err = io.StringIO()
        with redirect_stderr(err):
            try:
                int("not a number")
            except ValueError:
                pass

        output = err.getvalue()
        self.assertIn("ROASTED", output)
        self.assertIn("👉", output)
        self.assertIn("ValueError", output)
        
        # Clear buffer
        err = io.StringIO()
        
        # Test with TypeError
        with redirect_stderr(err):
            try:
                len(5)
            except TypeError:
                pass

        output = err.getvalue()
        self.assertIn("ROASTED", output)
        self.assertIn("👉", output)
        self.assertIn("TypeError", output)

    def test_get_available_categories(self):
        """Test getting available categories."""
        categories = CodeRoast.get_available_categories()
        self.assertIsInstance(categories, list)
        self.assertGreater(len(categories), 0)
        self.assertEqual(sorted(categories), categories)  # Check that list is sorted
        
        # Check all categories are valid
        for category in categories:
            self.assertIn(category, CodeRoast.CATEGORIZED_INSULTS)


if __name__ == "__main__":
    unittest.main()