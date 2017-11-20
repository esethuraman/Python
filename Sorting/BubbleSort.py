
def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(len(elements)-1):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
            # print(elements)

    return elements
if __name__ == "__main__":
    elements = input("Enter the numbers to be sorted\n").strip().split()
    print(bubble_sort(elements))