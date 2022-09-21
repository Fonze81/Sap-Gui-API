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


class GuiAbapEditor(GuiShell):
    """SAP Class 'GuiAbapEditor'

    The GuiAbapEditor object represents the new ABAP editor control available
    as of SAP_BASIS release 6.20 (see also SAP Note 930742).
    GuiAbapEditor extends GuiShell.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiApoGrid(GuiShell):
    """SAP Class 'GuiApoGrid'

    The GuiApoGrid object is component, which is similar to GuiGridView,
    but which contains additional SCM specific functions (used for example
    in transaction /sapapo/sdp94).
    GuiApoGrid extends GuiShell.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiApplication(GuiContainer):
    """SAP Class 'GuiApplication'

    The GuiApplication represents the process in which all SAP GUI activity
    takes place. If the scripting component is accessed by attaching to an
    SAPlogon process, then GuiApplication will represent SAPlogon.
    GuiApplication is a creatable class. However, there must be only one
    component of this type in any process.
    GuiApplication extends GuiContainer.
    """

    VALID_ENUMERATIONS: list = [10]
    """GuiComponentType constant enumerations"""
    pass


class GuiBarChart(GuiShell):
    """SAP Class 'GuiBarChart'

    The GuiBarChart is a powerful tool to display and modify time scale
    diagrams. The object is of a very technical nature. It should only be used
    for recording and playback, as most of the parameters cannot be determined
    in any other way.
    GuiBarChart extends GuiShell.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiBox(GuiVComponent):
    """SAP Class 'GuiBox'

    A GuiBox is a simple frame with a name. The items inside the frame are not
    children of the box. The type prefix is box.
    The name property is the ABAP fieldname.
    GuiBox extends GuiVComponent.
    """

    VALID_ENUMERATIONS: list = [62]
    """GuiComponentType constant enumerations"""
    pass


class GuiButton(GuiVComponent):
    """SAP Class 'GuiButton'

    GuiButton represents all push buttons that are on dynpros, the toolbar or
    in table controls.  The type prefix is btn, the name property is the
    fieldname taken from the SAP data dictionary
    There is one exception: for tabstrip buttons, it is the button id set in
    screen painter that is taken from the SAP data dictionary.
    GuiButton extends GuiVComponent.
    """

    VALID_ENUMERATIONS: list = [40]
    """GuiComponentType constant enumerations"""
    pass


class GuiCalendar(GuiShell):
    """SAP Class 'GuiCalendar'

    The calendar control can be used to select single dates or periods of
    time.
    GuiCalendar extends GuiShell.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiChart():
    """SAP Class 'GuiChart'

    The GuiChart object is of a very technical nature. It should only be used
    for recording and playback, as most of the parameters cannot be determined
    in any other way.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiCheckBox(GuiVComponent):
    """SAP Class 'GuiCheckBox'

    The type prefix is chk, the name is the fieldname taken from the SAP
    data dictionary.
    GuiCheckBox extends GuiVComponent.
    """

    VALID_ENUMERATIONS: list = [42]
    """GuiComponentType constant enumerations"""
    pass


class GuiCollection():
    """SAP Class 'GuiCollection'

    GuiCollection is similar to GuiComponentCollection, but its members are
    not necessarily extensions of GuiComponent. It can be used to pass a
    collection as a parameter to functions of scriptable objects.
    An object of this class is created by calling the CreateGuiCollection
    function of the GuiApplication.
    """

    VALID_ENUMERATIONS: list = [120]
    """GuiComponentType constant enumerations"""
    pass


class GuiColorSelector(GuiShell):
    """SAP Class 'GuiColorSelector'

    GuiColorSelector displays a set of colors for selection.
    It extends GuiShell.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiComboBox(GuiVComponent):
    """SAP Class 'GuiComboBox'

    The GuiComboBox looks somewhat similar to GuiCTextField,
    but has a completely different implementation.
    While pressing the combo box button of a GuiCTextField will open a new
    dynpro or control in which a selection can be made, GuiComboBox retrieves
    all possible choices on initialization from the server, so the selection
    is done solely on the client.
    The type prefix is cmb, the name is the fieldname taken from the SAP
    data dictionary.
    GuiComboBox extends GuiVComponent.
    """

    VALID_ENUMERATIONS: list = [34]
    """GuiComponentType constant enumerations"""
    pass


