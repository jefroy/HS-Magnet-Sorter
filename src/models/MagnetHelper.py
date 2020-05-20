"""
Helper class to process data.
"""


class MagnetHelper:
    def __init__(self):
        self.fin_name = 'links.txt'
        self.in_dir = 'src/data/input/'

        self.outf_name = 'output.txt'
        self.out_dir = 'src/data/output/'

        self.links = []
        self.processed_links = []

    def read_file(self):
        """
        read the input file
        input file should contain magnet links
        :return: array of magnet links (strings)
        """
        data_path = self.in_dir + self.fin_name
        f = open(data_path, 'r')
        self.links = f.readlines()
        f.close()

    def process_array(self, arr):
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

    def filter_processed_array(self, arr, num1, num2):
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

    def write_file(self, arr):
        f = open(self.out_dir + self.outf_name, 'w')
        f.writelines(arr)
        f.close()

    # utility
    def print_links(self):
        for link in self.links:
            print('-> ', link)
