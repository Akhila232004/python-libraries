# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Create And Write To XML Using ElementTree
#  Author       : Team Tinitiate
# ==============================================================================



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
myfile = open("C:/tinitiate/test-data-output.xml", "w")
myfile.write(mydata)
