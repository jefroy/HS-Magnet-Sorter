def test():
    print('magnet_helper.py says hi :)')


def read_file(fname, dir_path):
    """
    read the input file
    input file should contain magnet links
    :return: array of magnet links (strings)
    """
    data_path = dir_path + '/' + fname
    f = open(data_path, 'r')
    lines = f.readlines()
    f.close()
    return lines


def process_array(arr):
    """
    add \n at the end of each entry,
    populate a new array with the correct ordering
    :return: new array
    """
    new_arr = []
    size = len(arr) - 1
    count = 0
    while size != 0:
        new_arr[count] = arr[size]
        count += 1
        size -= 1
    return new_arr


def filter_processed_array(arr, num1, num2):
    """
    filter the array based on range from num1 to num 2
    eg: i want to download from ep 3 to 8, num1 = 3, num2 = 8
    :param arr: filtered array of links in correct order
    :param num1: start
    :param num2: end
    :return: array of filtered links between start and end (inclusive)
    """
    start = num1 - 1
    end = num2
    new_arr = arr[start:end]
    return new_arr


def write_file(arr):
    fname = 'output.txt'
    data_dir = os.path.abspath(folder_name + fname)
    f = open(data_dir, 'w')
    f.writelines(arr)
    f.close()
