# def evenOdd(x):
#     if x % 2 == 0:
#         print(x, 'is even number!')
#     else:
#         print(x, 'is odd number!')
# evenOdd(4)        


# def swap(x, y):
#     temp = x
#     x = y
#     y = temp
   
# e = swap(3, 6)
# print(e)

# 28.
# 1. Required arguments:
# def printme(str):
#     print(str)
#     return
# printme("Banti kumar")

# 2.Keyword Argument:-
# def printme(name, age):
#     print(name, 'is', age, 'year old!')
#     return
# printme('banti_kumar', 18)
# printme('shubham ', 19)
# printme('Sonu_singh', 24)
# printme('Aman_bhai', 28)


# 3.Default Arguments-
# def printinfo(name, age = 35):
#     print('Name:', name)
#     print('Age', age)
#     return
# printinfo('Aman_bhai', 45)
# printinfo('sonu_sharama!')


# 4.:-
# Variable-Length Arguments:
# def printinfo(arg1, *vartuple):
#     print("Output is:s", arg1)
#     for var in vartuple:
#         print(var)
#     return;
# printinfo(140)
# printinfo(10, 20, 30)

# declaring docstring:-
# 1.
# def my_function():
#     """demonstrate docstrings and does nothing really."""
#     return None
# print("Using__doc__.")
# print(my_function.__doc__)

# print("Using help:")
# help(my_function)

# 2.
# def power(a, b):
#     """Returns args1 raised to power arg2"""
#     return a**b
# print(power.__doc__)
# print(power(2, 3))

# 3.
# # multi line docstrings:-
# def my_function(arg1):
#     """
# Summary Line.
# Extended description of function.
# Parameters:
# arg1 (int): Description of return value

# Returns:
# int: Description of return value
#     """
#     return arg1
# print(my_function.__doc__)


# Built in function:-
# x = abs(3+5j)
# print(x)
# c = -5
# print(abs(c))
# p = .32
# print(abs(p)) 

# print(abs(3+1j))

# 2.all()
# mylist = [True, True, True] 
# x = all(mylist)
# print(x)

# list = [0, 1, 1]
# c = all(list)
# print(c)


# list = [False, True, False]
# x = any(list)
# print(x)

# list = [1, 1, 1]
# y = any(list)
# print(x)

# mytuple = (0, 1, False)
# print(any(mytuple))

# mydict = {1:'banti', 2:'Sonu', 3:'Hariom'}
# print(any(mydict))

# D = {}
# print(any(D))

# x = ascii('My name is ståle')
# print(x)
# print(ascii('ååååå'))

# m = bin(9)
# print(m)
# print(bool(0))


# classmethod Function()
# class geeks:
#     course = 'DSA'
#     def Purchase(obj):
#         print('Purchase Course:', obj.course)
# geeks.Purchase = classmethod(geeks.Purchase)
# geeks.Purchase()


# from datetime import date


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)

#     def display(self):
#         print("Name : ", self.name, "Age : ", self.age)
# Person = Person('mayank', 21)
# Person.display()          
        

# OR
# Python program to demonstrate
# use of a class method and static method.
# from datetime import date

# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

	# a class method to create a
	# Person object by birth year.
# 	@classmethod
# 	def fromBirthYear(cls, name, year):
# 		return cls(name, date.today().year - year)

# 	# a static method to check if a
# 	# Person is adult or not.
# 	@staticmethod
# 	def isAdult(age):
# 		return age > 18

# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)

# print(person1.age)
# print(person2.age)

# # print the result
# print(Person.isAdult(22))


# x = compile('print(53.4)', 'test', 'eval')
# exec(x)
# print(x)

# x = compile('print(55)\nprint(88)', 'test', 'exec')
# exec(x)
# print(x)

# x = 'name = "John"\nprint(name)'
# exec(x)


# x = complex(3, 5)
# print(x)

# class Person:
#     name = 'Banti kumar'
#     age = 18
#     Country = 'India'
# delattr(Person, 'age')    
# x = getattr(Person, 'age')
# x1 = getattr(Person, 'name')
# x2 = getattr(Person, 'Country')
# print(x)
# print(x1)
# print(x2)

# x = hasattr(Person, 'age')
# x1 = hasattr(Person, 'name1')
# x2 = hasattr(Person, 'Country')
# print(x)
# print(x1)
# print(x2)

# setattr(Person, 'age', 30)
# setattr(Person, 'name', 'Preetam singh')
# setattr(Person, 'Country', 'America')

