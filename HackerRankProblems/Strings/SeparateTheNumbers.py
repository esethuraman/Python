#!/bin/python3

import sys


q = int(input().strip())


def is_beautiful_string(s):

    position = 0
    first_int_length = 1
    first_int = int(s[0: first_int_length])
    current_int = first_int
    flag = False
    # print(len(s))

    for i in range(0, len(s)-1):
        expected_next_int = current_int + 1
        next_window_length = (position + 1 + len(str (expected_next_int)))
        if next_window_length <= len(s):
            actual_next_int = int (s[position+1 : next_window_length])

        # print(current_int)
        # print(expected_next_int)
        # print(actual_next_int)
        # print("=====>")
        if expected_next_int == actual_next_int:
            current_int = actual_next_int
            # expected_next_int = current_int + 1
            position += len(str (expected_next_int))
            # print("position ", position)


        else:
           first_int_length += 1
           # reset the position to start from the begining
           first_int = int (s[0: first_int_length])
           current_int = first_int
           position = len(str (current_int))-1

           continue

        if position == len(s)-1:
            flag = True
            break

    if flag:
        print("YES ", first_int)
    else:
        print("NO")

for a0 in range(q):
    s = input().strip()
    # your code goes here
    is_beautiful_string(s)