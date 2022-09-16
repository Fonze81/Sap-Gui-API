import unittest
from sap_api import GuiComponent, GuiVComponent


class MockGuiComponent:
    def __init__(self,
                 type='str type',
                 container_type=True,
                 id='str id',
                 name='str name',
                 parent={},
                 type_as_number=0) -> None:
        self.ContainerType: bool = container_type
        self.Id: str = id
        self.Name: str = name
        self.Parent: object = parent
        self.Type: str = type
        self.TypeAsNumber: int = type_as_number


class MockGuiComponentNoType:
    def __init__(self) -> None:
        pass


class TestGuiComponent(unittest.TestCase):

    def test__init__no_arguments(self) -> None:
        """Create object with no arguments.
        The 'element' attribute must be 'None'."""
        obj: GuiComponent = GuiComponent()
        self.assertIsNone(obj.element)

    def test__init__without_type(self) -> None:
        """Create object with argument.
        The object does not have the 'Type' attribute."""
        with self.assertRaises(TypeError):
            obj_mock: MockGuiComponentNoType = MockGuiComponentNoType()
            obj: GuiComponent = GuiComponent(obj_mock)

    def test__init__incompatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute but its value is incompatible."""
        with self.assertRaises(TypeError):
            obj_mock: MockGuiComponent = MockGuiComponent("beer")
            obj: GuiComponent = GuiComponent(obj_mock)

    def test__init__ignore_incompatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute but its value is incompatible.
        Does not perform type checking."""
        obj_mock: MockGuiComponent = MockGuiComponent("beer")
        obj: GuiComponent = GuiComponent(obj_mock, validate_type=False)
        self.assertEqual(obj.element, obj_mock)

    def test__init__compatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent(type="GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.element, obj_mock)

    def test_set_element(self) -> None:
        """Set the element attribute to None."""
        obj: GuiComponent = GuiComponent()
        obj.element = None
        self.assertIsNone(obj.element)

    def test_set_element_without_type(self) -> None:
        """Set an object with no 'Type' attribute for the element."""
        with self.assertRaises(TypeError):
            obj: GuiComponent = GuiComponent()
            obj_mock: MockGuiComponentNoType = MockGuiComponentNoType()
            obj.element = obj_mock

    def test_set_element_incompatible_value(self) -> None:
        """Set an object has the 'Type' attribute but its value is incompatible."""
        with self.assertRaises(TypeError):
            obj: GuiComponent = GuiComponent()
            obj_mock: MockGuiComponent = MockGuiComponent("beer")
            obj.element = obj_mock

    def test_set_element_ignore_incompatible_value(self) -> None:
        """Set an object has the 'Type' attribute but its value is incompatible.
        Does not perform type checking."""
        obj_mock: MockGuiComponent = MockGuiComponent("beer")
        obj: GuiComponent = GuiComponent(validate_type=False)
        obj.element = obj_mock
        self.assertEqual(obj.element, obj_mock)

    def test_set_element_compatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.element, obj_mock)

    def test_get_container_type(self) -> None:
        """The object has the 'ContainerType' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertTrue(obj.container_type)

    def test_get_container_type_with_element_none(self) -> None:
        """The element is none."""
        with self.assertRaises(TypeError):
            obj: GuiComponent = GuiComponent()
            objA: bool = obj.container_type

    def test_get_container_type_with_element_without_type(self) -> None:
        """Set an object with no 'Type' attribute for the element."""
        obj_mock: MockGuiComponentNoType = MockGuiComponentNoType()
        obj: GuiComponent = GuiComponent()
        try:
            obj.element = obj_mock
        except:
            with self.assertRaises(TypeError):
                objA: bool = obj.container_type

    def test_get_id(self) -> None:
        """The object has the 'Id' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.id, 'str id')

    def test_get_name(self) -> None:
        """The object has the 'Name' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.name, 'str name')

    def test_get_parent(self) -> None:
        """The object has the 'Parent' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.parent, {})

    def test_get_type(self) -> None:
        """The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.type, "GuiComponent")

    def test_get_type_as_number(self) -> None:
        """The object has the 'TypeAsNumber' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.type_as_number, 0)

