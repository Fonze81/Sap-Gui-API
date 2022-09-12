<!-- Used for back to top link -->
<div id="top"></div>

# GuiComponent :simple-sap:

## Description

`GuiComponent` is the base class for most classes in the Scripting API.  
It was designed to allow generic programming, meaning you can work with objects without knowing their exact type.

``` mermaid
classDiagram
    class GuiComponent{
        + &nbsp; container_type : bool &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; element : object
        # &nbsp; _element : object
        + &nbsp; id : str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; is_valid : bool &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; name : str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; parent : object &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; type : str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; type_as_number : int &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        - &nbsp; __init__()
        &# &nbsp; _validate_element_type(self : object)
    }
```

## Attributes

### ```element```

**object**

Attribute to be referenced to the SAP element.

### ```is_valid```

**bool** &nbsp; <sup>read-only</sup>

Checks if the [element](#element) is valid. After assigning a Sap element to the object, he object is dereferenced in some interface updates.

### ```container_type``` <sup>:simple-sap:</sup>

**bool** &nbsp; <sup>read-only</sup>

This property is *true* if the object is a container and therefore has the Children property.

### ```id``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

An object `id` is a unique textual identifier for the object. It is built in a URLlike formatting, starting at the GuiApplication object and drilling down to the respective object.

### ```name``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

The `name` property is especially useful when working with simple scripts that only access dynpro fields. In that case a field can be found using its name and type information, which is easier to read than a possibly very long id.  
However, there is no guarantee that there are no two objects with the same name and type in a given dynpro.

### ```parent``` <sup>:simple-sap:</sup>

**object** &nbsp; <sup>read-only</sup>

The `parent` of an object is one level higher in the runtime hierarchy. An object is always in the children collection of its parent.

### ```type``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

The `type` information of [GuiComponent](#GuiComponent) can be used to determine which properties and methods an object supports.  
The value of the type string is the name of the type taken from this documentation.

### ```type_as_number``` <sup>:simple-sap:</sup>

**int** &nbsp; <sup>read-only</sup>

While the [type](#type) property is a string value, the `type_as_number` property is a long value that can alternatively be used to identify an object's type.  
It was added for better performance in methods such as FindByIdEx.  
Possible values for this property are taken from the GuiComponentType enumeration.


<!-- Link to top -->
<p align="right"><a href="#top">back to top</a></p>