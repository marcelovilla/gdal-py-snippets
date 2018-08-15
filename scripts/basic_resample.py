#!/usr/bin/env python2.7

# =============================================================================
# Date:     February, 2018
# Author:   Marcelo Villa P.
# Purpose:  Resamples a raster to a new resolution without interpolation.
# Notes:    This script has been slightly adapted from Chris Garrards's
#           "Geoprocessing with Python" book. In this case the script re-
#           samples to a resolution three times higher (pixel size is one
#           sixth of the original pixel size) than the original file. This
#           relation can easily be changed on lines 24-25 and 34-35.
# =============================================================================

from osgeo import gdal

# enable gdal exceptions
gdal.UseExceptions()

# open raster and get band
in_ds = gdal.Open('my.tif')  # input TIFF file
in_band = in_ds.GetRasterBand(1)

# multiply output size by 3
out_rows = in_band.YSize * 3
out_columns = in_band.XSize * 3

# create output TIFF file
gtiff_driver = gdal.GetDriverByName('GTiff')
out_ds = gtiff_driver.Create('output_resampled.tif', out_columns, out_rows)
out_ds.SetProjection(in_ds.GetProjection())
geotransform = list(in_ds.GetGeoTransform())

# edit the geotransform so pixels are one-sixth previous size
geotransform[1] /= 3
geotransform[5] /= 3
out_ds.SetGeoTransform(geotransform)

# read input band and write to output band
# specify a larger buffer size when reading data
data = in_band.ReadAsArray(buf_xsize=out_columns, buf_ysize=out_rows)
out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(data)

# flush data to disk, compute statistics and build overviews
out_band.FlushCache()
out_band.ComputeStatistics(False)
out_ds.BuildOverviews('average', [2, 4, 8, 16, 32, 64])
del out_ds