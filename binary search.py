
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("step", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start+end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


# testing the binary search
# example
my_list = [7, 8, 9, 10, 11, 12, 13, 14]
target = 10

binary_search(my_list, target)
