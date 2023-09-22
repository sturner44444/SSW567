# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(13,12,5),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(1,3,4),'Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(9,6,3),'Scalene')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(1,1,2),'Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3,2,2),'Isosceles')

    def testValidTriangleA(self):
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle')

    def testValidTriangleB(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral')

    def testValidTriangleC(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')

    def testValidTriangleD(self):
        self.assertEqual(classifyTriangle(0,-1,1),'InvalidInput')

    def testValidTriangleE(self):
        self.assertEqual(classifyTriangle(1.5,2.5,3.5),'InvalidInput')
        
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

