Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=str("Hello World")
>>> reverse(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    reverse(a)
NameError: name 'reverse' is not defined
>>> print("the reverse of string is",a)
the reverse of string is Hello World
>>> reverse str(a)
SyntaxError: invalid syntax
>>> reverse(str(a))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    reverse(str(a))
NameError: name 'reverse' is not defined
>>> a=str("World Hello")
>>> print(the reverse of string is",a)
	  
SyntaxError: invalid syntax
>>> 
	  

>>> print("the reverse of string is",a)
	  
the reverse of string is World Hello
>>> a=str("Hello World")
	  
>>> b=("World Hello")
	  
>>> print("The reverse of string is",b)
	  
The reverse of string is World Hello
>>> 
