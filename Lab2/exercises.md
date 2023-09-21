# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

Dictionary is an unordered hashmap, and list is an ordered array,

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pros:

1. Flexibility: Use containers for various data types.
2. Code Reusability: One container handles multiple data types.
3. Extensibility: Easily adapt to new data types.
4. Readability: Concise code without type-specific versions.
5. Maintenance: Single container codebase is easier to manage.
Cons:

1. Performance Overhead: Generics/duck typing can introduce latency.
2. Type Safety: Potential for runtime type errors.
3. Complexity: Underlying implementation can be intricate.
4. Memory Overhead: Generic containers might use more memory.
5. Potential Misuse: Storing mixed, unrelated data types can convolute code.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes, they are well named.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes, for example: send(), which takes request, stream, timeout, verify, cert and proxies as parameters.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

**kwargs in Python is a syntax for passing a variable number of keyword arguments to a function or method.

Pros: **kwargs offers flexibility in accepting varied named parameters and facilitates function extensibility without changing signatures.

Cons: Its use can obscure clear function expectations and complicate debugging due to unintended parameter interactions.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


Arguments set to None provide default values, allowing optional parameters. Defaults aren't limited to None; any value can be used. Predetermined values simplify function calls, ensuring consistent behavior without requiring callers to always provide those arguments. However, they must be used judiciously to avoid unexpected behaviors.
