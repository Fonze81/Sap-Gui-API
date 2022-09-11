# GuiComponent :simple-sap:

## Description

`#!python GuiComponent: object` is the base class for most classes in the Scripting API.  
It was designed to allow generic programming, meaning you can work with objects without knowing
their exact type.

## Atributes

`#!python element: object` <small>:simple-python:</small>

Class attribute to which the SAP element should be referenced.

`#!python container_type: bool` <small>read-only :simple-sap:</small>

This property is TRUE, if the object is a container and therefore has the Children property.

`#!python id: str` <small>read-only :simple-sap:</small>

An object id is a unique textual identifier for the object. It is built in a URL like formatting, starting at the GuiApplication object and drilling down to the respective object.

`#!python name: str` <small>read-only :simple-sap:</small>

The name property is especially useful when working with simple scripts that only access dynpro fields. In that case a field can be found using its name and type information, which is easier to read than a possibly very long id. However, there is no guarantee that there are no two objects with the same name and type in a given dynpro.

`#!python parent: object` <small>read-only :simple-sap:</small>

The parent of an object is one level higher in the runtime hierarchy.
An object is always in the children collection of its parent.

`#!python type: str` <small>read-only :simple-sap:</small>

The type information of GuiComponent can be used to determine which properties and methods an object supports.
The value of the type string is the name of the type taken from this documentation.

`#!python type_as_number: int` <small>read-only :simple-sap:</small>

While the Type property is a string value, the TypeAsNumber property is a long value that can alternatively
be used to identify an object's type . It was added for better performance in methods such as FindByIdEx.
Possible values for this property are taken from the GuiComponentType enumeration.

## Methods

validate_element_type()