class GuiComboBoxControl(GuiShell):
    """SAP Class 'GuiComboBoxControl'

    GuiComboboxControl offers a combo box that can be used inside control
    containers (unlike the Dynpro element represented by GuiComboBox).
    GuiComboBoxControl extends GuiShell.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiComboBoxEntry():
    """SAP Class 'GuiComboBoxEntry'

    Members of the Entries collection of a GuiComboBox are of type
    GuiComBoxEntry.
    """

    VALID_ENUMERATIONS: list = ['?']  # TODO
    """GuiComponentType constant enumerations"""
    pass


class GuiComponent():
    """SAP Class 'GuiComponent'

    GuiComponent is the base class for most classes in the Scripting API.
    It was designed to allow generic programming, meaning you can work with
    objects without knowing their exact type.

    Simulates how the SAP class 'GuiComponent Object' object works.
    The difference is that the reference is made by the element attribute and not directly to the object.
    The reference can be made on initialization or by setting the element attribute.

    Note:
        For more information, see the developer guide for SAP GUI Scripting API,
        version 7.60 PL1 – 2019-03-28, item 1.2.15, page 78.

    Keyword Arguments:
        element (object) : A reference to the SAP element. (default: {None})
        validate_type (bool): If is 'false', validation of type is disabled.
            This is not recommended, except for collections. (default: {True})

    Attributes:
        element (object): A reference to the SAP element.
        is_valid (bool): Checks if the reference to a SAP element is valid. {Read-only}
        container_type (bool): SAP property 'ContainerType'. {Read-only}
        id (str): SAP property 'Id'. {Read-only}
        name (str): SAP property 'Parent'. {Read-only}
        parent (str): SAP property 'Parent'. {Read-only}
        type (str): SAP property 'Type'. {Read-only}
        type_as_number (str): SAP property 'TypeAsNumber'. {Read-only}

    Examples:
        >>> obj = GuiComponent()
        >>> obj.element = Session.FindById('id_of_element')

        or

        >>> obj = GuiComponent(Session.FindById('id_of_element'))

    Raises:
        TypeError: Object is incompatible with class.
        TypeError: SAP element type is incompatible with class.
        TypeError: None Type. The object was not referenced to a SAP element.
        TypeError: This object object does not have the property.
    """

    # See PEP 591 – Adding a final qualifier to typing
    VALID_TYPES: list = ['GuiComponent']
    VALID_ENUMERATIONS: list = [0]  # TODO

    def __init__(self, element: object = None, validate_type: bool = True) -> None:
        """Constructor."""
        self.__validate_type: bool = validate_type
        self.element: object = element

    @final
    @property
    def element(self) -> object:
        """A reference to the SAP element.

        The link between the SAP element and this object is made by the 'element' attribute.
        Is defined at initialization or by setting this attribute.
        Checks if the SAP element is compatible with the expected types for this class defined in the 'VALID_TYPES' constant.
        If the '____validate_type' attribute is 'false', validation is disabled. This is not recommended, except for collections.

        Arguments:
            value (object): SAP element.

        Raises:
            TypeError: Object is incompatible with class.
            TypeError: SAP element type is incompatible with class.

        Returns:
            object: None or SAP element.
        """
        return self._element

    @final
    @element.setter
    def element(self, value: object) -> None:
        if value is None:
            self._element: object = None
        elif not self.__has_type(value):
            self._element = None
            message: str = f"Object '{value}' is incompatible with class '{type(self).__name__}'."
            logger.error(message)
            raise TypeError(message)
        elif self.__compatible_type(value):
            self._element = value
        elif self.__validate_type:
            message: str = f"Element type '{value}' is incompatible with class '{type(self).__name__}'."
            logger.error(message)
            raise TypeError(message)
        else:
            message: str = f"The incompatibility between element type '{value}' and class '{type(self).__name__}' is disregarded."
            logger.warning(message)
            self._element = value

    @final
    @property
    def is_valid(self) -> bool:
        """Checks if the reference to a SAP element is valid.

        Returns:
            bool: True if valid.
        """
        result: bool = False
        try:
            if self.__compatible_type('Type'):
                result: Literal[True] = True
        except:
            result: Literal[False] = False
        finally:
            return result

    @final
    @property
    def container_type(self) -> bool:
        """SAP property 'ContainerType'.

        This property is TRUE, if the object is a container and therefore has the Children property.

        Returns:
            bool: True if the object is a container.
        """
        self.__has_valid('ContainerType')
        return self._element.ContainerType

    @final
    @property
    def id(self) -> str:
        """SAP property 'Id'.

        An object id is a unique textual identifier for the object.
        It is built in a URLlike formatting, starting at the GuiApplication object
        and drilling down to the respective object.

        Returns:
            str: A unique textual identifier of SAP element.
        """
        self.__has_valid('Id')
        return self._element.Id

    @final
    @property
    def name(self) -> str:
        """SAP property 'Name'.

        The name property is especially useful when working with simple scripts that only access dynpro fields.
        In that case a field can be found using its name and type information, which is easier to read than a possibly very long id.
        However, there is no guarantee that there are no two objects with the same name and type in a given dynpro.

        Returns:
            str: Name of SAP element.
        """
        self.__has_valid('Name')
        return self._element.Name

    @final
    @property
    def parent(self) -> object:
        """SAP property 'Parent'.

        The parent of an object is one level higher in the runtime hierarchy.
        An object is always in the children collection of its parent.

        Returns:
            object: The parent of SAP element. #TODO
        """
        self.__has_valid('Parent')
        return self._element.Parent

    @final
    @property
    def type(self) -> str:
        """SAP property 'Type'.

        The type information of GuiComponent can be used to determine which properties and methods an object supports.

        Returns:
            str: Name of the type SAP element.
        """
        self.__has_valid('Type')
        return self._element.Type

    @final
    @property
    def type_as_number(self) -> int:
        """SAP property 'TypeAsNumber'.

        While the 'Type' property is a string value,
        the 'TypeAsNumber' property is a long value that can alternatively
        be used to identify an object's type.
        It was added for better performance in methods such as FindByIdEx.

        Returns:
            int: Possible values for this property are taken from the GuiComponentType enumeration.
        """
        self.__has_valid('TypeAsNumber')
        return self._element.TypeAsNumber

    @final
    def __compatible_type(self, value: object) -> bool:
        """Checks for type compatibility.

        Checks if the protected attribute '_element' in your property 'Type'
        has one of the types listed in the constant 'VALID_TYPES'.

        Arguments:
            value (object): Object to be checked.

        Returns:
            bool: True if compatible.
        """
        result: Literal[False] = False
        element_type: str = value.Type
        for item in self.VALID_TYPES:
            if item == element_type:
                result: Literal[True] = True
        return result

    @final
    def __has_type(self, value: object) -> bool:
        """Checks if the object has 'Type' property.

        Arguments:
            value (object): Object to be checked.

        Returns:
            bool: Returns true if has the 'Type' property.
        """
        return hasattr(value, 'Type')

    @final
    def __has_valid(self, value: str) -> bool:
        """Checks if the '_element' protected attribute has a SAP property.

        Throws an error if the SAP element is not referenced (None).
        Throws an error if the SAP element doesn't have the property.
        Hint!!! It's possible that the SAP interface has been updated and the object has lost the reference.
        Hint!!! It's possible that the connection to SAP was dropped.
        Hint!!! It's possible that has occurred an access violation to the protected attribute '_element'.

        Args:
            value (str): Name of the SAP property.

        Raises:
            TypeError: None Type. The object was not referenced to a SAP element.
            TypeError: This object object does not have the property.

        Returns:
            bool: Returns true if has the SAP property.
        """
        result: Literal[False] = False
        if self._element is None:
            message: str = f"None Type. The object '{self}' was not referenced to a Sap element."
            logger.error(message)
            raise TypeError(message)
        elif not hasattr(self._element, value):
            message: str = f"""The '{self}' object does not have the '{value}' property.
                Validation is performed at object initialization or setting the 'element' attribute.
                Hint!!! It's possible that the SAP interface has been updated and the object has lost the reference.
                Hint!!! It's possible that the connection to SAP was terminated or dropped.
                Hint!!! It's possible that has occurred an access violation to the protected attribute '_element'."""
            logger.error(message)
            raise TypeError(message)
        else:
            result: Literal[True] = True
        return result


