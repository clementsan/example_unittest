#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import example.example as e
import example_package_clem.example as e_clem 

def main():
	var_add = e.add(2,3)
	print('var_add: ', var_add)

	var_sub = e.substract(3,2)
	print('var_sub: ', var_sub)

	var_addone = e_clem.add_one(2)
	print('var_add: ', var_add)


if __name__ == "__main__":
	main()
