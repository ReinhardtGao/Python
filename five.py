import zoo as menagerie

menagerie.hours()

from zoo import hours

hours()

from zoo import hours as info

info()
##################################
plain = {'a':1, 'b':2, 'c':3}
print(plain.items())
from collections import OrderedDict
fancy = OrderedDict([('a',1),('b',2),('c',3)])
print(fancy.items())
###################################
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('Something for a')
print(dict_of_lists['a'])
