def longest_substring_without_repeating_characters(word):
	''' Basic Idea: 
		For every index i, we will find the size of largest word without 
		repeating characters that ends at i.
		To do this, we track the index f_i, which is the smallest index less 
		than or equal to i such that s[f_i : i] does not have a repeating character.
		Observe, f_{i+1} = max(f_i, index of prev occurance of s[i+1])
		Either f_i is still the smallest valid index, or character s[i+1] occured 
		somewhere between f_i and i+1. This index is f_{i+1} and we find it from 
		a prev_occurence dictionary.
	'''
	max_start, max_len, f_i = 0, 0, 0
	prev_occurence = {}
	
	for i, x in enumerate(word):
		if x in prev_occurence:
			f_i = max(f_i, prev_occurence[x] + 1)

		if max_len < i - f_i + 1:
			max_len = i - f_i + 1
			max_start = f_i

		prev_occurence[x] = i

	return word[max_start: max_start + max_len]

def main():
	L = ["pwwkper"]
	for w in L:
		print(w, longest_substring_without_repeating_characters(w))

if __name__ == '__main__':
	main()