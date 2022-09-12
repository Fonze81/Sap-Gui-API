from argparse import ArgumentError
import unittest
from sapguiapi import GuiComponent

class TestGuiComponent(unittest.TestCase):

    def test_constructor(self: object):
        obj = GuiComponent()
        self.assertEqual(obj._element, None)

    def test_constructor_with_arguments(self: object):
        pass # TODO

    def test_is_valid(self: object):
        """Check if the validation is correct.

        Assigns the internal variable an object of the wrong type,
        to check if the validation is correct.
        """
        obj = GuiComponent()
        obj._element = {}
        self.assertFalse(obj.is_valid)

    def test_validate_element_type(self: object):
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.type


if __name__ == '__main__':
    unittest.main()
