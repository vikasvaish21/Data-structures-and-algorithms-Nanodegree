def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    front_index = 0
    last_index = len(input_list)-1
    mid_index = 0
    while mid_index <= last_index:
        if input_list[mid_index] == 0:
            input_list[front_index],input_list[mid_index] = input_list[mid_index],input_list[front_index]
            mid_index += 1
            front_index += 1
        elif input_list[mid_index] == 1:
            mid_index += 1
        else:
            input_list[mid_index],input_list[last_index] = input_list[last_index],input_list[mid_index]
            last_index -= 1

def test_function(test_case):
    sort_012(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

 # Edge cases
print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])
