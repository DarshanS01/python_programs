#variables
a=10       #this is integer variable
b="darsh"  #this is string variable
c=2.04     #this is floating point variable


#datatypes
a=15
print(type(a)) #this is integer datatype

b=3.14
print(type(b)) #this is floating point datatype

c="string"
print(type(c)) #this is string datatype

d=True
print(type(d)) #this is boolean datatype

f=None
print(type(f)) #this is None datatype


#operators in python

#i.arithmetic operator
a=10
b=2
print("addition of two num is:",a+b)
print("subtraction of two num is:",a-b)
print("multiplication of two num is:",a*b)
print("division of two num is:",a/b)

#ii.assignment operator
a=8   #value 8 is assigning to variable a
a+=5  # 5 is added to 8 and result is asign to a
a-=5  # 8 is subtracted by 5 and result is asign to a
a*=5  # 8 is multiple by 5 and result is asign to a
a/=2  # 8 is divided by 2 and result is asign to a

#iii.comparision operator
a=10<5
print(a) #it give boolean value Flase
b=10>5
print(b) #it give boolean value True
c=10==5
print(c) #it give boolean value Flase
d=10!=5
print(d) #it give boolean value True

#iv.logical operators

#Truth table of and operator
print("True and False is:",True and False)
print("False and False is:",True and False)
print("True and True is:",True and False)
print("False and False is:",True and False)

#Truth table of or operator
print("True or False is:",True or False)
print("False or False is:",True or False)
print("True or True is:",True or False)
print("False or False is:",True or False)

#tTruth table of not operator
print(not(False))
print(not(True))


#v.type() functions

r=12
t=type(r) #class int
print(t)

q=12.07
e=type(q)  #class float
print(e)

d="darshan"
s=type(d) #class string
print(s)

a="68.9"
v=float(a)  #converting string to float
y=type(a)
print(y)