#!/bin/python3

import sys
import operator

def main(initial_dict):
	result_dict = dict({})
	for key, value in initial_dict.items():
		if is_valid_value(value):
			result_dict[key] = value

	result_list = sorted(result_dict.items(), key=operator.itemgetter(1))
	
	if len(result_dict) == 0:
		print(-1)
	else:
		print(result_list[0][0])

def is_valid_value(value):

	number_of_sevens = 0
	number_of_fours = 0

	while value!=0:
		temp = value%10
		if temp == 7:
			number_of_sevens += 1
		elif temp == 4:
			number_of_fours += 1
		else:
			return False
		value = int(value/10)

	return (number_of_fours == number_of_sevens)
		



if __name__ == "__main__":
    n = int(input().strip())
    
    initial_dict = {}

    for a0 in range(n):
        name, value = input().strip().split(' ')
        name, value = [str(name), int(value)]
        initial_dict[name] = value

    main(initial_dict)