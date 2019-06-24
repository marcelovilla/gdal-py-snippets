#!/usr/bin/env python
# =============================================================================
# Date:     February, 2018
# Author:   Marcelo Villa P.
# Purpose:  Resamples a raster to a new resolution.
# Notes:    This script has been slightly adapted from Chris Garrards's
#           "Geoprocessing with Python" book. In this case the script resamples
#           to a resolution two times higher (pixel size is one quarter of the
#           original pixel size) than the original file.
# =============================================================================
import gdal

from helper_functions import array_to_tiff

# open raster and get band
fn = '../data/raster/wc2.0_10m_prec_01.tif'
ds = gdal.Open(fn, 0)

# specify output raster cols and rows
cols = ds.RasterXSize * 2
rows = ds.RasterYSize * 2

# get projection and GeoTransform
sr = ds.GetProjection()
gt = list(ds.GetGeoTransform())

# edit the geotransform so pixels are one quarter of the previous size
gt[1] /= 2
gt[5] /= 2

# read dataset specifying a larger buffer so the array has more values than the
# original data.
arr = ds.ReadAsArray(buf_xsize=cols, buf_ysize=rows)

# create output raster
out_fn = '../data/raster/wc2.0_10m_prec_01_resample.tif'
nd_value = ds.GetRasterBand(1).GetNoDataValue()
array_to_tiff(arr, out_fn, sr, gt, gdal.GDT_Int16, nd_value)

# close original raster
del ds
