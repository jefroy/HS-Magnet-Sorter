# runner script thingy
from models.MagnetHelper import MagnetHelper
sep = "-=" * 50

def test_mh():
    print("-=-=-=- Testing MagnetHelper! -=-=-=- ")
    mh = MagnetHelper()
    print("instantiated MagnetHelper!")
    print(sep)
    print("testing read_file()...")
    mh.read_file()
    print("read_file() -> len(links) = ", len(mh.links))


    # mh.process_links()


test_mh()
