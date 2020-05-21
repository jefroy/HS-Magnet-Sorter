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
        if self.check_file(data_path):
            f = open(data_path, 'r')
            self.links = f.readlines()
            f.close()
            return True
        else:
            return False

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

    def write_file(self):
        if len(self.processed_links) <= 0:
            print("cant write file! array empty!!")
            return False
        data_path = self.out_dir + self.outf_name
        f = open(data_path, 'w')
        f.writelines(self.processed_links)
        f.close()
        if self.check_file(data_path):
            print("output.txt generated!!")
            return True
        else:
            print("error while generating output.txt")
            return False

    # utility
    @staticmethod
    def check_file(path):
        # check for empty file
        if os.stat(path).st_size == 0:
            print("error: file empty or not found :(")
            return False
        else:
            print("file found and not empty!!")
            return True

    def print_links(self):
        for link in self.links:
            print('-> ', link)
