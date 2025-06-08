#we can write string in three ways

a='in single quote'
b="in double quote"
c='''in triple quote'''

#string slicing
d="college"
d_len=len(d)
print(d_len)  #return the lenght of the string


#string functions

e="window"
e_short=e[0:4]  #start from index 0 all but exclude 4 index
print(e_short)

print(e.endswith("dow"))
print(e.capitalize())
print(e.startswith("Wind"))
print(e.title())

#escape sequence
a="hello \n world" 
b="hello \t world"
c=("you are a \" good \" guys" )
print (a)
print(b)
print(c)


 