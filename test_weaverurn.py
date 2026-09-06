# test_weaverurn.py
"""
Tests for WeaverUrn module.
"""

import unittest
from weaverurn import WeaverUrn

class TestWeaverUrn(unittest.TestCase):
    """Test cases for WeaverUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WeaverUrn()
        self.assertIsInstance(instance, WeaverUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WeaverUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
