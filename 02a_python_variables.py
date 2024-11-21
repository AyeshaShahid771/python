# variable names can contain letters, num, underscores avoid keywords donot start with numbers and donot give space but you can use underscore ,variable name should be short but descriptive
# Typing python
# data types string str ,integer int,float float,boolean bool
# python is a dynamically typed language means you don't have to declare the data type of a variable ,static typed language means you have to declare the data type of a variable as in other langauges like c++,java



####### Rules for naming variables in python ###########

# 1. Variable names can contain letters, numbers, and underscores.
# 2. Variable names cannot start with a number.
# 3. Variable names cannot contain spaces.
# 4. Variable names should be short but descriptive.
# 5. Variable names should avoid using Python keywords.
# 6. Variable names should be in lowercase.
# 7. Variable names should not start with an underscore,number,.

name : str # declaration
name = "Ayesha shahid    " # initialization
print (name)
# for multiline string use triple quotes
name = """ Ayesha
       Shahid"""
age :int =18
height : float =5.7
status : bool = True
print("My name is",name,",my age is ",age,"and my height is",height,"martial status",status )
print("ayesha's advice")
print(name.title())  # title case
print(name.upper())  # upper case
# formatted string
print(f'I am {age} years old')
# new line
print("Hello\nworld")
# right strip ignore spaces from right
print("my name is ",name.rstrip(),".")
 # To write constant use all caps
PI = 3.14



#### static binding and dynamic binding
# static binding mean you cannot change the datatype of a variable once it is declared
# int a =10
# a = "hello"  # this will give an error
# dynamic binding means you can change the datatype of a variable once it is declared
# a = 10
# a = "hello"  # this will not give an error in python because python is dynamically typed language
#  