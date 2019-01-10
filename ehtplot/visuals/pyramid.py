# Copyright (C) 2018--2019 Chi-kwan Chan
# Copyright (C) 2018--2019 Steward Observatory
#
# This file is part of ehtplot.
#
# ehtplot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ehtplot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ehtplot.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import

import numpy as np

try:
    basestring
except NameError:
    basestring = str # so that we can always test strings as in python2


def pyramid(N=513):
    """Create a pyramid function"""
    s    = np.linspace(-1.0, 1.0, N)
    x, y = np.meshgrid(s, s)
    return 1.0 - np.maximum(abs(x), abs(y))


def visualize_pyramid(ax, cmap):
    """Plot the pyramid image with the colormap `cmap`

    Args:
        ax (matplotlib.axes.Axes): The matplotlib Axes to be plot on.
        cmap (string or matplotlib.colors.Colormap): The colormap to
            be used in plotting the pyramid.

    """
    ax.imshow(pyramid(), cmap=cmap, vmin=0.0, vmax=1.0)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_title(cmap if isinstance(cmap, basestring) else cmap.name)
