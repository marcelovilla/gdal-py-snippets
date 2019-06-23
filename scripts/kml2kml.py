#!/usr/bin/env python

# =============================================================================
# Date:     February, 2018
# Author:   Marcelo Villa P.
# Purpose:  Converts a single KML file into multiple single-feature KML files.
# Notes:    This script does not store any attribute information and keeps
#           geometries only.
# =============================================================================

from osgeo import ogr

fn = r'my.kml'  # KML file
dst = r'output_folder'  # Output directory

# open and read KML file
driver = ogr.GetDriverByName('KML')
ds = driver.Open(fn)
layer = ds.GetLayer()

# get spatial reference
sr = layer.GetSpatialRef()

# create a feature definition to store features in the new files
new_feat = ogr.Feature(layer.GetLayerDefn())  # Dummy feature

# iterate through all the features and create a new KML file for each one
for id, feat in enumerate(layer):
    new_ds = driver.CreateDataSource(r'{}\feat_{}.kml'.format(dst, id))
    new_lyr = new_ds.CreateLayer('feat_{}'.format(id), sr, ogr.wkbPolygon)
    geom = feat.geometry().Clone()
    new_feat.SetGeometry(geom)
    new_lyr.CreateFeature(new_feat)

    del new_ds, new_lyr

del ds
