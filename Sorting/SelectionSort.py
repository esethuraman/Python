
def do_selection_sort(lst):
    for i in range(len(lst)):
        local_minimum = 99999
        index = i
        for j in range(i,len(lst)):
            if local_minimum > int (lst[j]):
                local_minimum = int (lst[j])
                index = j
        temp = lst[index]
        lst[index] = lst[i]
        lst[i] = temp

    print(lst)
if __name__ == "__main__":
    lst = input("Enter the elements\n").strip().split()

    do_selection_sort(lst)