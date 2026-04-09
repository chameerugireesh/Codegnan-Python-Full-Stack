Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> print(10)
10
>>> y=10
>>> y
10
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> a123456789=11
>>> print(123456789)
123456789
>>> x="gireesh"
>>> print(x)
gireesh
>>> print(x")
      
SyntaxError: EOL while scanning string literal
>>> print("x")
x
>>> city="vjy
SyntaxError: EOL while scanning string literal
>>> city="vjy"
>>> print("city")
city
>>> a,b=10,11
>>> print(a,b)
10 11
>>> x,y="hi","gireesh"
>>> print(x,"",y)
hi  gireesh
>>> x,y=1,2,3
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x,y=1,2,3
ValueError: too many values to unpack (expected 2)
>>> del x,y
>>> print(x,y)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(x,y)
NameError: name 'x' is not defined
>>> fname,lname="hi","gireesh"
>>> print(fname,lname)
hi gireesh
>>> 