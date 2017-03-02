import itertools

global true 
global false 

true = 0
false = 0

def logical_xor(a, b):
    if bool(a) == bool(b):
		return [ False ]
	else:
		if a or b :
			return [True]
		else:
			return [False]

def logical_and(a,b):
		if a and b:
			return [True]
		else :
			return [False]


def logical_or(a,b):
		if a or b :
			return [True]
		else :
			return [False]

list = [True, 'or', False, 'xor', True]


def rec (list, num, length):
		if length == 1 :
			if list[0] :
				true+=1
			else :
				false+=1
		else :
			if num == 1 :
				pass

print('original list' )
print(list)

list1 =  logical_or(list[0], list[2]) + list[0+3:]
				
print('new list' )
print(list)


