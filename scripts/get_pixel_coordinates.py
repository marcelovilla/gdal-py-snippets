#!/usr/bin/env python
# =============================================================================
# Date:     June, 2019
# Author:   Marcelo Villa P.
# Purpose:  Creates two 2D arrays (grids) with the x and y coordinates of each
#           pixel center in a raster.
# =============================================================================
import gdal
import numpy as np

# open raster and get GeoTransform and number of rows and cols
fn = '../data/raster/COL_msk_alt.vrt'
ds = gdal.Open(fn, 0)
gt = ds.GetGeoTransform()

# get origin (upper left corner) coordinates
ox = gt[0]
oy = gt[3]

# get pixel width and height
pw = gt[1]
ph = gt[5]

# compute end (lower right corner) coordinates
ex = ox + (ds.RasterXSize * pw)
ey = oy + (ds.RasterYSize * ph)

# create 1D arrays with the coordinates of each axis (shifted to the center)
x = np.arange(ox, ex, pw) + pw/2
y = np.arange(oy, ey, ph) + ph/2

# create the 2D coordinates arrays
xx, yy = np.meshgrid(x, y)
