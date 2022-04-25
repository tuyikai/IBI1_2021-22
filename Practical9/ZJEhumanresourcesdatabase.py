from re import X

class staff(object):# define attributes here 
    def  __init__(self,a,b,c):#we have 3 attrubutes here about the name , location and role
        self.a = a
        self.b = b
        self.c = c# we distribute the attributes
        

x = staff('Robert James','International	Campus','leadership')# this is the data we need
print(x.a,x.b,x.c)   

        