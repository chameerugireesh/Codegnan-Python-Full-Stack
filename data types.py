Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> ptint(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ptint(a)
NameError: name 'ptint' is not defined
>>> print(a)
10
>>> print(type(a))
<class 'int'>
>>> print("value of a and type: ",a,type(a))
value of a and type:  10 <class 'int'>
>>> print("value of a and type: ",a,"the type of a:"type(a))
SyntaxError: invalid syntax
>>> print("value of a and type: ",a,"the type of a:",type(a))
value of a and type:  10 the type of a: <class 'int'>
>>> print("value of a and type: ",a,/n"the type of a:"type(a))
SyntaxError: invalid syntax
>>> 
>>> v=true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    v=true
NameError: name 'true' is not defined
>>> v=True
>>> print(v)
True
>>> 
>>> 
>>> 
>>> 
>>> y=3+5j
>>> print(y)
(3+5j)
>>> y=5+6j
>>> type(y)
<class 'complex'>
>>> 