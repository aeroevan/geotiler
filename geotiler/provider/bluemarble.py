﻿"""
>>> p = Provider()
>>> p.getTileUrls(Coordinate(10, 13, 7))
('http://s3.amazonaws.com/com.modestmaps.bluemarble/7-r10-c13.jpg',)
>>> p.getTileUrls(Coordinate(13, 10, 7))
('http://s3.amazonaws.com/com.modestmaps.bluemarble/7-r13-c10.jpg',)
"""

from math import pi

from ..core import Coordinate
from ..geo import MercatorProjection, deriveTransformation
from .base import IMapProvider

from .. import tiles

class Provider(IMapProvider):
    def __init__(self):
        # the spherical mercator world tile covers (-π, -π) to (π, π)
        t = deriveTransformation(-pi, pi, 0, 0, pi, pi, 1, 0, -pi, -pi, 0, 1)
        self.projection = MercatorProjection(0, t)

    @property
    def tile_width(self):
        return 256

    @property
    def tile_height(self):
        return 256

    def get_tile_urls(self, coordinate):
        return ('http://s3.amazonaws.com/com.modestmaps.bluemarble/%d-r%d-c%d.jpg' % (coordinate.zoom, coordinate.row, coordinate.column),)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
