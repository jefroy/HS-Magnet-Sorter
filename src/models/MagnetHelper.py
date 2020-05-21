"""
Helper class to process data.
"""
import os


class MagnetHelper:
    def __init__(self):
        self.fin_name = 'links.txt'
        self.in_dir = 'src/data/input/'

        self.outf_name = 'output.txt'
        self.out_dir = 'src/data/output/'

        self.links = []
        self.reversed_links = []
        self.processed_links = []

    def read_file(self):
        """
        read the input file
        input file should contain magnet links
        :return: array of magnet links (strings)
        """
        data_path = self.in_dir + self.fin_name
        # check for empty file
        if os.stat(data_path).st_size == 0:
            print("error: file empty or not found :(")
        else:
            print("file found and not empty!!")

        f = open(data_path, 'r')
        self.links = f.readlines()
        f.close()

    def reverse_links(self):
        """
        add \n at the end of each entry,
        populate a new array with the correct ordering
        :return: bool
        """
        size = len(self.links)
        if size <= 0:
            print("array is empty! run read_file() first!")
            return
        new_arr = []
        for link in reversed(self.links):
            new_arr.append(link)
        self.reversed_links = new_arr
        if len(self.reversed_links) == len(self.links):
            print('new array worked!')
            return True
        else:
            print('new array did not work :(')
            return False

    def filter_reversed_links(self, num1, num2):
        """
        filter the array based on range from num1 to num 2
        eg:
            - i want to download from ep 3 to 8, num1 = 3, num2 = 8,
            - the array will take num1 to be 2, and num2 to be 8 since
            array splicing goes from 0 to size inclusive (-1 to the start)
        :param num1: start
        :param num2: end
        store the result in self.processed_links
        """
        arr = self.reversed_links
        start = num1 - 1
        end = num2
        pred_size = end - start
        self.processed_links = arr[start:end]
        # print(len(self.processed_links))
        if len(self.processed_links) == pred_size:
            print("list filtered!")
            return True
        else:
            print("error: list not filtered!")
            return False

    def write_file(self, arr):
        f = open(self.out_dir + self.outf_name, 'w')
        f.writelines(arr)
        f.close()

    # utility
    def print_links(self):
        for link in self.links:
            print('-> ', link)
