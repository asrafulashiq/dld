'''
simple unittest
'''
import unittest

import sys,os
sys.path.append( os.path.abspath('..'))
from basic import *
from base_class import BVar


class BaseTest(unittest.TestCase):

    def test_and(self):
        self.assertEqual( And(0,0),0 )
        self.assertEqual( And(0,1),0 )
        self.assertEqual( And(1,0),0 )
        self.assertEqual( And(1,1),1 )

    def test_and(self):
        self.assertEqual( Or(1,1),1 )
        self.assertEqual( Or(1,0),1 )
        self.assertEqual( Or(0,1),1 )
        self.assertEqual( Or(0,0),0 )
    def test_and(self):
        self.assertEqual( Not(0),1 )
        self.assertEqual( Not(1),0 )

class BVarTest(unittest.TestCase):
    def setUp(self):
        self.x1 = BVar(1)
        self.x2 = BVar(1)

    def test_Var_Eq(self):
        self.assertEqual(self.x1,self.x2)
        self.assertEqual(BVar(0),BVar(0))
        self.assertNotEqual(BVar(0),BVar())
    
    def test_Var_Or(self):
        self.assertEqual(self.x1+self.x2,BVar(1))
        self.assertEqual(BVar(1)+BVar(),BVar(1))
        self.assertEqual(BVar(0)+BVar(0),BVar(0))
        self.assertEqual(BVar(),BVar(),BVar())

    def test_Var_And(self):
        self.assertEqual(BVar()*BVar(0),BVar(0))
        self.assertEqual(BVar(1)*BVar(1),BVar(1))
    
    def test_Var_Not(self):
        self.assertEqual(~BVar(1),BVar(0))
        self.assertEqual(-BVar(0),BVar(1))
        self.assertEqual(~BVar(0),BVar(1))

    def test_And_Or_Not(self):
        x1 = BVar(1)
        x2 = BVar(1)
        x3 = BVar(0)

        self.assertEqual(x1+x2*x3,x1)
        self.assertEqual(~x3*x2,x2)
        self.assertEqual((x1+x2)*~x3,BVar(1))
        

def main():
    unittest.main()

if __name__=='__main__':
    main()
