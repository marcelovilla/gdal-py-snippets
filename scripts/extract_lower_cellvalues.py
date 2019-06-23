#!/usr/bin/env python
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
cells_perc = 0.05  # percentage
k = int(size * cells_perc)  # 5% cells of the raster

# create arrays with the lowest 5% cells of the original raster
values = np.partition(arr.flatten(), k)[:k]
arr = np.where(np.isin(arr, values), arr, np.nan)  # lowest 5%

# create output TIFF file
driver = ds.GetDriver()
out_ds = driver.Create('output.tif', cols, rows, 1, GDT_Float64)

# get raster band
out_band = out_ds.GetRasterBand(1)

# write the data to the output TIFF file
out_band.WriteArray(arr, 0, 0)

# flush data to the disk and set the NoData value
out_band.FlushCache()
out_band.SetNoDataValue(-9999)

# georeference and set projection of the TIFF file
out_ds.SetGeoTransform(ds.GetGeoTransform())
out_ds.SetProjection(ds.GetProjection())

# close raster file and delete variables
del ds, out_ds, out_band
