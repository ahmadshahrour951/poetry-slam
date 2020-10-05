# we import randint at the top so that we may generate a random interger in our logic later in our code
from random import randint


def get_file_lines(filename):
    """
    This function reads the filename string parameter provided returns an array. Each element in the array is a line read from the filename.

    Parameters:
    - filename: String - path to file to read

    Return:
    - An array of each line of filename parameeter
    """
    # open, read, and splitlines methods are chained and invoked to return a clean array of filename lines.
    return open(filename).read().splitlines()

# This is a test to check if the function performs correctly with the solved example given in the assignment description
# print(get_file_lines('./poem.txt'))


def lines_printed_backwards(lines_list):
    """
    This function takes lines_list as a parameter, then prints each elements of the list in reverse order

    Parameters:
    - lines_list: Array - an array of elements of a printable literal

    Return:
    - None (this function only has logic to print)
    """
    lines_list_len = len(lines_list)

    while lines_list_len > 0:
        print(str(lines_list_len) + ' ' + lines_list[lines_list_len - 1])
        lines_list_len -= 1


# lines_printed_backwards(get_file_lines('./poem.txt'))

def lines_printed_random(lines_list):
    """
    This function takes lines_list as a parameter, then prints elements of the list in random.
    This is where we make use of randint import we did in the begininning

    Parameters:
    - lines_list: Array - an array of elements of a printable literal

    Return:
    - None (this function only has logic to print)
    """
    lines_list_len = len(lines_list)

    for list_ind in range(lines_list_len):
        print(lines_list[randint(0, lines_list_len - 1)])


# lines_printed_random(get_file_lines('./poem.txt'))
