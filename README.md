# gdal-py-snippets
This repository presents a wide range of different-purpose small examples using the gdal-python bindings (both `gdal` and `ogr`). It uses a fair amount of `numpy` as well, along with other third party packages such as `pandas` and `geopandas`.

The programs presented in this repository were developed using Python 3.6.5 and the following packages versions:
* `gdal` version: 2.3.3
* `geopandas` version: 0.4.0
* `numpy` version: 1.14.3
* `pandas` version: 0.24.2


### Data
All the snippets in this repository use open data. Here is a table with the description of each dataset used<sup>*</sup> and its source:

| Dataset                   | Description                                         | Type   | Extension | Source             |
|---------------------------|-----------------------------------------------------|--------|-----------|--------------------|
| ne_110m_admin_0_countries | Administrative boundaries (countries) of the world. | Vector | .shp      | [Natural Earth][1] |

<sup>I do not own any of the datasets here presented.</sup>


### Examples
Here is a brief explanation for each snippet:

##### 1. [attribute_table_to_csv][2]
Saves a shapefile's attribute table to a given csv file using `ogr` and `pandas`. The program iterates through each feature in the shapefile and then iterates through each one of its fields, storing the values in a `DataFrame`. The `DataFrame` is then converted to a csv file.


[1]: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/
[2]: https://github.com/marcelovilla9/gdal-py-snippets/blob/master/scripts/attribute_table_to_csv
