![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Pickle
* The `pickle` module provides a way to serialize and deserialize Python objects to and from a binary format.
* Pickling is the process of converting a Python object hierarchy into a byte stream, and unpickling is the reverse process of converting a byte stream back into a Python object hierarchy.
* Pickling is often used to save and load Python objects, and is a popular way to store data in a file or database.
* **Serialization** is the process of converting an object state into a binary file, this file can be stored on filesystem or transmitted across network or it can be persisted(stored) and later use. 
* Serialization of an object is also known as deflating or marshalling.
* In order to resurrect an Object from a Pickle file it needs to be deserialized.
* **Deserialization** of a file into an object also known as inflating or unmarshalling.
```python
import pickle;

# Serialization of an Object
# Create a Class
class PickleTest():
    
    a=0
    b=0
    
    def __init__(self,i_a,i_b):
        self.a=i_a
        self.b=i_b

# Create an Object
Obj1 = PickleTest(1,2)

# Serialize an Object
with open('C:/tinitiate/object.pickle', 'wb') as f:
	pickle.dump(Obj1, f)
    
# DeSerialize File to Object
with open('C:/tinitiate/object.pickle', 'rb') as f:
	ObjFile = pickle.load(f)

print(ObjFile)

print(ObjFile.a)
print(ObjFile.b)



# Serialization of a Dictionary
# Create a Dict
Dict1={'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Serialize an Dict
with open('C:/tinitiate/dict.pickle', 'wb') as f:
	pickle.dump(Dict1, f)

# DeSerialize File to Object
with open('C:/tinitiate/dict.pickle', 'rb') as f:
	DictFile = pickle.load(f)
    
print(DictFile)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|