class GuiComponentCollection():
    """SAP Class 'GuiComponentCollection'

    The GuiComponentCollection is used for collections elements such as the
    children property of containers. Each element of the collection is an
    extension of GuiComponent.
    """

    VALID_ENUMERATIONS: list = [128]
    """GuiComponentType constant enumerations"""
    pass


class GuiConnection(GuiContainer):
    """SAP Class 'GuiConnection'

    A GuiConnection represents the connection between SAP GUI and an
    application server. Connections can be opened from SAPlogon or from
    GuiApplication's openConnection and openConnectionByConnectionString
    methods. The type prefix for GuiConnection is con, the name is con
    plus the connection number in square brackets.
    GuiConnection extends GuiContainer.
    """

    VALID_ENUMERATIONS: list = [11]
    """GuiComponentType constant enumerations"""
    pass


class GuiContainer(GuiComponent):
    """SAP Class 'GuiContainer'

    This interface resembles GuiVContainer. The only difference is that it is
    not intended for visual objects but rather administrative objects such as
    connections or sessions. Objects exposing this interface will therefore
    support GuiComponent but not GuiVComponent.
    GuiContainer extends GuiComponent.
    """

    VALID_ENUMERATIONS: list = [70]
    """GuiComponentType constant enumerations"""
    pass


