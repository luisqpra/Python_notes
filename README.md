# Python_notes
Notes own about python

## Differences between Lists, Tuples, and Sets

Data type | Mutable | Ordered | Indexing | Duplicate elements
----------|---------|---------|--------|-------------------
List | ✓ | ✓ | ✓ | ✓
Tuple | x | ✓ | ✓ | ✓
Set |✓ | x | x | x

## Lambda funtion
Lambda funtion is a funtion in a single line of code

![Lambda funtion](https://runestone.academy/ns/books/published/fopp/_images/lambda.gif "Lambda funtion")

## Utils

 <code>´__init__.py´</code> is a special Python file used to mark a directory as a Python package. It is executed when the package is imported and can be used to initialize the package or set up any necessary resources for the package. The file can be empty, but its presence in a directory indicates to Python that the directory should be considered a package and allows for other modules in the package to be imported and used.

 ## Naming conventions

 ### LowerCamelCase

* Funtions
* Methods

```python
def checkStatusApi():
    pass 
```

### UpperCamelCase

* Classes
* Exceptions - add at the end **Error**

```python
class MotionAPi():
    pass 
```

### Snake_case

* Functions 
* Variables

```python
def compute_angle_vectors():
    pass 
```

### SCREAMING_SNAKE_CASE

* Constants

```python
class TwitterApi:
    VERSION_API = 1
    URL_API = 'https://api.twitter.com' 
```