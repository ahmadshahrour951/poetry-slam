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


def lines_printed_custom(lines_list, loops):
    """
    This function takes lines_list and loops as parameters.
    loops is an integer that will define the number of cycles the user want to perform.
    A cycle constitutes to printing the list in order then in reverse.

    Parameters:
    - lines_list: Array - an array of elements of a printable literal
    - loops: Integer - the number of cycles you want to perform

    Return:
    - None
    """
    # This will be used as the range iterator in the upcoming for loop, a simple multiplication helps.
    half_loops = loops * 2
    # is_reverse is flag to help direct the logic in upcoming for loop
    is_reverse = False

    for half_cycle in range(half_loops):
        # so I'm checking if the flag True, if it isnt print each element in the regular order
        if not is_reverse:
            print('CYCLE: ' + str((half_cycle/2 + 1)))
            print('====================')
            for line in range(len(lines_list)):
                print(lines_list[line])
            # this will change the flag, so that in the next iteration the logic is navigated to the else statement
            is_reverse = True
        else:
            print('====================')
            print('REVERSING!')
            print('====================')
            # range(len(lines_list) - 1, -1, -1) essentially means go backwards starting at the end of the list
            for reverse_line in range(len(lines_list) - 1, -1, -1):
                print(lines_list[reverse_line])
            print('====================')
            # this will change the flag, so that in the next iteration the logic is navigated to the first if statement
            is_reverse = False


# executing the code
file_lines = get_file_lines('./poem.txt')

# print(file_lines)
# lines_printed_backwards(file_lines)
# lines_printed_random(file_lines)
lines_printed_custom(file_lines, 3)
