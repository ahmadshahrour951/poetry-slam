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
