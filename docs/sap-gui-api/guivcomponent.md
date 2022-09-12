<!-- Used for back to top link -->
<div id="top"></div>

# GuiVComponent :simple-sap:

## Description

The `GuiVComponent` interface is exposed by all visual objects, such as windows, buttons or text fields.  
Like GuiComponent, it is an abstract interface. Any object supporting the GuiVComponent interface also exposes the GuiComponent interface.
GuiVComponent extends the GuiComponent Object.

``` mermaid
classDiagram
    GuiComponent <|-- GuiVComponent
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
    class GuiVComponent{
        + &nbsp; acc_label_collection: GuiComponentCollection
        + &nbsp; acc_text: str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; acc_text_on_request: str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; acc_tooltip: str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; changeable: Byte &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; default_tooltip: str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; element : object
        # &nbsp; _element : object
        + &nbsp; height: Long &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; icon_name: str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; is_symbol_font: Byte &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; left: Long &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; modified: Byte
        + &nbsp; parent_frame: GuiComponent &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; screen_left: Long &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; screen_top: Long &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; text: str
        + &nbsp; tooltip: str &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; top: Long &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        + &nbsp; width: Long &lbrace;&lbrace;&nbsp; readOnly &nbsp;&rbrace;&rbrace;
        - &nbsp; __init__()
        &# &nbsp; _validate_element_type(self : object)
        + &nbsp; dump_state(inner_object: str) -> object:
        + &nbsp; set_focus()
        + &nbsp; visualize(on: bool, inner_object: Variant = None) -> Byte:
    }
```

## Attributes

### ```acc_label_collection``` <sup>:simple-sap:</sup>

**GuiComponentCollection**

### ```acc_text``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

### ```acc_text_on_request``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

### ```acc_tooltip``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

### ```changeable``` <sup>:simple-sap:</sup>

**Byte** &nbsp; <sup>read-only</sup>

### ```default_tooltip``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

### ```height``` <sup>:simple-sap:</sup>

**Long** &nbsp; <sup>read-only</sup>

### ```icon_name``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

### ```is_symbol_font``` <sup>:simple-sap:</sup>

**Byte** &nbsp; <sup>read-only</sup>

### ```left``` <sup>:simple-sap:</sup>

**Long** &nbsp; <sup>read-only</sup>

### ```modified``` <sup>:simple-sap:</sup>

**Byte**

### ```parent_frame``` <sup>:simple-sap:</sup>

**GuiComponent** &nbsp; <sup>read-only</sup>

### ```screen_left``` <sup>:simple-sap:</sup>

**Long** &nbsp; <sup>read-only</sup>

### ```screen_top``` <sup>:simple-sap:</sup>

**Long** &nbsp; <sup>read-only</sup>

### ```text``` <sup>:simple-sap:</sup>

**str**

### ```tooltip``` <sup>:simple-sap:</sup>

**str** &nbsp; <sup>read-only</sup>

### ```top``` <sup>:simple-sap:</sup>

**Long** &nbsp; <sup>read-only</sup>

### ```width``` <sup>:simple-sap:</sup>

**Long** &nbsp; <sup>read-only</sup>

## Methods

### ```dump_state(inner_object)``` <sup>:simple-sap:</sup>

*inner_object* = **str**  
*return* = **object**

### ```set_focus()``` <sup>:simple-sap:</sup>

### ```visualize(on, inner_object = None)``` <sup>:simple-sap:</sup>

*on* = **bool** *inner_object* = **Variant**  
*return* = **Byte**


<!-- Link to top -->
<p align="right"><a href="#top">back to top</a></p>