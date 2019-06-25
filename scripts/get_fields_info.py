#!/usr/bin/env python
# =============================================================================
# Date:     December, 2018
# Author:   Marcelo Villa P.
# Purpose:  Prints information about a shapefile's fields.
# =============================================================================
import ogr

ds = ogr.Open('../data/vector/ne_110m_admin_0_countries.shp', 0)
lyr = ds.GetLayer(0)
lyr_dfn = lyr.GetLayerDefn()

for i in range(lyr_dfn.GetFieldCount()):
    field_dfn = lyr_dfn.GetFieldDefn(i)
    print('Name:\t {}'.format(field_dfn.GetName()))
    print('Type:\t {}'.format(field_dfn.GetTypeName()))
    print('Width:\t {}'.format(field_dfn.GetWidth()))
    print('\n')
