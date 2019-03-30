#!/usr/bin/env python3

# =============================================================================
# Date:     October, 2018
# Author:   Marcelo Villa P.
# Purpose:  Uses gdal Warp library function to reproject a raster dataset.
# Notes:    The gdal Warp library function (like the gdal_warp command line
#           utility) takes different options. A list of these is available at:
#           https://gdal.org/python/osgeo.gdal-module.html#WarpOptions
# =============================================================================

from osgeo import gdal
from osgeo import osr

# open raster dataset
ds = gdal.Open('input.tif')

# get raster resolution
res = ds.GetGeoTransform()[1]

# define a spatial reference
sr = osr.SpatialReference()
sr.ImportFromEPSG(32618)  # UTM zone 18N

# call gdal Warp
out_ds = gdal.Warp(destNameOrDestDS='output.tif', srcDSOrSrcDSTab=ds,
                   dstSRS=sr, xRes=res, yRes=res)
del out_ds
