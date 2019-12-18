#!/usr/bin/env python

# -*- coding: utf-8 -*-

import unittest

from app import process_input

 

class TestApp(unittest.TestCase):

   """Test the mathematical operations app"""

   def setUp(self):

       "This runs before the test cases are executed"

       self.a = 10

       self.b = 5

   def test_0010_add(self):

       "Test add operation"

       result = process_input(self.a, self.b, "add")

       self.assertEqual(result, 15)

def test_0020_subtract(self):

       "Test subtract operation"

       result = process_input(self.a, self.b, "subtract")

       self.assertEqual(result, 5)

def test_0030_multiply(self):

       "Test multiple operation"

       result = process_input(self.a, self.b, "multiple")

       self.assertEqual(result, 50)

def suite():

   "Test suite"

   suite = unittest.TestSuite()

   suite.addTests(

       unittest.TestLoader().loadTestsFromTestCase(TestApp)

   )

   return suite

 

if __name__ == '__main__':

   unittest.TextTestRunner(verbosity=2).run(suite())
