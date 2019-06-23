#!/usr/bin/env python
# =============================================================================
# Date:     May, 2018
# Author:   Marcelo Villa P.
# Purpose:  Creates a specific number of random points (samples) over a raster.
# Notes:    `val`, declared in line 31 may be any number but must be different
#           than NoData value and any other cell value that the raster might
#           have.
# =============================================================================
from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import numpy as np

# open TIFF file and read it as a NumPy array
ds_raster = gdal.Open("raster.tif")
band = ds_raster.GetRasterBand(1)
arr = band.ReadAsArray()
nodata = band.GetNoDataValue()

samples = 1000  # number of points

# skip NoData values
indices = np.nonzero(arr != nodata)

# select random indices to create the points at
ind = np.random.choice(np.arange(len(indices[0])), samples, replace=False)

# assign a specific value to the cells where points are going to be created at
val = -9999
arr[indices[0][ind], indices[1][ind]] = val

# mask the array using the previous specific value
(y_index, x_index) = np.nonzero(arr == val)

# get raster GeoTransform values
(upper_left_x, x_size, x_rotation, upper_left_y, y_rotation, y_size) = \
    ds_raster.GetGeoTransform()

# calculate x and y coordinates
x_coords = x_index * x_size + upper_left_x + (x_size / 2)
y_coords = y_index * y_size + upper_left_y + (y_size / 2)

# create samples
fn = "my.shp"   # output shapefile name
driver = ogr.GetDriverByName('ESRI Shapefile')
ds_points = driver.CreateDataSource(fn)
lyr = ds_points.CreateLayer('samples',
                            osr.SpatialReference(ds_raster.GetProjection()),
                            ogr.wkbPoint)

# create feature and geometry dummies
feature = ogr.Feature(lyr.GetLayerDefn())
point = ogr.Geometry(ogr.wkbPoint)

# iterate over the coordinates, create the points and store them in the output
# file
for x, y in zip(x_coords, y_coords):
    point.AddPoint(x, y)
    feature.SetGeometry(point)
    lyr.CreateFeature(feature)

del ds_raster, ds_points
