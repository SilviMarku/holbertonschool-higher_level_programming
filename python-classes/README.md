Python - Classes and Objects

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around the concept of objects. In OOP, objects are instances of classes, which serve as blueprints or templates for creating objects. This paradigm is based on four main principles: encapsulation, inheritance, polymorphism, and abstraction.

A "class" in OOP is a blueprint for creating objects. It defines the structure and behavior that its instances will have. For example, a "Car" class can have attributes like "color" and "model" and methods like "start_engine" and "stop_engine."

An "object" or "instance" is a concrete, individual entity created from a class. If "Car" is a class, then a specific car, such as "my_car," would be an object or instance of the "Car" class. You can create multiple instances from the same class, each with its own unique data and state.

The key difference between a class and an object is that a class is a blueprint or template, while an object is an actual instance created from that blueprint. Think of a class as the plan for a house, and an object as the actual house built following that plan.

Attributes in OOP are variables that store data about an object's state. For example, if you have a "Person" class, attributes could include "name," "age," and "address." These attributes define the characteristics of an object and its current state.

In Python, attributes can be classified as public, protected, or private based on naming conventions. Public attributes are accessible from anywhere, protected attributes have a single underscore prefix (e.g., "_protected"), indicating they should not be accessed directly from outside the class but can still be accessed, and private attributes have a double underscore prefix (e.g., "__private"), making them harder to access directly. However, Python uses name mangling to change the name of private attributes in a way that can still be accessed if needed.

"Self" in Python is a reference to the instance of a class and is used to access its attributes and methods within the class. It's the first parameter of methods in Python.

A "method" is a function defined within a class that operates on the class's attributes or performs actions associated with the class. For instance, a "calculate_area" method in a "Rectangle" class could calculate the area of a rectangle.

The "init" method is a special method in Python classes and serves as a constructor. It gets called when an object of the class is created and allows you to initialize its attributes. For example:


Code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Data abstraction, data encapsulation, and information hiding are fundamental concepts in OOP. Abstraction refers to simplifying complex reality by modeling classes based on their essential properties and behaviors. Encapsulation is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class). Information hiding is the concept of restricting access to certain details of an object and only exposing the necessary parts to the outside world.

A "property" in Python is a special kind of attribute that allows you to define custom behavior for getting and setting its value. It is used to control access to an attribute and can perform additional actions when the attribute is accessed or modified.

The difference between an attribute and a property in Python is that an attribute is a simple variable that stores data, while a property uses methods to define custom behavior for getting and setting the value associated with it. For example, you can use a property to ensure that a temperature attribute is always within a specific range.

In Python, you can use the @property decorator to define a getter method for a property and the @property_name.setter decorator to define a setter method. This allows you to control how attribute values are accessed and modified while maintaining compatibility with existing code that uses the attribute directly.

To dynamically create arbitrary new attributes for existing instances of a class, you can simply assign values to new attribute names using dot notation. For example:


Code
my_object.new_attribute = 42
You can also bind attributes to a class or object by using the setattr() function. For instance:

Code
setattr(my_object, 'new_attribute', 42)
The __dict__ attribute of a class or instance contains a dictionary that maps attribute names to their values. You can access and manipulate this dictionary to inspect or modify attributes dynamically.

Python finds the attributes of an object or class by first searching in the instance's namespace (its __dict__ dictionary). If the attribute is not found there, Python looks in the class's namespace and then in its base classes if it's a derived class. If the attribute is still not found, it raises an AttributeError.

The getattr() function in Python is used to retrieve the value of an attribute from an object. It takes three arguments: the object, the attribute name as a string, and an optional default value to return if the attribute does not exist. For example:

Code
value = getattr(my_object, 'attribute_name', default_value)
getattr() is handy when you want to access attributes dynamically or handle cases where an attribute may or may not exist on an object.