class GuiContainerShell():
    """SAP Class 'GuiContainerShell'

    A GuiContainerShell is a wrapper for a set of GuiShell objects.
    GuiContainerShell extends GuiVContainer. The type prefix is shellcont,
    the name is the last part of the id, shellcont[n].
    """

    VALID_ENUMERATIONS: list = [51]
    """GuiComponentType constant enumerations"""
    pass


class GuiCTextField(GuiTextField):
    """SAP Class 'GuiCTextField'

    If the cursor is set into a text field of type GuiCTextField a combo box
    button is displayed to the right of the text  field.
    Pressing this button is equivalent to pressing the F4 key.
    The button is not represented in the scripting object model as a separate
    object; it is considered to be part of the text  field.
    There are no other differences between GuiTextField and GuiCTextField.
    The type prefix is ctxt, the name is the Fieldname taken from the SAP
    data dictionary.
    GuiCTextField extends GuiTextField.
    """

    VALID_ENUMERATIONS: list = [32]
    """GuiComponentType constant enumerations"""
    pass

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


class GuiVComponent(GuiComponent):

    VALID_TYPES: list = ['GuiComponent', 'GuiVComponent']

    @final
    @property
    def acc_label_collection(self) -> object:
        return self._element.AccLabelCollection

    @final
    @property
    def acc_text(self) -> str:
        """SAP property 'AccText'.

        Returns:
            str: An additional text for accessibility support.
        """
        return self._element.AccText

    @final
    @property
    def acc_text_on_request(self) -> str:
        """SAP property 'AccTextOnRequest'.

        Returns:
            str: An additional text for accessibility support.
        """
        return self._element.AccTextOnRequest

    @final
    @property
    def acc_tooltip(self) -> str:
        """SAP property 'AccTooltip'.

        Returns:
            str: An additional tooltip text for accessibility support.
        """
        return self._element.AccTooltip

    @final
    @property
    def changeable(self) -> bool:
        return self._element.Changeable

    @final
    @property
    def default_tooltip(self) -> str:
        """SAP property 'DefaultTooltip'.

        Returns:
            str: Tooltip text generated from the short text defined in the data
                dictionary for the given screen element type.
        """
        return self._element.DefaultTooltip

    @final
    @property
    def height(self) -> int:
        """SAP property 'Height'.

        Returns:
            int: Height of the component in pixels.
        """
        return self._element.Height

    @final
    @property
    def icon_name(self) -> str:
        """SAP property 'IconName'.

        Returns:
            str: If the object has been assigned an icon, then this property is
                the name of the icon, otherwise it is an empty string.
        """
        return self._element.IconName

    @final
    @property
    def is_symbol_font(self) -> bool:
        return self._element.IsSymbolFont

    @final
    @property
    def left(self) -> int:
        """SAP property 'Left'.

        Returns:
            int: Left position of the element in screen coordinates.
        """
        return self._element.Left

    @final
    @property
    def modified(self) -> bool:
        return self._element.Modified

    @final
    @property
    def parent_frame(self) -> object:
        return self._element.ParentFrame

    @final
    @property
    def screen_left(self) -> int:
        """SAP property 'ScreenLeft'.

        Returns:
            int: The y position of the component in screen coordinates.
        """
        return self._element.ScreenLeft

    @final
    @property
    def screen_top(self) -> int:
        """SAP property 'ScreenTop'.

        Returns:
            int: The x position of the component in screen coordinates.
        """
        return self._element.ScreenTop

    @final
    @property
    def text(self) -> str:
        """SAP property 'Text'.

        Returns:
            str: The value of this property very much depends on the type of
                the object on which it is called. This is obvious for text fields
                or menu items. On the other hand this property is empty for
                toolbar buttons and is the class id for shells. You can read
                the text property of a label, but you can’t change it, whereas
                you can only set the text property of a password field, but
                not read it.
        """
        return self._element.Text

    @final
    @property
    def tooltip(self) -> str:
        """SAP property 'Tooltip'.

        Returns:
            str: The tooltip contains a text which is designed to help a user
                understand the meaning of a given text field or button.
        """
        return self._element.Tooltip

    @final
    @property
    def top(self) -> int:
        """SAP property 'Top'.

        Returns:
            int: Top coordinate of the element in screen coordinates.
        """
        return self._element.Top

    @final
    @property
    def width(self) -> int:
        """SAP property 'Width'.

        Returns:
            int: Width of the component in pixels.
        """
        return self._element.Width

    def dump_state(self, inner_object):
        pass

    def set_focus(self):
        pass

    def visualize(self, on, inner_object=None):
        pass

# TODO Create class based on the documentation of the 'GuiVContainer'
# TODO Create class based on the documentation of the 'GuiVHViewSwitch'
