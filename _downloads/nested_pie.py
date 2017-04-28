"""
=================
Nested pie charts
=================

The following examples show two ways to build a nested pie chart
in Matplotlib.

The most straightforward way to build a pie chart is to use the
:func:`pie method <matplotlib.pyplot.pie>`:
"""

from matplotlib import pyplot as plt
import numpy as np

vals = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
fig, ax = plt.subplots()
ax.pie(vals.flatten(), radius=1.2,
       colors=plt.rcParams["axes.prop_cycle"].by_key()["color"][:vals.shape[1]])
ax.pie(vals.sum(axis=1), radius=1)
ax.set(aspect="equal", title='Pie plot with `ax.pie`')

plt.show()

###############################################################################
# However, you can accomplish the same output by using a bar plot on
# axes with a polar coordinate system. This may give more flexibility on
# the exact design of the plot.

fig, ax = plt.subplots(subplot_kw=dict(polar=True))

common_opts = {'linewidth': 2, 'edgecolor': 'w'}

inner = {
    'left': np.arange(0.0, 2 * np.pi, 2 * np.pi / 6),
    'width': 2 * np.pi / 6,
    'bottom': 0,
    'color': 'C0'
}
inner['height'] = np.zeros_like(inner['left']) + 5

middle = {
    'left': np.arange(0.0, 2 * np.pi, 2 * np.pi / 12),
    'width': 2 * np.pi / 12,
    'bottom': 5,
    'color': 'C1'
}
middle['height'] = np.zeros_like(middle['left']) + 2

outer = {
    'left': np.arange(0.0, 2 * np.pi, 2 * np.pi / 9),
    'width': 2 * np.pi / 9,
    'bottom': 7,
    'color': 'C2'
}
outer['height'] = np.zeros_like(outer['left']) + 3

ax.bar(**inner, **common_opts)
ax.bar(**middle, **common_opts)
ax.bar(**outer, **common_opts)

ax.set(title="Pie plot with `ax.bar` and polar coordinates")
ax.set_axis_off()
plt.show()
