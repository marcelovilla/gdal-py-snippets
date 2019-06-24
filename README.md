# gdal-py-snippets
This repository presents a wide range of different-purpose small examples using the gdal-python bindings (both `gdal` and `ogr`). It uses a fair amount of `numpy` as well, along with other third party packages such as `pandas` and `geopandas`.

The programs presented in this repository were developed using Python 3.6.5 and the following packages versions:
* `gdal` version: 2.3.3
* `geopandas` version: 0.4.0
* `numpy` version: 1.14.3
* `pandas` version: 0.24.2


### Data
All the snippets in this repository use open data. Here is a table with the description of each dataset used<sup>*</sup> and its sources:

| Dataset                   | Description                                             | Type   | Extension | Source             |
|---------------------------|---------------------------------------------------------|--------|-----------|--------------------|
| wc2.0_10m_prec_01         | Average January global precipitation from 1970 to 2000. | Raster | .tif      | [WorldClim][1]     |
| COL_msk_alt               | Elevation for Colombia (country mask)                   | Raster | .vrt      | [DIVA_GIS][2]      |
| COL_rails                 | Colombian railroads                                     | Vector | .shp      | [DIVA_GIS][2]      |
| ne_110m_admin_0_countries | Administrative boundaries (countries) of the world.     | Vector | .shp      | [Natural Earth][3] |

<sup>*I do not own any of the datasets here presented.</sup>


### Snippets
Here is a brief explanation for each snippet:

#### 1. [attribute_table_to_csv][4]
Saves a shapefile's attribute table to a given csv file using `ogr` and `pandas`. The program iterates through each feature in the shapefile and then iterates through each one of its fields, storing the values in a `DataFrame`. The `DataFrame` is then converted to a csv file.

#### 2. [compute_proximity][5]
Computes proximity (euclidean distance) in pixels from each cell to a target value using the `gdal.ComputeProximity()` function. The input raster is the output from [rasterize][9].

#### 3. [euclidean_distance][6]
Computes the euclidean distance (in pixels) from each cell to a target value. Similar to [compute_proximity][5] but instead of using `gdal`'s built-in function an own implementation of the distance computation is presented. In this case, the target values are the rasterized lines produced in [rasterize][9]. This snippet uses `numpy` to vectorize the distance computation (following [Pythagoras' theorem][7]). It creates a distance matrix to each target value (*i.e.* each value different from NoData). Then, the minimum distance value for each cell is retrieved and a single distance matrix is returned.

#### 4. [extract_lowest_cell_values][8]<sup>*</sup>
Extracts an arbitrary percentage (5% in this case) of the lowest cell values in the raster.

#### 4. [raster_up_sample][9]<sup>*</sup>
Resamples (up-samples) a raster to a higher resolution. In order to do this it reads the original `GeoTransform` and changes the pixel width and pixel height to be proportionally smaller. Then it reads the data from the original dataset specifying `buf_xsize` and `buf_ysize` so the array where the data is going to be stored fits the new dimensions. When specifying a bigger buffer than the original raster dimensions in the `ReadAsArray()` method, original values are repeated to fit the new dimensions.

<sup>*This snippet was slightly adapted from one example presented by Chris Garrard in [Geoprocessing with Python's][10] 9th chapter.</sup>

#### 5. [rasterize][11]
Rasterizes a shapefile. It uses `ogr` to open a shapefile and get its extent. Then it creates an empty raster with the same extent as the shapefile and an arbitrary value for the pixel resolution. It uses the `gdal.RasterizeLayer()` function to burn the raster´s band (*i.e.* first and only band) with a 1 where the shapefile presents a feature. The rest is set as NoData.

[1]: http://worldclim.org/version2
[2]: https://www.diva-gis.org/gdata
[3]: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/
[4]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/attribute_table_to_csv.py
[5]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/compute_proximity.py
[6]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/euclidean_distance.py
[7]: https://en.wikipedia.org/wiki/Pythagorean_theorem
[8]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/extract_lowest_cell_values.py
[9]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/raster_up_sample.py
[10]: https://www.manning.com/books/geoprocessing-with-python
[11]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/rasterize.py
