import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# import _mysql_connector as conn
from scipy.stats import norm
from scipy.integrate import quad
ϕ=norm() 
value,error=quad(ϕ.pdf,-2,2)
print(value) 
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
a = np.linspace(-np.pi, np.pi, 100)    # Create even grid from -π to π
b = np.cos(a)                          # Apply cosine to each element of a
c = np.sin(a) 
print(b@c)

print("Hello")
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']
np.random.seed(0)
grid = np.random.rand(4, 4)

fig, axes = plt.subplots(3, 6, figsize=(12, 6),
                         subplot_kw={'xticks': [], 'yticks': []})

fig.subplots_adjust(hspace=0.3, wspace=0.05)
for ax, interp_method in zip(axes.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(interp_method)

plt.show()

