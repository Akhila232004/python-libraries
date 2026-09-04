![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# XMLSchema
* XML Schema is a language used for describing the structure and content of XML documents.
* XML Schema defines a set of rules for elements and attributes within an XML document.
* XML Schema uses the XSD file extension file, and schemas are typically written in XML syntax.
* XML Schema supports data types such as strings, numbers, dates, and Booleans, and allows for custom data types to be defined.
* XML Schema allows for the definition of complex types, which can be used to describe hierarchical structures, repeating elements, and other advanced XML features.
* XML Schema supports element and attribute constraints, including minimum and maximum occurrence, length, and value ranges.
```bash
# To install 'xmlschema' run the following command
python -m pip install xmlschema
```

## Schema
The xml schema includes:
- `xs:schema`: This is the root element of an XML schema document. It contains declarations for all the elements and attributes that are allowed in the XML document that this schema describes. It may also include information about namespaces, imports, and includes.
- `xs:sequence`: This element is used to specify the order and number of child elements that can appear within an element. It contains one or more `xs:element` elements that represent the child elements allowed in a specific order.
- `xs:complexType`: This element is used to define a complex type, which can be used to describe the structure of an element that contains other elements or attributes. It can have one or more child elements, including `xs:sequence`, `xs:choice`, and `xs:attribute`. You can think of `xs:complexType` as a blueprint for defining the structure of an element.
- `xs:element`: This element is used to define an element in the XML document that this schema describes. It can specify the name of the element, its data type, and other attributes. An `xs:element` can have a child element `xs:complexType` or `xs:simpleType` to define the structure of its contents.
- `xs:choice`: This element is used to specify that one and only one of a given set of child elements must appear in an XML document. It is often used when an element can contain one of several alternatives, and you want to specify which alternatives are allowed. 
- `xs:attribute`: This element is used to define an attribute of an XML element. Attributes are used to provide additional information about an element, such as its size, color, or style. An `xs:attribute` element can specify the name and data type of the attribute, as well as any restrictions on its value.
### Sample 'product' XSD schema
* Save as `product.xsd`.
* Change any value as per your requirement.
```xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="http://www.example.com/product"
           xmlns="http://www.example.com/product"
           elementFormDefault="qualified">

  <xs:element name="Products">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="Product" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="ID" type="xs:int"/>
              <xs:element name="Name" type="xs:string"/>
              <xs:element name="Price" type="xs:decimal"/>
              <xs:element name="Category" type="xs:string" minOccurs="0"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```
### Sample 'product' XML
* Save as `product.xml`.
* Change any value as per your requirement.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Products xmlns="http://www.example.com/product">
  <Product>
    <ID>1</ID>
    <Name>Laptop</Name>
    <Price>750.00</Price>
    <Category>Electronics</Category>
  </Product>
  <Product>
    <ID>2</ID>
    <Name>Table</Name>
    <Price>120.50</Price>
    <Category>Furniture</Category>
  </Product>
</Products>
```

## XML Schema Validation
* Validating the 'product' XML data against the 'product' XSD schema.
```python
import xmlschema

# Load the XSD schema file
xsd_file = 'C:/tinitiate/product.xsd'
try:
    schema = xmlschema.XMLSchema(xsd_file)
except Exception as e:
    print(f"Failed to load XSD schema file: {e}")
    raise

# Load the XML data file
xml_file = 'C:/tinitiate/product.xml'
try:
    with open(xml_file, 'r') as f:
        xml_data = f.read()
except Exception as e:
    print(f"Failed to load XML data file: {e}")
    raise


# Validate the XML data against the XSD schema
is_valid = schema.is_valid(xml_data)

# Log the validation result
if is_valid:
    print("The XML data is valid according to the XSD schema.")
else:
    print("The XML data is not valid according to the XSD schema.")
    for e in schema.iter_errors(xml_file):
        print(e)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|