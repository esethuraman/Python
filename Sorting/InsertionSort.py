
def do_insertion_sort(elements):
    # since the 1st subarray containing only one element is considered to be sorted
    for i in range(1,len(elements)):
        if (elements[i] < elements[i-1]):
            # an unsorted element has been found
            # in such a case, this element has to be rightly INSERTED in the left subarray
            for j in range(i,0,-1):
                # while traversing the left subarray, swap any unordered elements because of
                #  this new insesrtion
                if elements[j] < elements[j-1]:
                    temp = elements[j-1]
                    elements[j-1] = elements[j]
                    elements[j] = temp
    print(elements)

if __name__ == "__main__":
    elements = input("Enter the elements \n").strip().split()
    do_insertion_sort(elements)