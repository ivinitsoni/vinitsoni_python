class Point:

    def __init__(self,x,y): #double underscore wala badha functions magic functions 6.. magic functions automatic call thay 6..
        #object banaisu tyare aa __init__ function automatic call thai jse...
        print('init called')
        self.x=x
        self.y=y
        print('X :',self.x,'Y :',self.y)

    def __str__(self):
        #object print krisu tyare aa __str__ function automatic call thai jse...
        #without return str function call j nai thay
        print('str called')
        return "({0},{1})".format(self.x,self.y) #() ni jagya e [] pan use kri skie.. {} compulsory use krvu pdse.. 0 self.x and 1 self.y ne allot thase..
        
    def __add__(self,obj):
        #add function jyare 2 object add thase tyare call thase
        print('add called')
        x = self.x + obj.x
        y = self.y + obj.y
        return Point(x,y)

p1=Point(1,2)
p2=Point(3,4)
print(p1)
print(p1)
print('Addition : ',p1+p2)