# x = getattr(Person, 'age')
# x1 = getattr(Person, 'name')
# x2 = getattr(Person, 'Country')
# print(x)
# print(x1)
# print(x2)


# x = dict(name='John', age=36, country="Norway")
# print(x)

# dict = {
#     'name':'preetam', 
#     'age' : 23, 
#     'country':'India'
# }

# print(dict['name'])
# print(dict['age'])
# print(dict['country'])

# class Person:
#     name = "Jaon"
#     age = 24
#     country = 'India'
# print(dir(Person))    


# x = divmod(8, 3)
# print(x)


# x = ('apple', 'banana', 'cherry')
# print(list(enumerate(x)))

# x = 'print(55)'
# eval(x)

# y = 'name = "John"\nprint(name)'
# exec(y)

# ages = [2, 5, 12, 47, 45, 5, 15, 69, 85]

# def myfunc(x):
#     if x < 18:
#         return False
#     else:
#         return True
# adults = filter(myfunc, ages)
# for x in adults:
#     print(x, end=', ')    
 
# ages = ('p', 'a', 'r', 'b', 'k')
# x = "".join(ages)
# print(x)

# x = float(4)
# print(x)

# x = format(0.5, '%')
# print(x) 
# print()
# print('<')
# print(format(255, '<'))
# print('>')
# print(format(255, '>'))
# print('^')
# print(format(255, '^'))
# print('=')
# print(format(255, '='))
# print('+')
# print(format(255, '+'))
# print('-')
# print(format(255, '-'))
# print(' ')
# print(format(255, ' '))
# print(', ')
# print(format(255, ','))
# print('_')
# print(format(255, '_'))
# print('b')
# print(format(255, 'b'))
# print('c')
# print(format(255, 'c'))
# print('d')
# print(format(255, 'd'))
# print('e')
# print(format(255, 'e'))
# print('E')
# print(format(255, 'E'))
# print('f')
# print(format(255, 'f'))
# print('F')
# print(format(255, 'F'))
# print('g')
# print(format(255, 'g'))
# print('G')
# print(format(255, 'G'))
# print('o')
# print(format(255, 'o'))
# print('x')
# print(format(255, 'x'))
# print('X')
# print(format(255, 'X'))
# print('n')
# print(format(255, 'n'))
# print('%')
# print(format(255, '%'))

# mylist = ['apple', 'banana', 'cherry']
# print(frozenset(mylist))

# x = globals()
# print(x)
# x=globals()
# print(x["__file__"])

# class Person:
#     name = 'Banti kumar'
#     age = 18
#     Country = 'India'
# x = hasattr(Person, 'Country')  
# print(x)

# int_val = 4
# str_val = 'GeeksforGeeks'
# flt_val = 25.63
# print('The integer hash value is:', str(hash(int_val)))
# print('The string hash value is:', str(hash(str_val)))
# print('The float hash value is:', str(hash(flt_val)))

# class helper:
#     def __init__(self):
#         '''The helper function is initialized'''
#     def print_help(self):
#         '''Returns the help Description'''
#         print('helper description')
# help(helper)
# help(helper.print_help)        

# print(hex(255))

# x = ('apple', 'banana', 'cherry')
# y = id(x)
# print(y)

# x = input('Enter the value of your name:')
# print('hello', x)


# print(int(4.6))

# print(isinstance(5, int))


# x = isinstance('Hello', (float, int, str, list, dict, tuple))
# print(x)


# class myObj:
#     name = 'John'
# y = myObj()
# x = isinstance(y, myObj)
# print(x)    


# class myAge:
#     age = 36

# class myObj(myAge):
#     name = 'John'
#     age = myAge
# x = issubclass(myObj, myAge) 
# print(x)       

# x = iter(['apple', 'banana', 'cherry'])
# print(next(x))
# print(next(x))
# print(next(x))

# x = object()
# print(dir(x))

# list1 = (('Apple', 'banana', 'Orange'))

# print(list(list1))

# x = locals()
# print(x)


# def myfunc(n):
# 	return len(n)

# x = map(myfunc, ('apple', 'banana', 'cherry'))

# print(x)
# print(list(x))


# x = memoryview(b"Hello")

# print(x)

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])

# x = pow(4, 6)
# print(x)

# alph = ["a", "b", "c", "d"]
# ralph = reversed(alph)
# for x in ralph:
# 	print(x)


