
import sys,os
sys.path.append( os.path.abspath('..'))

from mterm import *
from minim import *
import unittest

class TestM(unittest.TestCase):

    def test_check_valid(self):
        self.assertEqual( m('xyz'),None )
        self.assertEqual( m('x1+x2-3'),None )

    def test_max_ind(self):
        self.assertEqual( max_ind('x1-x2+x3'),3 )
        self.assertEqual( max_ind('~x') , 0 )
          
    def test_modify(self):
        self.assertEqual( modify('x'),'x1' )
        self.assertEquals( modify('x1+~x*0'),'x1+~x1*0' )

    def test_dec2bin(self):
        self.assertListEqual( dec2bin(2,3),[0,1,0] )
        self.assertListEqual( dec2bin(3,4),[0,0,1,1] )
    def test_bin2dec(self):
        self.assertEqual( bin2dec([0,1,0]),2)
        self.assertEqual( bin2dec([0,0,1,1]),3 )
    def test_m(self):
        self.assertListEqual( m('x1'),[1] )
        self.assertListEqual( m('~x'),[0] )
        self.assertListEqual( m('~x1') ,[0] )
        self.assertListEqual( m('x1*x2+x1*~x2'),[2,3] )
        self.assertListEqual( m('x1*x2*x3'),[7] )
        self.assertListEqual( m('x1+x2'),[1,2,3] )
        self.assertListEqual( m('x1*x2*x3+x1*~x2*~x3'),[4,7] )
    
    def test_listin(self):
        self.assertTrue( listin([[0,1],[1,0]],[ [0,1],[1,0],[1,1] ]) )

       
    def test_form(self):
        self.assertEqual(
            
                get_form([ [1,0,1] ]),
                'x1*~x2*x3'

        )

        self.assertEqual(
                
                get_form([ [1,0,0],[1,0,1] ]),
                'x1*~x2'
                
                )
    
    def test_fnc(self):
        self.assertListEqual(
                fnc(
                    [ [0,0] ],
                    0,
                    [ [0,0],[1,1] ]
                ),
                [[0,0]]
        )

        self.assertListEqual(
                fnc(
                    [ [0,0,0] ],
                    0,
                    [ [0,0,0],[1,0,0],[0,1,0] ]

                    ),
                [ [0,0,0],[1,0,0] ]
    
        )
    
    def test_2(self):
         pass
       

if __name__=='__main__':
    unittest.main()

