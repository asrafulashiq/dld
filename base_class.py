from basic import *

class BVar():
    '''
    A class to define basic boolean variable
    '''
    def __init__(self,val = None):
        self.__v = val

    def set(self,val):
        self.__v = val

    def __eq__(self,other):
        if self.__v == other.__v:return True
        return False

    def __add__(self,other):
        if self.__v==1 or other.__v == 1:
            return BVar(1)
        if self.__v==None or other.__v==None:
            return BVar()
        return BVar(Or(self.__v,other.__v))

    def __mul__(self,other):
        if self.__v==0 or other.__v==0:
            return BVar(0)
        elif self.__v==None or other.__v==None:
            return BVar()
        return BVar(And(self.__v,other.__v))

    def __invert__(self):
        if self.__v != None:
            return BVar(Not(self.__v))
        return BVar()

    def __neg__(self):
        return ~self



