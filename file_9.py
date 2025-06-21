# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()
d="hello bye"
with open("file.txt","w")as f:
    f.write(d)
    
    
with open("file.txt")as f:
    f.read()