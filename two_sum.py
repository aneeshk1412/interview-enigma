def two_sum(nums, target):
	d = dict((x, i) for (i, x) in enumerate(nums))
	for x, i in d.items():
		if target - x in d and d[target - x] != i:
			return [i, d[target - x]]

def main():
	L = [([2, 4, 7, 5, 3, 6], 10), ]
	for l, t in L:
		print(l, t, ':', two_sum(l, t))

if __name__ == '__main__':
	main()