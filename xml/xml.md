![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# XML
* XML (Extensible Markup Language) is a markup language used for representing structured data in a way that is both human-readable and machine-readable.

## Read XML Using DOM
* Reading XML file using DOM parsing using the `minidom` module.
* The Document Object Model (DOM), its very useful to randomly access elements of an XML.
* First operation is to parse the XML document.
* Each XML is made up of elements, its values (Optional) and attributes (optional). The trick is to get the an XML element using `getElementsByTagName`, with in that extract the element value and attribute as needed.
* Below is the XML, that will be used in the demo.
* Save the file as `test-data.xml` in `C:/your-path` folder
```xml
<tinitiate>
    <training>
        <course>JAVA</course>
        <course>UNIX</course>
        <course>PERL</course>
        <course>PYTHON</course>
    </training>
    <code id="1"> Python XML Parsing </code>
    <code id="2"> Python File writing </code>
</tinitiate>
```
```python
from xml.dom import minidom

# Create a DOM object by reading the XML
# Note: Change the folder to where the file is located
xmldoc = minidom.parse('C:/tinitiate/test-data.xml')

# Print the document node and name of the first child tag
print (xmldoc.nodeName)
print (xmldoc.firstChild.tagName)

# Extract Tag and its elements By Tag Name
# ==============================================================================
# Extract the TINITIATE element and its children from the xmldoc
tinitiate_elements = xmldoc.getElementsByTagName("tinitiate")

# Loop through a Tag Element and read underlying Elements / Attributes
# ==============================================================================
# Since we know the tinitiate element has children we use the loop
for tinitiate_element in tinitiate_elements:

    # For every tinitiate element, extract the next clind node, i.e, training
    training_elements = tinitiate_element.getElementsByTagName("training")

    # Get Values of the training_elements list
    # ========================================
    for training_element in training_elements:

        # For every course element, extract the next clind node, i.e, COURSE
        course_elements = training_element.getElementsByTagName("course")

        # Get Values of the course_elements list
        for course_element in course_elements:
            # For every course element, print the nodeValue,
            # NOTE: There is only ONE child Node at the lowest
            #       level so use index ZERO
            print(course_element.childNodes[0].nodeValue)

    # READING Attributes, in CODE element which is at 
    # the same level as the training_element
    # ===============================================
    code_elements = xmldoc.getElementsByTagName("code")

    # Print the number of elements with in a Tg    
    print("Total Count of 'CODE' elements in XML: ",len(code_elements))

    # Loop through the code_elements list
    # ===================================
    for code_element in code_elements:

        # print the attributes of every code_element
        print(code_element.attributes["id"].value)
        # print the NodeValue of every code_element
        print(code_element.childNodes[0].nodeValue)
```

## Read XML Using SAX
* Reading XML file using SAX parsing
* The Simple API for XML (SAX), its very useful to parse large XMl documents access elements of an XML. The entire document is NEVER loaded into memory, only the portions based on an element name are loaded, this program uses python `xml.SAX` module.
* Using `SAX` requires the developer to write `Contenthandler` by creating a subclass of `xml.sax.ContentHandler`, `startDocument()` and `endDocument()`
* `characters()` method is invoked whenever character data is found.
* First operation is to parse the XML document.
* Each XML is made up of elements, its values (Optional) and attributes (optional) The trick is to get the An XML element using `getElementsByTagName`, with in that extract the element value and attribute as needed.
* We'll use the same demo xml file as used for above topic.
```python
import xml.sax

# Define a class that inherits from xml.sax.ContentHandler
class TIContentHandler(xml.sax.ContentHandler):
    # Constructor method
    def __init__(self):
        # Call the constructor of the base class
        xml.sax.ContentHandler.__init__(self)
        # Initialize a variable to keep track of the current element being parsed
        self.CurrentData = ""
        
    # This method is called every time a new element is encountered in the XML file
    def startElement(self, name, attrs):
        # Print the name of the element
        print("startElement :" + name)
        # Update the value of the current data variable
        self.CurrentData = name
        # If the current element is "code", print its "id" attribute value
        if name == "code":
            print("\tattribute id=" + attrs.getValue("id"))
    
    # This method is called every time character data is encountered inside an element
    def characters(self, content):
        # If the current element is "course", print its value
        if self.CurrentData == "course":
            print(content)
        # If the current element is "code", print its value
        if self.CurrentData == "code":
            print(content)

    # This method is called every time the end of an element is encountered
    def endElement(self, name):
        # Print the name of the element
        print("endElement:"  + name)


# This function processes an XML file using the SAX parser and the TIContentHandler class
def SAXprocessXML(sourceFileName):
  # Open the XML file for reading
  source = open(sourceFileName)
  # Parse the XML file using the SAX parser and the TIContentHandler class
  xml.sax.parse(source, TIContentHandler())

# Note: Change the folder to where the file is located
SAXprocessXML('C:/tinitiate/test-data.xml')
```

## Create And Write To XML Using ElementTree
* The ElementTree module, provides the following
    * `ElementTree.Element` : Creates the Root Element
    * `ElementTree.SubElement` : Creates the Sub Element
    * `ElementTree.SubElement.text` : Sets the Element Value
    * `ElementTree.SubElement.set("id","Value")` : Set the Attribute Name and Value
```python
import xml.etree.ElementTree as ET

# Generate the XML File
# Create Root Element
root_element = ET.Element("tinitiate")

# Create Sub Element
training_element = ET.SubElement(root_element, "training")
course_element1 = ET.SubElement(training_element, "course")

# Set Sub Element Value
course_element1.text = "JAVA"
course_element2 = ET.SubElement(training_element, "course")
course_element2.text = "UNIX"
course_element3 = ET.SubElement(training_element, "course")
course_element3.text = "PERL"
course_element4 = ET.SubElement(training_element, "course")
course_element4.text = "PYTHON"
code_element1 = ET.SubElement(root_element, "code")

# Set Attribute
code_element1.set("id",str(1))
code_element1.text = "Python File Reading"
code_element2 = ET.SubElement(root_element, "code")
code_element2.set("id",str(2))
code_element2.text = "Python File Writing"

# create a new XML file with the results
mydata = ET.tostring(root_element, encoding='unicode')
print(mydata)

# Write the Generated XML to file
# Note: Change the folder to your desired location
myfile = open("C:/tinitiate/test-data-OUT.xml", "w")
myfile.write(mydata)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|