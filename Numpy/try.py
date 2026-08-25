import numpy as np
import os

folder = os.path.dirname(os.path.abspath(__file__))

a = np.array([1, 2, 3])
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)

d = np.zeros((3, 4))
np.ones((2, 3, 4), dtype=np.int16)
d = np.arange(10, 25, 5)
np.linspace(0, 2, 9)
e = np.full((2, 2), 7)
f = np.eye(2)
np.random.random((2, 2))
np.empty((3, 2))

np.save(os.path.join(folder, 'm!!y_array'), a)
np.savez(os.path.join(folder, '!!array.npz'), a, b)
np.load(os.path.join(folder, '!!my_array.npy'))
np.savetxt(os.path.join(folder, '!!myarray.txt'), a, delimiter=" ")
