class grandpaa:
    feature="height"

class father(grandpaa):
    feature1="color"
    
class child(father):
    feature2="intelligent"
    
obj=grandpaa()
print(obj.feature)


obj1=father()
print(obj1.feature,obj1.feature1)

obj2=child()
print(obj2.feature,obj2.feature1,obj2.feature2)
