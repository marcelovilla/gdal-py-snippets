#!/usr/bin/env python
# =============================================================================
# Date:     February, 2018
# Author:   Marcelo Villa P.
# Purpose:  Saves a shapefile's attribute table to a csv file.
# =============================================================================
import ogr
import pandas as pd

fn = '../data/vector/ne_110m_admin_0_countries.shp'   # input shapefile
out_fn = '../data/csv/ne_110m_admin_0_countries.csv'  # output csv

# open shapefile and get layer definition
ds = ogr.Open(fn, 0)
lyr = ds.GetLayer(0)
lyr_dfn = lyr.GetLayerDefn()

# get fields names
fields = []
for n in range(lyr_dfn.GetFieldCount()):
    field_dfn = lyr_dfn.GetFieldDefn(n)
    fields.append(field_dfn.name)

# create new DataFrame
df = pd.DataFrame(columns=fields)

# loop through each feature and its fields and store them in the DataFrame
for ind, feat in enumerate(lyr):
    vals = []
    for i in range(lyr_dfn.GetFieldCount()):
        vals.append(feat.GetField(i))
    df.loc[ind] = vals

# save csv and close shapefile
df.to_csv(out_fn, index_label='FID')
del ds
