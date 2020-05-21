# runner script thingy
from models.MagnetHelper import MagnetHelper
from models.Menu import Menu

mh = MagnetHelper()
menu = Menu()

menu.greet()
mh.read_file()
mh.reverse_links()

start, end = menu.get_range()

start = int(start)
end = int(end)

mh.filter_reversed_links(start, end)
mh.write_file()
menu.outro()
