# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- Without specific code to reference, it's hard to definitively classify MObject as abstract or concrete. However, generally speaking, a concrete class is one that can be instantiated on its own, while an abstract class cannot and requires subclassing with defined abstract methods. If MObject can be instantiated on its own and contains implementation details, it's a concrete class. If not, and if it declares abstract methods that need to be implemented by subclasses, it's an abstract class.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- The __del__ method in Python is a special method that is invoked when an object is about to be destroyed (when its reference count reaches zero). If the 'Image' class has a commented out __del__ method, it's likely that it was intended to perform some cleanup operations like releasing resources when an Image object is no longer needed, but was commented out for some reason, possibly due to bugs or unwanted behavior.
1. What class does Texture inherit from?
	-It appears from the context provided that the 'Texture' class inherits from the 'Image' class. The inheritance relationship is typically established in the class definition like so: class Texture(Image):. However, without the actual code, it's hard to provide a definitive answer.
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- When 'Texture' inherits from 'Image', it inherits all of the public and protected methods and attributes defined in the 'Image' class. This would typically include methods to manipulate and query image data, and attributes that store the image data and metadata. Without the actual code of the 'Image' class, it's challenging to provide a detailed list of inherited methods and attributes. However, any method or attribute defined in 'Image' (that is not private) would be available to 'Texture' through inheritance.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- A "has-a" relationship (composition) is more suitable if a 'Texture' utilizes an 'Image' but isn't fundamentally an 'Image'. It makes the code more flexible and easier to extend.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, Python automatically provides a default constructor if you don't declare one. If specific initialization is needed, you'd define your own __init__ method.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
No, the object creation code in the instance function is not wrapped in a mutual exclusive block, which is necessary to ensure thread safety during instantiation in a multi-threaded environment.
*edit the code directly*  
  
