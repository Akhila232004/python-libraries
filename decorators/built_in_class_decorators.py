# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Built-in Class Decorators
#  Author       : Team Tinitiate
# ==============================================================================



# Create class with two methods
class tinitiate:
    "Class to demonstrate @classmethod and @staticmethod Decorations"

    # Decorated using the `@classmethod`
    @classmethod
    def class_function(cls, x):
        print(cls, x)

    # Decorated using the `@staticmethod`
    # No need to pass the "self" (the object instance) for static method
    @staticmethod
    def static_function(x):
        print(x)

# Create an object of the class tinitiate
obj = tinitiate()

# Call the "CLASS_FUNCTION" using the object
obj.class_function("Class Object Test")

# Call the "STATIC_FUNCTION" using the object
obj.static_function("Static Object Test")

# Call the "STATIC_FUNCTION" directly without the object
tinitiate.static_function("Static Test")

# Call the "CLASS_FUNCTION" directly without the object
tinitiate.class_function("Class Test")
