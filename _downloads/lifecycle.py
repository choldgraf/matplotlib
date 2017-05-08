"""
=======================
The Lifecycle of a Plot
=======================

Going from start to finish of one plot in Matplotlib.

This tutorial aims to show the beginning, middle, and end of a single
visualization using Matplotlib. We'll begin with some raw data, and
end by saving a figure of a customized visualization. Along the way we'll try
to highlight some neat features and best-practices using Matplotlib.

.. currentmodule:: matplotlib

.. note::

    This tutorial is based off of
    `this excellent blog post <http://pbpython.com/effective-matplotlib.html>`_
    by Chris Moffitt. It was modified and put here by Chris Holdgraf.

A note on Object-oriented vs Pyplot
===================================

Matplotlib has two interfaces. The first is based on MATLAB and uses
a state-based interface. This is encapsulated in the :mod:`pyplot`
module. See the :ref:`pyplot tutorials <sphx_glr_tutorials_01_introductory_lifecycle.py>`
for a more in-depth look at the pyplot interface.

The second option is an an object-oriented (OO) interface.
In this case, we utilize an instance of :class:`axes.Axes` in order to
render visualizations on an instance of :class:`figure.Figure`.
We call methods that do the plotting directly from the
Axes object, which gives us much more flexibility and
power over customizing our plot. See the
:ref:`object-oriented examples <api_examples>` for many examples of how
this approach is used.

.. note::

    In general, try to use the object-oriented interface over the pyplot
    interface.

Our data
========

We'll generate some fake data that is broken down according to groups.
These data contain one number per group, perhaps representing the mean value
of each group.

"""

# sphinx_gallery_thumbnail_number = 10
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from string import ascii_lowercase

n_groups = 10
group_data = np.random.randint(0, 100, n_groups)
group_names = ['group_%s' % ii for ii in ascii_lowercase[:n_groups]]

###############################################################################
# Getting started
# ===============
#
# This data is naturally visualized as a barplot, with one bar per
# group. To do this with the object-oriented approach, we'll first generate
# an instance of :class:`figure.Figure` and
# :class:`axes.Axes`. The Figure is like a canvas, and the Axes
# is a part of that canvas on which we will make a particular visualization.
#
# .. note::
#
#    Figures can have multiple axes on them. For information on how to do this,
#    see the :ref:`Tight Layout tutorial <sphx_glr_tutorials_02_intermediate_tight_layout_guide.py>`.

fig, ax = plt.subplots()

###############################################################################
# Now that we have an Axes instance, we can plot on top of it.

fig, ax = plt.subplots()
ax.bar(group_names, group_data)

###############################################################################
# Controlling the style
# =====================
#
# There are many styles available in Matplotlib in order to let you tailor
# your visualization to your needs. To see a list of styles, we can use
# :mod:`pyplot.style`.

print(plt.style.available)

###############################################################################
# You can activate a style with the following:

plt.style.use('fivethirtyeight')

###############################################################################
# Now let's remake the above plot to see how it looks:

fig, ax = plt.subplots()
ax.bar(group_names, group_data)

###############################################################################
# The style controls many things, such as color, linewidths, backgrounds,
# etc.
#
# Customizing the plot
# ====================
#
# Now we've got a plot with the general look that we want, so let's fine-tune
# it so that it's ready for print. First let's rotate the labels on the x-axis
# so that they show up more clearly. We can gain access to these labels
# with the :meth:`axes.Axes.get_xticklabels` method:

fig, ax = plt.subplots()
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()

###############################################################################
# If we'd like to set the property of many items at once, it's useful to use
# the :func:`pyplot.setp` function. This will take a list (or many lists) of
# matplotlib objects, and attempt to set some style element of each one.

fig, ax = plt.subplots()
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

###############################################################################
# It looks like this cut off some of the labels on the bottom. We can
# tell matplotlib to automatically make room for elements in the figures
# that we create. To do this we'll set the ``autolayout`` value of our
# rcParams. For more information on controlling the style, layout, and
# other features of plots with rcParams, see
# :ref:`sphx_glr_tutorials_01_introductory_customizing.py`.

plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots()
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

###############################################################################
# Next, we'll add labels to the plot. To
# do this with the OO interface, we can use the :meth:`axes.Axes.set` method
# to set properties of this axis object.

fig, ax = plt.subplots()
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(ylim=[0, 105], xlabel='Group ID', ylabel='Count',
       title='Group ID and Count.')

###############################################################################
# We can also adjust the size of this plot using the :func:`pyplot.subplots`
# function. We can do this with the ``figsize`` kwarg.
#
# .. note::
#
#    While indexing in python follows the form (row, column), the figsize
#    kwarg follows the form (width, height). This follows conventions in
#    visualization, which unfortunately are different from those of linear
#    algebra.

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(ylim=[0, 105], xlabel='Group ID', ylabel='Count',
       title='Group ID and Count.')

###############################################################################
# For labels, we can specify custom formatting guidelines in the form of
# functions by using the :class:`ticker.FuncFormatter` class. Below we'll
# define a function that takes an integer as input, and returns a string
# as an output.


def make_labels(num, pos):
    """The two args are the value and tick position."""
    if num < 25:
        s = 'super tiny'
    elif num >= 25 and num < 50:
        s = 'medium-ish'
    elif num >= 50 and num < 75:
        s = 'pretty big'
    elif num > 75:
        s = 'super big!'
    else:
        s = 'I dunno!'
    return s

formatter = FuncFormatter(make_labels)

###############################################################################
# We can then apply this formatter to the labels on our plot. To do this,
# we'll use the ``xaxis`` attribute of our axis. This lets you perform
# actions on a specific axis on our plot.

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

ax.set(ylim=[0, 105], xlabel='Group ID', ylabel='Count',
       title='Group ID and Count.')
ax.yaxis.set_major_formatter(formatter)

###############################################################################
# Combining multiple visualizations
# =================================
#
# It is possible to draw multiple visualizations on the same instance of
# :class:`axes.Axes`. To do this we simply need to call another one of
# the plot methods on that axes object.

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axhline(80, ls='--', color='r')
# Annotate the best groups
for group in ['group_a', 'group_d', 'group_f']:
    ax.text(group, 110, "Awesome\nGroup", fontsize=10,
            horizontalalignment='center')
# Now we'll move our title up since it's getting a little cramped
ax.title.set(y=1.2)

ax.set(ylim=[0, 105], xlabel='Group ID', ylabel='Count',
       title='Group ID and Count.')
ax.yaxis.set_major_formatter(formatter)
plt.show()


###############################################################################
# Saving our plot
# ===============
#
# Now that we're happy with the outcome of our plot, we want to save it to
# disk. There are many file formats we can save to in Matplotlib. To see
# a list of available options, use:

print(fig.canvas.get_supported_filetypes())

###############################################################################
# We can then use the :meth:`figure.Figure.savefig` in order to save the figure
# to disk. Note that there are several useful flags we'll show below:
#
# * ``transparent=True`` makes the background of the saved figure transparent.
# * ``dpi=80`` controls the resolution (dots per square inch) of the ouput.
# * ``bbox_inches="tight"`` fits the bounds of the figure to our plot.

# Uncomment this line to save the figure.
# fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")

###############################################################################
# There are many other things you can do with Matplotlib, and this is just
# a taste. For more information, check out our :ref:`tutorials` and
# :ref:`examples-index` pages.
