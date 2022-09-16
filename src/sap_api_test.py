from argparse import ArgumentError
import unittest
from sapguiapi import GuiComponent


class MockGuiComponent():
    """_summary_
    """

    def __init__(self: object, container_type: bool = True,
                 id: str = 'id',
                 name: str = 'name',
                 parent: object = {},
                 type: str = 'GuiComponent',
                 type_as_number: int = 0):
        """_summary_

        Args:
            self (object): _description_
            container_type (bool, optional): _description_. Defaults to True.
            id (str, optional): _description_. Defaults to 'id'.
            name (str, optional): _description_. Defaults to 'name'.
            parent (object, optional): _description_. Defaults to {}.
            type (str, optional): _description_. Defaults to 'GuiComponent'.
            type_as_number (int, optional): _description_. Defaults to 0.
        """
        self.ContainerType = container_type
        self.Id = id
        self.Name = name
        self.Parent = parent
        self.Type = type
        self.TypeAsNumber = type_as_number


class TestGuiComponent(unittest.TestCase):

    def test_is_valid(self: object):
        """Check if the validation is correct.

        Assigns the internal variable an object of the wrong type,
        to check if the validation is correct.
        """
        obj = GuiComponent()
        obj._element = {}
        self.assertFalse(obj.is_valid)
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertTrue(obj.is_valid)
        obj_mock.Type = 'Component'
        self.assertFalse(obj.is_valid)

    def test_element(self: object):
        obj = GuiComponent()
        self.assertIsNone(obj._element)
        with self.assertRaises(AttributeError):
            obj = GuiComponent({})
        with self.assertRaises(AttributeError):
            obj = GuiComponent()
            obj.element = {}
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertEqual(obj.type, 'GuiComponent')
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            obj_mock = MockGuiComponent()
            obj_mock.Type = 'Component'
            errorTest = obj.element

    def test_container_type(self: object):
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertTrue(obj.container_type)
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.container_type

    def test_id(self: object):
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertEqual(obj.id, 'id')
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.id

    def test_name(self: object):
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertEqual(obj.name, 'name')
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.name

    def test_parent(self: object):
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertEqual(obj.parent, {})
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.parent

    def test_type(self: object):
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertEqual(obj.type, 'GuiComponent')
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.type

    def test_type_as_number(self: object):
        obj = GuiComponent()
        obj_mock = MockGuiComponent()
        obj._element = obj_mock
        self.assertEqual(obj.type_as_number, 0)
        with self.assertRaises(TypeError):
            obj = GuiComponent()
            errorTest = obj.type_as_number


if __name__ == '__main__':
    unittest.main()
