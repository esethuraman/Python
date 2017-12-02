#!/bin/python3

import sys

def surfaceArea(A):
	
	total_surface_area = 0

	for i in range(len(A)):
		for j in range(len(A[0])):

			top, bottom, front, back, right, left = get_initial_values()

			if (i == 0):
				back = A[i][j]
			
			if  (i == (len(A)-1)):
				front = A[i][j]

			if (j == 0):
				left = A[i][j]

			if (j == (len(A[0])-1)):
				right = A[i][j] 

			# for a normal cell
			if (back == 0) and (A[i][j] > A[i-1][j]):
				back = (A[i][j] - A[i-1][j])

			if (front == 0) and (A[i][j] > A[i+1][j]):
				front = (A[i][j] - A[i+1][j])

			if (right == 0) and (A[i][j] > A[i][j+1]):
				right = (A[i][j] - A[i][j+1])

			if (left == 0) and (A[i][j] > A[i][j-1]):
				left = (A[i][j] - A[i][j-1])

			total_surface_area += (top + bottom + front + back + left + right)


	return total_surface_area

def get_initial_values():
	return (1,1,0,0,0,0)

if __name__ == "__main__":
	H, W = input().strip().split(' ')
	H, W = [int(H), int(W)]
	A = []
	for A_i in range(H):
	   A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
	   A.append(A_t)
	result = surfaceArea(A)
	print(result)
