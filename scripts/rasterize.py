#!/usr/bin/env python
# =============================================================================
# Date:     June, 2019
# Author:   Marcelo Villa P.
# Purpose:  Creates a raster with the distance to the closest target.
# Notes:    Rasterizes a shapefile.
# =============================================================================
import math

import gdal
import ogr

# open shapefile, get layer and get extent
fn = '../data/vector/COL_rails.shp'
ds = ogr.Open(fn, 0)
lyr = ds.GetLayer()
xmin, xmax, ymin, ymax = lyr.GetExtent()

# specify pixel resolutions and calculate output raster dimensions
pw = 0.025
ph = 0.025
cols = math.ceil((xmax - xmin) / pw)
rows = math.ceil((ymax - ymin) / ph)

# create empty output raster
out_fn = '../data/raster/COL_rails.tif'
driver = gdal.GetDriverByName('GTiff')
out_ds = driver.Create(out_fn, cols, rows, 1, gdal.GDT_Byte)

# set geotransform and projection
gt = (xmin, pw, 0, ymax, 0, -ph)
sr = lyr.GetSpatialRef().ExportToWkt()
out_ds.SetGeoTransform(gt)
out_ds.SetProjection(sr)

# rasterize layer
band = out_ds.GetRasterBand(1)
gdal.RasterizeLayer(out_ds, [1], lyr, burn_values=[1])

# set NoData value and close shapefile and raster
band.SetNoDataValue(0)
del ds, out_ds
