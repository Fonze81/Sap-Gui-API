"""
SAP GUI Scripting API
---------------------

DEVELOPER GUIDE | PUBLIC
Document Version: 7.60 PL1 – 2019-03-28
https://help.sap.com/doc/9215986e54174174854b0af6bb14305a/760.01/en-US/sap_gui_scripting_api_761.pdf
"""

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
# TODO Create class based on the documentation of the 'GuiComponent'

class GuiComponent(object):
    """GuiComponent is the base class for most classes in the Scripting API.

    It was designed to allow generic programming, meaning you can work with objects without knowing
    their exact type.
    """

    # See PEP 591 – Adding a final qualifier to typing
    VALID_TYPES: list = ['GuiComponent']

    @property
    def element(self: object) -> object:
        """
        Class attribute to which the SAP element should be referenced.

        Returns:
            object: SAP element
        """
        return self._element

    @element.setter
    def element(self: object, value: object):
        self._element = value
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
        built in a URL like formatting, starting at the GuiApplication
        object and drilling down to the respective object.
        """
        self._validate_element_type()
        return self._element.Id

    @property
    def name(self: object) -> str:
        """
        *Read-only*.

        The name property is especially useful when working with
        simple scripts that only access dynpro fields. In that case a
        field can be found using its name and type information,
        which is easier to read than a possibly very long id. However,
        there is no guarantee that there are no two objects with the
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

    #_type = self.type
    #_type_as_number = self.type_as_number
    def _validate_element_type(self):
        pass

    def __init__(self: object, element: object = None):
        # Constructor.
        self._element = element


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
# TODO Create class based on the documentation of the 'GuiVComponent'
# TODO Create class based on the documentation of the 'GuiVContainer'
# TODO Create class based on the documentation of the 'GuiVHViewSwitch'
