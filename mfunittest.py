#!/usr/local/bin/python3.7

import unittest
from Mathmatic_Functions import Mathmatic_Functions

class TestMathmatic_Functions(unittest.TestCase):

	# Returns True or False
	def test_even(self):
		mf = Mathmatic_Functions()
		self.assertTrue(mf.is_even(2))
	
if __name__ == '__main__':
	unittest.main()
