#!/usr/bin/env python
# =============================================================================
# Date:     June, 2019
# Author:   Marcelo Villa P.
# Purpose:  Creates a raster with the (pixel) distance to the closest target.
# Notes:    Uses gdal.ComputeProximity() function to compute the distance.
# =============================================================================
import gdal

# open rasterized file and get information
fn = '../data/raster/COL_rails.tif'
ds = gdal.Open(fn, 0)
band = ds.GetRasterBand(1)
gt = ds.GetGeoTransform()
sr = ds.GetProjection()
cols = ds.RasterXSize
rows = ds.RasterYSize

# create empty proximity raster
out_fn = '../data/raster/COL_rails_proximity.tif'
driver = gdal.GetDriverByName('GTiff')
out_ds = driver.Create(out_fn, cols, rows, 1, gdal.GDT_Float32)
out_ds.SetGeoTransform(gt)
out_ds.SetProjection(sr)
out_band = out_ds.GetRasterBand(1)

# compute proximity
gdal.ComputeProximity(band, out_band, ['VALUES=1', 'DISTUNITS=PIXEL'])

# delete input and output rasters
del ds, out_ds
