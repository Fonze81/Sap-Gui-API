"""
SAP GUI Scripting API
---------------------

DEVELOPER GUIDE | PUBLIC
Document Version: 7.60 PL1 – 2019-03-28
https://help.sap.com/doc/9215986e54174174854b0af6bb14305a/760.01/en-US/sap_gui_scripting_api_761.pdf
"""

import logging
from typing import Final, Literal, final

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh: logging.FileHandler = logging.FileHandler('./log/sap_api.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter: logging.Formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(fh)

# TODO Create class based on the documentation of the 'GuiAbapEditor'
# TODO Create class based on the documentation of the 'GuiApoGrid'
# TODO Create class based on the documentation of the 'GuiApplication'
# TODO Create class based on the documentation of the 'GuiBarChart'
# TODO Create class based on the documentation of the 'GuiBox'
# TODO Create class based on the documentation of the 'GuiButton'
# TODO Create class based on the documentation of the 'GuiCalendar'
# TODO Create class based on the documentation of the 'GuiChart'
# TODO Create class based on the documentation of the 'GuiCheckBox'
# TODO Create class based on the documentation of the 'GuiCollection'
# TODO Create class based on the documentation of the 'GuiColorSelector'
# TODO Create class based on the documentation of the 'GuiComboBox'
# TODO Create class based on the documentation of the 'GuiComboBoxControl'
# TODO Create class based on the documentation of the 'GuiComboBoxEntry'


class GuiComponent(object):
    """
    GuiComponent is the base class for most classes in the Scripting API.
    It was designed to allow generic programming, meaning you can work with objects without knowing
    their exact type.

    Attributes
    ----------
        element : object
            Attribute to be referenced to the SAP element.
        container_type : bool (read-only)
            This property is TRUE, if the object is a container and therefore
            has the Children property.
        is_valid : bool (read-only)
            Checks if the element is valid.
            After assigning a Sap element to the object,
            the object is dereferenced in some interface updates.
        container_type : bool (read-only)
            This property is TRUE, if the object is a container and therefore
            has the Children property.
        id : str (read-only)
            An object id is a unique textual identifier for the object. It is
            built in a URLlike formatting, starting at the GuiApplication
            object and drilling down to the respective object.
        name :  str (read-only)
            The name property is especially useful when working with
            simple scripts that only access dynpro fields.
            In that case a field can be found using its name and type information,
            which is easier to read than a possibly very long id.
            However, there is no guarantee that there are no two objects with the
            same name and type in a given dynpro.
        parent : object (read-only)
            The parent of an object is one level higher in the runtime hierarchy.
            An object is always in the children collection of its parent.
        type : str (read-only)
            The type information of GuiComponent can be used to determine which properties and
            methods an object supports.
            The value of the type string is the name of the type taken
            from this documentation.
        type_as_number : int (read-only)
            While the Type property is a string value,
            the TypeAsNumber property is a long value that can alternatively
            be used to identify an object's type .
            It was added for better performance in methods such as FindByIdEx.
            Possible values for this property are taken from the
            GuiComponentType enumeration.
    """

    # See PEP 591 – Adding a final qualifier to typing
    VALID_TYPES: list = ['GuiComponent']

    @property
    def element(self: object) -> object:
        """
        Attribute to be referenced to the SAP element.
        """
        self._validate_element_type()
        return self._element

    @element.setter
    def element(self: object, element_sap: object):
        if element_sap is None:
            self._element = element_sap
        elif hasattr(element_sap, 'Type'):
            self._element = element_sap
        else:
            raise AttributeError(name='Type')
        self._validate_element_type()

    @property
    def container_type(self: object) -> bool:
        """
        *Read-only*.

        This property is TRUE, if the object is a container and therefore
        has the Children property.
        """
        self._validate_element_type()
        return self._element.ContainerType

    @property
    def id(self: object) -> str:
        """
        *Read-only*.

        An object id is a unique textual identifier for the object. It is
        built in a URLlike formatting, starting at the GuiApplication
        object and drilling down to the respective object.
        """
        self._validate_element_type()
        return self._element.Id

    @property
    def name(self: object) -> str:
        """
        *Read-only*.

        The name property is especially useful when working with
        simple scripts that only access dynpro fields.
        In that case a field can be found using its name and type information,
        which is easier to read than a possibly very long id.
        However, there is no guarantee that there are no two objects with the
        same name and type in a given dynpro.
        """
        self._validate_element_type()
        return self._element.Name

    @property
    def parent(self: object) -> object:
        """
        *Read-only*.

        The parent of an object is one level higher in the runtime hierarchy.
        An object is always in the children collection of its parent.
        """
        self._validate_element_type()
        return self._element.Parent

    @property
    def type(self: object) -> str:
        """
        *Read-only*.

        The type information of GuiComponent can be used to determine which properties and
        methods an object supports.
        The value of the type string is the name of the type taken
        from this documentation.
        """
        self._validate_element_type()
        return self._element.Type

    @property
    def type_as_number(self: object) -> int:
        """
        *Read-only*.

        While the Type property is a string value,
        the TypeAsNumber property is a long value that can alternatively
        be used to identify an object's type .
        It was added for better performance in methods such as FindByIdEx.
        Possible values for this property are taken from the
        GuiComponentType enumeration.
        """
        self._validate_element_type()
        return self._element.TypeAsNumber

    @final  # See PEP 591 – Adding a final qualifier to typing
    def _validate_element_type(self) -> bool:
        """Check if the type of the assigned 'element' attribute is compatible.

        Raises:
            TypeError: The 'element' attribute has not been set.
            TypeError: The type of 'element' assigned is  not supported.

        Returns:
            bool: Returns true if supported
        """
        valid: bool = False
        # If the attribute has not been defined raise a TypeError
        if self._element == None:
            message = f"The 'element' attribute of class '{type(self).__name__}' object has not been set."
            raise TypeError(message)
        else:
            # Checks if the type is supported by the class
            element_type: str = self._element.Type
            for item in self.VALID_TYPES:
                if item == element_type:
                    valid = True
            if valid:
                return True
            else:
                message = f"The type of 'element' assigned to object of class '{type(self).__name__}' is  not supported."
                raise TypeError(message)

    @property
    def is_valid(self: object) -> bool:
        """Checks if the element is valid. Return True

        After assigning a Sap element to the object,
        the object is dereferenced in some interface updates."""
        valid: bool = False
        try:
            element_type: str = self._element.Type
            for item in self.VALID_TYPES:
                if item == element_type:
                    valid = True
        except:
            valid = False
        finally:
            if valid:
                return True
            else:
                return False

    def __init__(self: object, element: object = None):
        # Constructor.
        if element is None:
            self._element = element
        elif hasattr(element, 'Type'):
            self._element = element
        else:
            raise AttributeError(name='Type')

# TODO Create class based on the documentation of the 'GuiComponentCollection'
# TODO Create class based on the documentation of the 'GuiConnection'
# TODO Create class based on the documentation of the 'GuiContainer'
# TODO Create class based on the documentation of the 'GuiContainerShell'
# TODO Create class based on the documentation of the 'GuiContextMenu'
# TODO Create class based on the documentation of the 'GuiCTextField'
# TODO Create class based on the documentation of the 'GuiCustomControl'
# TODO Create class based on the documentation of the 'GuiDialogShell'
# TODO Create class based on the documentation of the 'GuiEAIViewer2D'
# TODO Create class based on the documentation of the 'GuiEAIViewer3D'
# TODO Create class based on the documentation of the 'GuiEnum'
# TODO Create class based on the documentation of the 'GuiFrameWindow'
# TODO Create class based on the documentation of the 'GuiGOSShell'
# TODO Create class based on the documentation of the 'GuiGraphAdapt'
# TODO Create class based on the documentation of the 'GuiGridView'
# TODO Create class based on the documentation of the 'GuiHTMLViewer'
# TODO Create class based on the documentation of the 'GuiInputFieldControl'
# TODO Create class based on the documentation of the 'GuiLabel'
# TODO Create class based on the documentation of the 'GuiMainWindow'
# TODO Create class based on the documentation of the 'GuiMap'
# TODO Create class based on the documentation of the 'GuiMenu'
# TODO Create class based on the documentation of the 'GuiMenubar'
# TODO Create class based on the documentation of the 'GuiMessageWindow'
# TODO Create class based on the documentation of the 'GuiModalWindow'
# TODO Create class based on the documentation of the 'GuiNetChart'
# TODO Create class based on the documentation of the 'GuiOfficeIntegration'
# TODO Create class based on the documentation of the 'GuiOkCodeField'
# TODO Create class based on the documentation of the 'GuiPasswordField'
# TODO Create class based on the documentation of the 'GuiPicture'
# TODO Create class based on the documentation of the 'GuiRadioButton'
# TODO Create class based on the documentation of the 'GuiSapChart'
# TODO Create class based on the documentation of the 'GuiScrollbar'
# TODO Create class based on the documentation of the 'GuiScrollContainer'
# TODO Create class based on the documentation of the 'GuiSession'
# TODO Create class based on the documentation of the 'GuiSessionInfo'
# TODO Create class based on the documentation of the 'GuiShell'
# TODO Create class based on the documentation of the 'GuiSimpleContainer'
# TODO Create class based on the documentation of the 'GuiSplit'
# TODO Create class based on the documentation of the 'GuiSplitterContainer'
# TODO Create class based on the documentation of the 'GuiStage'
# TODO Create class based on the documentation of the 'GuiStatusbar'
# TODO Create class based on the documentation of the 'GuiStatusPane'
# TODO Create class based on the documentation of the 'GuiTab'
# TODO Create class based on the documentation of the 'GuiTableColumn'
# TODO Create class based on the documentation of the 'GuiTableControl'
# TODO Create class based on the documentation of the 'GuiTableRow'
# TODO Create class based on the documentation of the 'GuiTabStrip'
# TODO Create class based on the documentation of the 'GuiTextedit'
# TODO Create class based on the documentation of the 'GuiTextField'
# TODO Create class based on the documentation of the 'GuiTitlebar'
# TODO Create class based on the documentation of the 'GuiToolbar'
# TODO Create class based on the documentation of the 'GuiToolbarControl'
# TODO Create class based on the documentation of the 'GuiTree'
# TODO Create class based on the documentation of the 'GuiUserArea'
# TODO Create class based on the documentation of the 'GuiUtils'


class GuiVComponent:

    def __init__(self,
                 acc_label_collection,
                 acc_text,
                 acc_text_on_request,
                 acc_tooltip,
                 changeable,
                 default_tooltip,
                 element,
                 _element,
                 height,
                 icon_name,
                 is_symbol_font,
                 left,
                 modified,
                 parent_frame,
                 screen_left,
                 screen_top,
                 text,
                 tooltip,
                 top,
                 width):
        self.acc_label_collection = acc_label_collection
        self.acc_text = acc_text
        self.acc_text_on_request = acc_text_on_request
        self.acc_tooltip = acc_tooltip
        self.changeable = changeable
        self.default_tooltip = default_tooltip
        self.element = element
        self._element = _element
        self.height = height
        self.icon_name = icon_name
        self.is_symbol_font = is_symbol_font
        self.left = left
        self.modified = modified
        self.parent_frame = parent_frame
        self.screen_left = screen_left
        self.screen_top = screen_top
        self.text = text
        self.tooltip = tooltip
        self.top = top
        self.width = width

    def dump_state(self, inner_object):
        pass

    def set_focus(self):
        pass

    def visualize(self, on, inner_object=None):
        pass

# TODO Create class based on the documentation of the 'GuiVContainer'
# TODO Create class based on the documentation of the 'GuiVHViewSwitch'
