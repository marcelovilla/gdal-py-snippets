#!/usr/bin/env python
# =============================================================================
# Date:     June, 2019
# Author:   Marcelo Villa P.
# Purpose:  Stores helper functions used in other scripts.
# =============================================================================\
import gdal


def array_to_tiff(arr, fn, sr, geotransform, gdtype, nd_val):
    """
    Writes a 2D NumPy array to a GeoTIFF file (1 band).
    :param arr:             2D NumPy array
    :param fn:              output GeoTIFF's file name
    :param sr:              output GeoTIFF's spatial reference
    :param geotransform:    output GeoTIFF's geotransform
    :param gdtype:          GDAL data type
    :param nd_val:          output GeoTIFF's NoData value
    :return:                None
    """
    # get driver and create output TIFF
    driver = gdal.GetDriverByName('GTiff')
    out_tiff = driver.Create(fn, arr.shape[1], arr.shape[0], 1, gdtype)

    # set projection and geotransform
    out_tiff.SetProjection(sr)
    out_tiff.SetGeoTransform(geotransform)

    # set NoData value and write array
    band = out_tiff.GetRasterBand(1)
    band.SetNoDataValue(nd_val)
    band.WriteArray(arr)

    # flush to disk
    band.FlushCache()
    del out_tiff, band
