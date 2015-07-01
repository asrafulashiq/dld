
import sys,os
sys.path.append( os.path.abspath('..'))

from mterm import *
import unittest

class TestM(unittest.TestCase):
    def test_1(self):
        self.assertListEqual( m('x1'),[1] )
        self.assertListEqual( m('~x'),[0] )
        self.assertListEqual( m('~x1') ,[1] )

    def test_2(self):
         pass
       

if __name__=='__main__':
    unittest.main()

