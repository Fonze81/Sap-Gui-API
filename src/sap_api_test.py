import unittest
from sap_api import GuiComponent


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


if __name__ == '__main__':
    unittest.main()
