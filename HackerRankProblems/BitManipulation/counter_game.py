
def main():
	t = int (input())
	initial_counters_lst = []

	for i in range (0,t):
		initial_counters_lst.append(int (input()))

	for i in range (0, t):
		n = initial_counters_lst[i]
		louise_turn = True
		# print("n value is ", n)
		while(True):
			n = get_next_turn_value(n)
			if(n==1):
				break
			louise_turn = not (louise_turn)

		if(louise_turn):
			print("Louise")
		else:
			print("Richard")
			
			

def get_next_turn_value(n):
	if n == 1:
		return n
	else:
		# getting the binary value of string, which is of the form "0b..."
		binary_string = str (bin(n))
		# the first two characters are chopped for string comparison
		truncated_string = binary_string[2:]

		# the nearest square of 2 should be of the form : 1 followed by m zeros
		# where x is length of truncated string minus 1
		comparison_string = "1"+"0"*(len(truncated_string)-1)
		
		if (comparison_string == truncated_string):
			n = n - n/2
		else:
			n = n - int(comparison_string, 2)
		return int(n)

if __name__ == "__main__":
	main()