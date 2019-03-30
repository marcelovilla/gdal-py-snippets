#!/usr/bin/env python

# =============================================================================
# Date:     October, 2018
# Author:   Marcelo Villa P.
# Purpose:  Uses gdal Translate library function to convert raster data from
#           HDF To GeoTIFF.
# Notes:    The gdal Translate library function (like the gdal_translate
#           command line utility) takes different options. A list of these is
#           available at:
#           https://gdal.org/python/osgeo.gdal-module.html#TranslateOptions
# =============================================================================

from osgeo import gdal

# open dataset, get subsets and open one of them
ds = gdal.Open('input.hdf')
sub_ds = ds.GetSubDatasets()
hdf = gdal.Open(sub_ds[0][0])

# get raster resolution
res = hdf.GetGeoTransform()[1]

# call gdal Translate
out_ds = gdal.Translate(destName='output.tif', srcDS=hdf, xRes=res, yRes=res)
del out_ds
