#!/usr/bin/env python
# =============================================================================
# Date:     June, 2019
# Author:   Marcelo Villa P.
# Purpose:  Creates a raster with the (pixel) distance to the closest target.
# =============================================================================
import gdal
import numpy as np

from helper_functions import array_to_tiff


def euclidean_distance(arr, nd_value):
    """
    Computes the euclidean distance to all non-NoData values in arr.
    :param arr:         raster 2D numpy array
    :param nd_value:    raster´s NoData value
    :return:            distance 2D numpy array
    """
    # create meshgrid
    y, x = arr.shape
    xx, yy = np.meshgrid(np.arange(x), np.arange(y))

    # create indices where arr is different from NoData and reshape them
    ind = np.nonzero((arr != nd_value))
    ix = ind[1].reshape((-1, 1, 1))
    iy = ind[0].reshape((-1, 1, 1))

    # compute legs
    dx = np.abs(iy - yy)
    dy = np.abs(ix - xx)

    return np.min(np.hypot(dx, dy), axis=0)


# open raster, get raster information and read data
fn = '../data/raster/COL_rails.tif'
ds = gdal.Open(fn, 0)
gt = ds.GetGeoTransform()
sr = ds.GetProjection()
arr = ds.ReadAsArray()
nd_value = ds.GetRasterBand(1).GetNoDataValue()

# compute euclidean distance
d = euclidean_distance(arr, nd_value)

# create output raster
out_fn = '../data/raster/COL_rails_distance.tif'
nd_value = -99
array_to_tiff(d, out_fn, sr, gt, gdal.GDT_Float32, nd_value)
