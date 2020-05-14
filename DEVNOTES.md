# Developer Notes

### Frameworks and Libraries

* Twisted - https://twistedmatrix.com/trac/

* logging - https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

* Documenting code - https://realpython.com/documenting-python-code/

* Property hiding - https://realpython.com/oop-in-python-vs-java/#public-and-private

* Interfaces - https://interview.codes/reference/essential-object-oriented-programming-for-a-python-interview/

* Type info for functions - https://www.python.org/dev/peps/pep-3107/

* Concurrency and locals - https://realpython.com/python-concurrency/

* Twisted and StartTLS

python docstring

```python

def area(base, height):
    '''(number, number ) -> number    #**TypeContract**
    Return the area of a tring with dimensions base   #**Description**
    and height

    >>>area(10,5)          #**Example **
    25.0
    >>area(2.5,3)
    3.75
    '''
    return (base * height) /2 

```