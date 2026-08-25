
from sortedcontainers import SortedDict

from sortedcontainers import SortedSet 
print(SortedSet({3, 1, 2}))
d = SortedDict({3: 'c', 1: 'a', 2: 'b'})
print(d)
d[0] = 'z'
print(d)
val = d.setdefault(4, 'd')
print(d)
print(val)
miss = d.get(5, 'default_value')
print(miss)
d.clear()
print(d)
