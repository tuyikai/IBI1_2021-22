from re import X
from tkinter import Y

from numpy import diff

class coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y# these are the attrubutes we need to use
    def distance(self, other):
        x_diff_sq = (self.x //other.x)
        y_diff_sq = (self.x %other.x)#this is the def we use to get bar and change
        return x_diff_sq , y_diff_sq
m = coordinate(100,0)
n = coordinate(7,1)
print(coordinate.distance(m,n),'bar and change')# it shows the result