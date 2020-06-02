Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> some_string = "My first string!"
>>> type(some_string)
<class 'str'>
>>> print(some_string)
My first string!
>>> some_string = input("type something: ")
type something: Hello
>>> type(some_string)
<class 'str'>
>>> print(some_string)
Hello
>>> numeric_string = "5.0"
>>> type(numeric_string)
<class 'str'>
>>> print(numeric_string)
5.0
>>> #what happens if we try to add a number
>>> #to a numeric string?
>>> print(numeric_string + 3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(numeric_string + 3)
TypeError: Can't convert 'int' object to str implicitly
>>> a_number = 5
>>> #an example of casting a number to a
>>> #string
>>> a_number = str(a_number)
>>> type(a_number)
<class 'str'>
>>> #When string goes bad
>>> some_string = "5.3a"
>>> float = (some_string)
>>> 
