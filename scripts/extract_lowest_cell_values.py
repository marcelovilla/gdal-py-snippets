#!/usr/bin/env python
# =============================================================================
# Date:     November, 2017
# Author:   Marcelo Villa P.
# Purpose:  Extracts an arbitrary percentage of cells with the lowest values
#           in a raster.
# Notes:    The code to extract the lowest k elements in a numpy array was
#           taken from https://stackoverflow.com/a/34226816/7144368.
# =============================================================================
import gdal
import numpy as np

from helper_functions import array_to_tiff

# open raster, read data and get information
ds = gdal.Open('../data/raster/COL_msk_alt.vrt')
arr = ds.ReadAsArray()
sr = ds.GetProjection()
gt = ds.GetGeoTransform()
nd_value = ds.GetRasterBand(1).GetNoDataValue()

# create mask with non-NoData values
mask = (arr != nd_value)

# define number of cells to extract from the original raster
perc = 0.05
k = np.int(np.ceil(mask.sum() * perc))

# create array with the lowest 5% cells of the original raster
idx = np.argpartition(arr[mask], k)
values = arr[mask][idx[:k]]
arr = np.where(np.isin(arr, values), arr, nd_value)

# create output_raster
out_fn = '../data/raster/COL_msk_alt_lowest_5_perc.tif'
array_to_tiff(arr, out_fn, sr, gt, gdal.GDT_Int16, nd_value)