class MockGuiVComponent:
    def __init__(self,
                 type='str type',
                 container_type=True,
                 id='str id',
                 name='str name',
                 parent={},
                 type_as_number=1,
                 text='str text',
                 tooltip='str tooltip',
                 height=1000,
                 left=1001,
                 screen_left=1002,
                 screen_top=1003,
                 top=1004,
                 width=1005) -> None:
        self.ContainerType: bool = container_type
        self.Id: str = id
        self.Name: str = name
        self.Parent: object = parent
        self.Type: str = type
        self.TypeAsNumber: int = type_as_number
        self.Text: str = text
        self.Tooltip: str = tooltip
        self.Height: int = height
        self.Left: int = left
        self.ScreenLeft: int = screen_left
        self.ScreenTop: int = screen_top
        self.Top: int = top
        self.Width: int = width

class MockGuiVComponentNoType(MockGuiComponentNoType):
    pass

class TestGuiComponent(unittest.TestCase):

    def test__init__no_arguments(self) -> None:
        """Create object with no arguments.
        The 'element' attribute must be 'None'."""
        obj: GuiComponent = GuiComponent()
        self.assertIsNone(obj.element)

    def test__init__without_type(self) -> None:
        """Create object with argument.
        The object does not have the 'Type' attribute."""
        with self.assertRaises(TypeError):
            obj_mock: MockGuiComponentNoType = MockGuiComponentNoType()
            obj: GuiComponent = GuiComponent(obj_mock)

    def test__init__incompatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute but its value is incompatible."""
        with self.assertRaises(TypeError):
            obj_mock: MockGuiComponent = MockGuiComponent("beer")
            obj: GuiComponent = GuiComponent(obj_mock)

    def test__init__ignore_incompatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute but its value is incompatible.
        Does not perform type checking."""
        obj_mock: MockGuiComponent = MockGuiComponent("beer")
        obj: GuiComponent = GuiComponent(obj_mock, validate_type=False)
        self.assertEqual(obj.element, obj_mock)

    def test__init__compatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent(type="GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.element, obj_mock)

    def test_set_element(self) -> None:
        """Set the element attribute to None."""
        obj: GuiComponent = GuiComponent()
        obj.element = None
        self.assertIsNone(obj.element)

    def test_set_element_without_type(self) -> None:
        """Set an object with no 'Type' attribute for the element."""
        with self.assertRaises(TypeError):
            obj: GuiComponent = GuiComponent()
            obj_mock: MockGuiComponentNoType = MockGuiComponentNoType()
            obj.element = obj_mock

    def test_set_element_incompatible_value(self) -> None:
        """Set an object has the 'Type' attribute but its value is incompatible."""
        with self.assertRaises(TypeError):
            obj: GuiComponent = GuiComponent()
            obj_mock: MockGuiComponent = MockGuiComponent("beer")
            obj.element = obj_mock

    def test_set_element_ignore_incompatible_value(self) -> None:
        """Set an object has the 'Type' attribute but its value is incompatible.
        Does not perform type checking."""
        obj_mock: MockGuiComponent = MockGuiComponent("beer")
        obj: GuiComponent = GuiComponent(validate_type=False)
        obj.element = obj_mock
        self.assertEqual(obj.element, obj_mock)

    def test_set_element_compatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.element, obj_mock)

    def test_get_container_type(self) -> None:
        """The object has the 'ContainerType' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertTrue(obj.container_type)

    def test_get_container_type_with_element_none(self) -> None:
        """The element is none."""
        with self.assertRaises(TypeError):
            obj: GuiComponent = GuiComponent()
            objA: bool = obj.container_type

    def test_get_container_type_with_element_without_type(self) -> None:
        """Set an object with no 'Type' attribute for the element."""
        obj_mock: MockGuiComponentNoType = MockGuiComponentNoType()
        obj: GuiComponent = GuiComponent()
        try:
            obj.element = obj_mock
        except:
            with self.assertRaises(TypeError):
                objA: bool = obj.container_type

    def test_get_id(self) -> None:
        """The object has the 'Id' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.id, 'str id')

    def test_get_name(self) -> None:
        """The object has the 'Name' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.name, 'str name')

    def test_get_parent(self) -> None:
        """The object has the 'Parent' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.parent, {})

    def test_get_type(self) -> None:
        """The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.type, "GuiComponent")

    def test_get_type_as_number(self) -> None:
        """The object has the 'TypeAsNumber' attribute and its value is compatible."""
        obj_mock: MockGuiComponent = MockGuiComponent("GuiComponent")
        obj: GuiComponent = GuiComponent(obj_mock)
        self.assertEqual(obj.type_as_number, 0)


class TestGuiVComponent(unittest.TestCase):

    def test__init__no_arguments(self) -> None:
        """Create object with no arguments.
        The 'element' attribute must be 'None'."""
        obj: GuiVComponent = GuiVComponent()
        self.assertIsNone(obj.element)

    def test__init__without_type(self) -> None:
        """Create object with argument.
        The object does not have the 'Type' attribute."""
        with self.assertRaises(TypeError):
            obj_mock: MockGuiVComponentNoType = MockGuiVComponentNoType()
            obj: GuiVComponent = GuiVComponent(obj_mock)

    def test__init__incompatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute but its value is incompatible."""
        with self.assertRaises(TypeError):
            obj_mock: MockGuiVComponent = MockGuiVComponent("beer")
            obj: GuiVComponent = GuiVComponent(obj_mock)

    def test__init__ignore_incompatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute but its value is incompatible.
        Does not perform type checking."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("beer")
        obj: GuiVComponent = GuiVComponent(obj_mock, validate_type=False)
        self.assertEqual(obj.element, obj_mock)

    def test__init__compatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent(type="GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.element, obj_mock)

    def test_set_element(self) -> None:
        """Set the element attribute to None."""
        obj: GuiVComponent = GuiVComponent()
        obj.element = None
        self.assertIsNone(obj.element)

    def test_set_element_without_type(self) -> None:
        """Set an object with no 'Type' attribute for the element."""
        with self.assertRaises(TypeError):
            obj: GuiVComponent = GuiVComponent()
            obj_mock: MockGuiVComponentNoType = MockGuiVComponentNoType()
            obj.element = obj_mock

    def test_set_element_incompatible_value(self) -> None:
        """Set an object has the 'Type' attribute but its value is incompatible."""
        with self.assertRaises(TypeError):
            obj: GuiVComponent = GuiVComponent()
            obj_mock: MockGuiVComponent = MockGuiVComponent("beer")
            obj.element = obj_mock

    def test_set_element_ignore_incompatible_value(self) -> None:
        """Set an object has the 'Type' attribute but its value is incompatible.
        Does not perform type checking."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("beer")
        obj: GuiVComponent = GuiVComponent(validate_type=False)
        obj.element = obj_mock
        self.assertEqual(obj.element, obj_mock)

    def test_set_element_compatible_value(self) -> None:
        """Create object with argument.
        The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.element, obj_mock)

    def test_get_container_type(self) -> None:
        """The object has the 'ContainerType' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertTrue(obj.container_type)

    def test_get_container_type_with_element_none(self) -> None:
        """The element is none."""
        with self.assertRaises(TypeError):
            obj: GuiVComponent = GuiVComponent()
            objA: bool = obj.container_type

    def test_get_container_type_with_element_without_type(self) -> None:
        """Set an object with no 'Type' attribute for the element."""
        obj_mock: MockGuiVComponentNoType = MockGuiVComponentNoType()
        obj: GuiVComponent = GuiVComponent()
        try:
            obj.element = obj_mock
        except:
            with self.assertRaises(TypeError):
                objA: bool = obj.container_type

    def test_get_id(self) -> None:
        """The object has the 'Id' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.id, 'str id')

    def test_get_name(self) -> None:
        """The object has the 'Name' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.name, 'str name')

    def test_get_parent(self) -> None:
        """The object has the 'Parent' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.parent, {})

    def test_get_type(self) -> None:
        """The object has the 'Type' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.type, "GuiVComponent")

    def test_get_type_as_number(self) -> None:
        """The object has the 'TypeAsNumber' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.type_as_number, 1)

    def test_get_text(self) -> None:
        """The object has the 'Text' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.text, 'str text')

    def test_get_tooltip(self) -> None:
        """The object has the 'Tooltip' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.tooltip, 'str tooltip')

    def test_get_height(self) -> None:
        """The object has the 'Height' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.height, 1000)

    def test_get_left(self) -> None:
        """The object has the 'Left' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.left, 1001)

    def test_get_screen_left(self) -> None:
        """The object has the 'ScreenLeft' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.screen_left, 1002)

    def test_get_screen_top(self) -> None:
        """The object has the 'ScreenTop' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.screen_top, 1003)

    def test_get_top(self) -> None:
        """The object has the 'Top' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.top, 1004)

    def test_get_width(self) -> None:
        """The object has the 'Width' attribute and its value is compatible."""
        obj_mock: MockGuiVComponent = MockGuiVComponent("GuiVComponent")
        obj: GuiVComponent = GuiVComponent(obj_mock)
        self.assertEqual(obj.width, 1005)

if __name__ == '__main__':
    unittest.main()