# print(round(25.664568549, 3))
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2)
# print(a[x])

# a = (4, 5, 6, 9, 8, 7, 3, 71)
# print(sum(a))

# f = open("scholarship_form.txt", "r")
# print(f.read())

# class Parent:
#     def __init__(self, txt):
#         self.message = txt
#     def printmessage(self):
#         print(self.message)

# class Child(Parent):
#      def __init__(self, txt):
#           super().__init__(txt)

# x = Child("Hello, and wecome")

# x.printmessage()


# class Person:
#     name = "John"
#     age = 36
#     country = "norway"
    
# x = vars(Person)

# print(x)

# a = ("a", "b", "c")
# b = ("d", "e", "f")

# x =  zip(a, b)

# print(tuple(x))

# def doubleSiuff(aList):
# 	"""Overwrite each element in aList with double its value."""
# 	for position in range(len(aList)):
# 		aList[position] = 2 * aList[position]
# things = [2, 5, 9]
# print(things)
# doubleSiuff(things)
# print(things)

# def func(d):
    
# 		for key in d:
# 			print("key:", key, "Value:", d[key])

# D = {'a':1, 'b':2, 'c':3}
# func(D)	
# 

# def myfunc(a, b):
#     return a+b
# print(myfunc(4, 6))		


# # *args function
# def myFunc(*argv):
#     for arg in argv:
#         print(arg)

# myFunc('Hello', 'Asian', 'Publishers', 'Muzaffarnagar')        

# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result    
# print(my_sum(4, 5, 6, 8, 4)) 
# 
# kwargs function:
# 
# def myFun(**Kwargs):
#     for key, value in Kwargs.items():
#         print("%s == %s" %(key, value))
# myFun(first='Asian', mid='Publishers', last='Muzaffarnagar')
# 

# Scope Function :-
# def f():
#     print(s)
# s = 'Asian'               
# f()    
# f()    
# f()    
# f()                   

# not the global value
# def f():
#     print(s)
#     s = 'asian'
#     print(s)
# s = 'publishers'
# f()
# print(s) 
# 
# def f():
#     global s 
#     print(s)
#     s = 'Asian publishers'
#     print(s)
# s = 'Hello World'
# f()
# print(s)


# First class Function:-
# def shout(text):
#     return text.upper()
# print(shout('Hello'))
# yell = shout
# print(yell('Hello'))

# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()
# def greet(func):
#     greeting = func('Hi, I am created by a function passed as an argument.')
#     print(greeting)
# greet(shout)
# greet(whisper)    


# map function:-
# def addition(n):
#     return n+n
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# # filter function:-
# def fun(variables):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if(variables in letters):
#         return True
#     else:
#         return False
# Sequence = ['g', 'e', 'e', 'j', 'k', 's', 'u', 'u']
# filtered = filter(fun, Sequence)

# print('The fitere letters are:')
# for s in filtered:
#     print(s)
# 


# """
# Desc
# Python map() function to apply on a Dict iterable 
# """ 
# iter_Dict = {"Python":0, "CSharp":0, "java":0}
# print_Iter(iter_Dict)
# map_result = map(getLength, iter_Dict)
# print("Type of map_result is {}".format(type(map_result)))
# print("Lengths are: ")
# show_result(map_result)     

# lambda function:-
# def cube(y):
#     return y*y*y
# g = lambda x:x*x*x
# print(g(7))
# print(cube(5))

# Use of lambda with  filter()
# li = [5, 7, 22, 97, 54, 67, 77, 23, 73, 61]
# final_list=list(filter(lambda x:(x%2==0), li))
# print(final_list)              

# # use of lambda with map():=
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list=list(map(lambda x: x*2, li))
# print(final_list)                       

# use of lambda with reduce():=
# from functools import reduce

# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y:x+y), li)
# print(sum)


# Inner Function:-
# def outerFunction(text):
#     text = text
#     def innerFunction():
#         print(text)
#     innerFunction()

# if __name__ =='__main__':
#     outerFunction('Hey !')
          

# def outerFunction(text):
#     text = text

#     def innerFunction():
#         print(text)

#     innerFunction()
# 
# Scope of Variable in Nested Function
# def f1():
#     s = 'Asian Publishers'

#     def f2():
#         print(s)

#     f2()   
# 
# Closures:-
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)
    return innerFunction #Note we are returning function WITHOUT parenthsis

if __name__ == '__main__':
    myFunction = outerFunction('Hey !')
    myFunction()    

