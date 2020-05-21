# runner script thingy
from models.MagnetHelper import MagnetHelper

sep = "-=" * 50
mh = MagnetHelper()


def test_read_file(x):
    print("testing read_file()...\n")
    x.read_file()
    print("read_file() -> len(links) = ", len(x.links))
    return True


def test_reverse_links(x):
    print("testing process_links()...\n")
    x.reverse_links()
    return True


def test_filter_reversed_links(x):
    print("testing filter_reversed_links()...\n")
    x.filter_reversed_links(3, 8)
    return True


def test_mh(x):
    """
    main function to test all the methods
    :param x: MagnetHelper instance
    :return: True if all passed, False otherwise
    """
    print("-=-=-=- Testing MagnetHelper! -=-=-=- ")
    print(sep)
    if test_read_file(x):
        print("read_file() passed!!")
    else:
        print("read_file() failed :(")

    print(sep)
    if test_reverse_links(x):
        print("reverse_links() passed!!")
    else:
        print("reverse_links() failed :(")

    print(sep)
    if test_filter_reversed_links(x):
        print("process_links() passed!!")
    else:
        print("process_links() failed :(")


test_mh(mh)
