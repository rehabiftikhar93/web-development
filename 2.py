Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '42'==42
False
>>> '42'==42.0
False
>>> 42.0==42
True
>>> #that means float can be equal to integer and vice versa but string ca not be equal to float or integer value.
>>> #Boolean values
>>> spam=true
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    spam=true
NameError: name 'true' is not defined
>>> spam=True
>>> spam
True
>>> spam=False
>>> spam
False
>>> spam+spam
0
>>> spam=spam
>>> #comparison opertors
>>> 42==42
True
>>> 42!=42
False
>>> 2!=3
True
>>> 2!=2
False
>>> 'hello'=='hello'
True
>>> 'hello'=='Hello'
False
>>> True!=False
True
>>> 0.42=>42
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> 0.42==42
False
>>> 42==42.0
True
>>> myage=90
>>> myage>=10
True
>>> #boolean operators
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> not true
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    not true
NameError: name 'true' is not defined
>>> not True
False
>>> not False
True
>>> #mixing comparison and boolean operators
>>> (4<5) and (8>4)
True
>>> (1==2) or (2==2)
True
>>> 2+2==4 and not 2+2==5 and 2+2==2*2
True

>>> #elements of flow control
>>> if name=='mary':
	print ('hi, mary')
	if password=='swordfish':
		print ('access granted')
		else:
			
SyntaxError: invalid syntax
>>> if name=='mary':
	print ('hi, mary')
	if password=='swordfish':
		print ('access granted')if name=='mary':
			print ('hi, mary')
			if password=='swordfish':
				print ('access granted')
				
SyntaxError: invalid syntax
>>> if name=='mary':
	print ('hi,mary')
	if password=='swordfish':
		print ('access granted')
		else:
			
SyntaxError: invalid syntax
>>> if name=='rehab':
	print ('hi, rehab.')
	else:
		
SyntaxError: invalid syntax
>>> if name=='rehab':
	print ('hi rehab')
    else:
	print ('hello stranger')
	
SyntaxError: unindent does not match any outer indentation level
>>> 
===================== RESTART: C:/Users/Haier/Desktop/if.py ====================
Traceback (most recent call last):
  File "C:/Users/Haier/Desktop/if.py", line 1, in <module>
    if name=='rehab':
NameError: name 'name' is not defined
>>> 
===================== RESTART: C:/Users/Haier/Desktop/if.py ====================
Traceback (most recent call last):
  File "C:/Users/Haier/Desktop/if.py", line 1, in <module>
    if name=='rehab':
NameError: name 'name' is not defined
>>> 
