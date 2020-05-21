import os


class Menu:

    def __init__(self):
        self.welcome_msg = "Hi good day."
        self.start = 0
        self.end = 0

    def greet(self):
        print(self.welcome_msg)
        print("Welcome to my smol script.\nINSTRUCTIONS:\n")
        print("0. Grab your links from https://anonembed.xyz/horriblesubs/")
        print("1. Place your magnet links inside: src/data/input/links.txt")
        print(
            "2. When prompted, enter:\n"
            "    a. the first number in your desired range (the min/start)\n"
            "    b. the second number in your desired range (the max/end)\n"
            "eg:\nStart: 3\nEnd: 8\nwhich means we want to get the links for episode 3 to 8 inclusive."
        )
        print('3. Fetch your results in the src/data/output/output.txt directory! :)\n\n')
        print("Proceed after you complete step 1 :)..")
        spunk = input("Press Enter to continue")

    def get_range(self):
        print(self.welcome_msg)
        self.start = input("Enter start: ")
        self.end = input("Enter end: ")
        return self.start, self.end

    def outro(self):
        print("Done!\nPlease check your output.txt!!")
