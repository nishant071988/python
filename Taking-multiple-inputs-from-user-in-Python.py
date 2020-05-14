"""User can take multiple inputs in python using split() function or using list comprehension"""
'''split() method or function can help user to get multiple inputs from user.
It breaks the given input specified by the seperator. If the seperator is not provided
then with whitespaces. Generally it is used to split a Python string but one
can use it in taking multiple input'''
'''The syntax to it is: input().split(seperator, maxsplit)

# Python program showing how to 
# multiple input using split 
  
# taking two inputs at a time'''

x ,y = input("Enter any two values: ").split('-')
print("Number of boys: ",x)
print("Number of girls :",y)

'''O/P of the above program is Enter any two values: 2-5
Number of boys:  2
Number of girls : 5
Here the two values which we have entered is seperated by -, if the seperator is , then
we have to type two values seperated by comma like 2,5. If there is no seperator
then we have put a whitespace between two values that is a space'''
 # Taking there variables at a time
x,y,z= input("Enter 3 values: ").split()
print("Total number of values:  ")
print ("Value of x is: ",x)
print ("Value of y is: ",y)
print ("Value of z is: ",z)
print()

# Taking two inputs at a time
y,z = input("Enter two value: ").split('.')
print ("First number is {} and second number is {}".format(y,z))

#Taking multiple inputs at a time
#and type casting using list() function
x=list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ",x)
