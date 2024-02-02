#/usr/bin/env python3


import unittest
import example.example as e


class TestExample(unittest.TestCase):

	def test_add(self):

		assert e.add(2, 3) == 5
		assert e.add("space", "ship") == "spaceship"

	def test_substract(self):
		assert e.substract(3,2) == 1

	def test_multiply(self):
		assert e.multiply(2, 3) == 6


if __name__ == '__main__':
	unittest.main()