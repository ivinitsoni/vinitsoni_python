#Class is a keyword.
#keep first letter of class name is a capital

class Student:

    def getdata(self,fname,lname): #(self,fname,lname) is an argument
        print('getdata called')
        self.f=fname
        self.l=lname

    def putdata(self):
        print('putdata called')
        print('First Name : ',self.f)
        print('Last Name : ',self.l)

#s1 is object. object will occupy memory.
s1 = Student()
s1.getdata('Vinit','Soni')
s1.putdata()

s2=Student()
s2.getdata('Ajay','Patel')
s2.putdata()