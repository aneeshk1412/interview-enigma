#! /usr/bin/python3

def flatten(L : list):
	for x in L:
		''' Ask for forgiveness rather than permission '''
		try:
			yield from flatten(x)
		except TypeError:
			yield x

print(list(flatten([[1, 2, 3, [4, 5], 6, [7, 8]], [9, [10, 11], 12, [13]]])))
