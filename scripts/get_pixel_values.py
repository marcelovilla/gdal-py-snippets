#!/usr/bin/env python
# =============================================================================
# Date:     June, 2019
# Author:   Marcelo Villa P.
# Purpose:  Gets array of values in a raster given two arrays of x and y
#           coordinates.
# =============================================================================
import gdal
import numpy as np

from .helper_functions import create_random_points


def get_indices(x, y, ox, oy, pw, ph):
    """
    Gets the row (i) and column (j) indices in an array for a given set of
    coordinates. Based on https://gis.stackexchange.com/a/92015/86131
    :param x:   array of x coordinates (longitude)
    :param y:   array of y coordinates (latitude)
    :param ox:  raster x origin
    :param oy:  raster y origin
    :param pw:  raster pixel width
    :param ph:  raster pixel height
    :return:    row (i) and column (j) indices
    """
    i = np.floor((oy-y) / ph).astype('int')
    j = np.floor((x-ox) / pw).astype('int')

    return i, j


# open raster and read data
fn = '../data/raster/COL_msk_alt.vrt'
ds = gdal.Open(fn, 0)
arr = ds.ReadAsArray()

# get raster envelope (bounding box)
xmin, pw, xskew, ymax, yskew, ph = ds.GetGeoTransform()
xmax = xmin + (ds.RasterXSize * pw)
ymin = ymax + (ds.RasterYSize * ph)
envelope = (xmin, ymin, xmax, ymax)

# create random points within the envelope
n = 1000
x, y = create_random_points(envelope, n)

# get indices
idx = get_indices(x, y, xmin, ymax, pw, ph)

# get corresponding pixel values
values = arr[idx]
