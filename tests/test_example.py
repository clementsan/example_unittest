#/usr/bin/env python3

import os
import unittest
import example.example as e
import example_package_clem.example as e_clem

class TestExample(unittest.TestCase):

	def test_add_one(self):
		assert e_clem.add_one(2) == 3

	def test_add(self):
		assert e.add(2, 3) == 5
		assert e.add("space", "ship") == "spaceship"

	def test_substract(self):
		assert e.substract(3,2) == 1

	def test_multiply(self):
		assert e.multiply(2, 3) == 6

	def test_inputpath(self):
		if 'TESTINPUTPATH' in os.environ:
			TestInputDir = os.environ["TESTINPUTPATH"]
			print('TestInputDir:', TestInputDir)
			self.assertTrue(os.path.exists(TestInputDir),
							"Test input directory specified by TESTINPUTPATH environment variable does not exist")
			return TestInputDir
		else:
			self.fail("TESTINPUTPATH environment variable should specfify input data directory")


if __name__ == '__main__':
	unittest.main()