#!/usr/bin/env python2.7

# =============================================================================
# Date:     September, 2018
# Author:   Marcelo Villa P.
# Purpose:  Creates a raster file from a point data set, where the values are
#           the number of points (count) in each one of the cells.
# Notes:    The point data set and the raster must have the same spatial
#           reference.
# =============================================================================

from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import numpy as np
import math


def get_indices(x, y, ox, oy, pw, ph):
    """
    Gets the row (i) and column (j) indices in an array for a specific point.
    Slightly adapted from https://gis.stackexchange.com/a/92015/86131

    :param x:   point x coordinate (longitude)
    :param y:   point y coordinate (latitude)
    :param ox:  raster x origin
    :param oy:  raster y origin
    :param pw:  raster pixel width
    :param ph:  raster pixel height
    :return:    row (i) and column (j) indices
    """

    i = math.floor((oy-y) / ph)
    j = math.floor((x-ox) / pw)

    return i, j


# enable gdal and ogr exceptions
gdal.UseExceptions()
ogr.UseExceptions()

# define spatial references
sr4326 = osr.SpatialReference()
sr4326.ImportFromEPSG(4326)

# colombia's bounding box (EPSG:4326)
x_origin = -78.9909352282
y_origin = 12.4373031682
x_end = -66.8763258531
y_end = -4.29818694419

# define pixel width and height values
px_width = 0.0043
px_height = 0.0043

# calculate x and y size
x_size = int((x_end - x_origin) / px_width)
y_size = int((y_origin - y_end) / px_height)

# create empty numpy array
arr = np.zeros((y_size, x_size), dtype=np.int16)

# read input point dataset
input_ds = ogr.Open('my.shp', 0)
lyr = input_ds.GetLayer(0)

# iterate through the points
for point in lyr:

    # get (transformed) x and y coordinates
    geom = point.geometry()
    x = geom.GetX()
    y = geom.GetY()

    # get indices and increment array position
    i, j = get_indices(x, y, x_origin, y_origin, px_width, px_height)
    arr[i, j] += 1

# replace cells with no points with NoData value
arr[(arr == 0)] = -99

# create geotransform
geotransform = [None, None, None, None, None, None]
geotransform[0] = x_origin          # origin x coordinate
geotransform[1] = px_width          # pixel width
geotransform[2] = 0                 # x pixel rotation
geotransform[3] = y_origin          # origin y coordinate
geotransform[4] = 0                 # y pixel rotation
geotransform[5] = -px_height        # pixel height (negative)

# create raster
fn = 'my.tif'
driver = gdal.GetDriverByName('GTiff')
output_ds = driver.Create(fn, x_size, y_size, 1, gdal.GDT_Int16)

# set projection and geotransform
output_ds.SetProjection(sr4326.ExportToWkt())
output_ds.SetGeoTransform(geotransform)

# set NoData value and write array
band = output_ds.GetRasterBand(1)
band.SetNoDataValue(-99)
band.WriteArray(arr)

# flush to disk and delete data sets
band.FlushCache()
del input_ds, output_ds






