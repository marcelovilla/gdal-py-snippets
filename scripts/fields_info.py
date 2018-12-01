#!/usr/bin/env python2.7

# =============================================================================
# Date:     December, 2018
# Author:   Marcelo Villa P.
# Purpose:  Prints information about a shapefile's fields.
# =============================================================================

from osgeo import ogr

ds = ogr.Open('my.shp', 0)
lyr = ds.GetLayer(0)
lyr_dfn = lyr.GetLayerDefn()

for i in range(lyr_dfn.GetFieldCount()):
    field_dfn = lyr_dfn.GetFieldDefn(i)
    print('Name:\t {}'.format(field_dfn.GetName()))
    print('Type:\t {}'.format(field_dfn.GetTypeName()))
    print('Width:\t {}'.format(field_dfn.GetWidth()))
    print('\n')
