#!/usr/bin/env python

# =============================================================================
# Date:     May, 2018
# Author:   Marcelo Villa P.
# Purpose:  Gets the pixel value in a raster for a specific pair of
#           coordinates.
# Notes:    Coordinates must be in the same spatial reference as the raster.
# =============================================================================


from osgeo import gdal

# open TIFF file and read it as a NumPy array
ds = gdal.Open("raster.tif")
arr = ds.ReadAsArray()

# get raster's Geotransform
geotransform = ds.GetGeoTransform()

# assign geotransofrm values
x_origin = geotransform[0]
y_origin = geotransform[3]
pixel_width = geotransform[1]
pixel_height = -geotransform[5]

# specify coordinates
x = -74.153833
y = 11.308202

# calculate column and row in the array
col = int((x - x_origin) / pixel_width)
row = int((y_origin - y) / pixel_height)

# index array to get pixel value
pixel_value = arr[row, col]
