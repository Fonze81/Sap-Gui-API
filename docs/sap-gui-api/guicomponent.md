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

id  
name  
parent  
type  
type_as_number

## Methods

validate_element_type()
