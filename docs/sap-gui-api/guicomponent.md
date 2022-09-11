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

name  
parent  
type  
type_as_number

## Methods

validate_element_type()
