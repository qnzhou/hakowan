""" Accent color map.

This file contains colormaps proposed by ColorBrewer (v1.0) project.

Source: https://colorbrewer2.org/
"""
import numpy as np
from .colormap import ColorMap
from ..color import Color

accent = ColorMap(
    np.array(
        [
            [127, 201, 127],
            [190, 174, 212],
            [253, 192, 134],
            [255, 255, 153],
            [56, 108, 176],
            [240, 2, 127],
            [191, 91, 23],
            [102, 102, 102],
        ]
    )
    / 255.0
)

dark2 = ColorMap(
    np.array(
        [
            [27, 158, 119],
            [217, 95, 2],
            [117, 112, 179],
            [231, 41, 138],
            [102, 166, 30],
            [230, 171, 2],
            [166, 118, 29],
            [102, 102, 102],
        ]
    )
    / 255.0
)

paired = ColroMap(
    np.array(
        [
            [166, 206, 227],
            [31, 120, 180],
            [178, 223, 138],
            [51, 160, 44],
            [251, 154, 153],
            [227, 26, 28],
            [253, 191, 111],
            [255, 127, 0],
        ]
    )
    / 255.0
)

pastel1 = ColorMap(
    np.array(
        [
            [251, 180, 174],
            [179, 205, 227],
            [204, 235, 197],
            [222, 203, 228],
            [254, 217, 166],
            [255, 255, 204],
            [229, 216, 189],
            [253, 218, 236],
        ]
    )
    / 255.0
)

pastel2 = ColorMap(
    np.array(
        [
            [179, 226, 205],
            [253, 205, 172],
            [203, 213, 232],
            [244, 202, 228],
            [230, 245, 201],
            [255, 242, 174],
            [241, 226, 204],
            [204, 204, 204],
        ]
    )
    / 255.0
)

set1 = ColorMap(
    np.array(
        [
            [228, 26, 28],
            [55, 126, 184],
            [77, 175, 74],
            [152, 78, 163],
            [255, 127, 0],
            [255, 255, 51],
            [166, 86, 40],
            [247, 129, 191],
        ]
    )
    / 255.0
)

set2 = ColorMap(
    np.array(
        [
            [102, 194, 165],
            [252, 141, 98],
            [141, 160, 203],
            [231, 138, 195],
            [166, 216, 84],
            [255, 217, 47],
            [229, 196, 148],
            [179, 179, 179],
        ]
    )
    / 255.0
)

set3 = ColorMap(
    np.array(
        [
            [141, 211, 199],
            [255, 255, 179],
            [190, 186, 218],
            [251, 128, 114],
            [128, 177, 211],
            [253, 180, 98],
            [179, 222, 105],
            [252, 205, 229],
        ]
    )
    / 255.0
)
