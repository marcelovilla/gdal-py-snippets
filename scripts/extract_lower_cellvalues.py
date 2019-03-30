#!/usr/bin/env python3

# =============================================================================
# Date:     November, 2017
# Author:   Marcelo Villa P.
# Purpose:  Extracts a predefined number of cells with the lowest cell values.
# =============================================================================

from osgeo.gdalconst import *
from osgeo import gdal
import numpy as np

# enable gdal exceptions
gdal.UseExceptions()

# open raster and read it as a numpy array
ds = gdal.Open("my.tif")  # input TIFF file
arr = np.array(ds.GetRasterBand(1).ReadAsArray())

# convert NoData values in the array to np.nan
arr = np.where(arr < 0, np.nan, arr)

# get number of columns and rows of the original raster
cols = ds.RasterXSize
rows = ds.RasterYSize
size = cols * rows

# define number of cells to extract from the original raster
perc = 0.05  # percentage
k = int(size * perc)  # 5% cells of the raster

# create arrays with the lowest 5% cells of the original raster
values = np.partition(arr.flatten(), k)[:k]
arr = np.where(np.isin(arr, values), arr, np.nan)  # lowest 5%

# create output TIFF file
driver = ds.GetDriver()
dsOut = driver.Create('output.tif', cols, rows, 1, GDT_Float64)

# get raster band
outBand = dsOut.GetRasterBand(1)

# write the data to the output TIFF file
outBand.WriteArray(arr, 0, 0)

# flush data to the disk and set the NoData value
outBand.FlushCache()
outBand.SetNoDataValue(-9999)

# georeference and set projection of the TIFF file
dsOut.SetGeoTransform(ds.GetGeoTransform())
dsOut.SetProjection(ds.GetProjection())

# close raster file and delete variables
dsOut = None
del ds, dsOut, outBand