# runner script thingy
from models.MagnetHelper import MagnetHelper

sep = "-=" * 50
mh = MagnetHelper()


def test_read_file(x):
    print("testing read_file()...\n")
    if x.read_file():
        print("read_file() -> len(links) = ", len(x.links))
        return True
    else:
        print("error: failed!")
        return False


def test_reverse_links(x):
    print("testing process_links()...\n")
    if x.reverse_links():
        print("passed!")
        return True
    else:
        print("failed!")
        return False


def test_filter_reversed_links(x):
    print("testing filter_reversed_links()...\n")
    if x.filter_reversed_links(64, 88):
        print("passed!")
        return True
    else:
        print("failed!")
        return False


def test_write_file(x):
    print("testing write_file()...\n")
    if x.write_file():
        print("passed!")
        return True
    else:
        print("failed!")
        return False


def test_mh(x):
    """
    main function to test all the methods
    :param x: MagnetHelper instance
    :return: True if all passed, False otherwise
    """
    print("-=-=-=- Testing MagnetHelper! -=-=-=- ")

    print(sep)
    if test_read_file(x):
        print("\033[0;36;47m passed!!  \033[0m")
    else:
        print("\033[0;31;47m failed! \033[0m")

    print(sep)
    if test_reverse_links(x):
        print("\033[0;36;47m passed!!  \033[0m")
    else:
        print("\033[0;31;47m failed! \033[0m")

    print(sep)
    if test_filter_reversed_links(x):
        print("\033[0;36;47m passed!!  \033[0m")
    else:
        print("\033[0;31;47m failed! \033[0m")

    print(sep)
    if test_write_file(x):
        print("\033[0;36;47m passed!!  \033[0m")
    else:
        print("\033[0;31;47m failed! \033[0m")


test_mh(mh)
