def spam (DividedBy):
    try:
        return 42/DividedBy
    except ZeroDivisionError:
        print('error')
		
print (spam(2))
print (spam(12))
print (spam(0))
print (spam(1))

def spam (DividedBy):
		return 42/DividedBy
try:		
    print (spam(2))
    print (spam(12))
    print (spam(0))
    print (spam(1))
except ZeroDivisionError:
    print ('shit')

