# spatial_scripts

### 1_raster_extent_to_shp.py:
#### Description:
Creates shapefile of extent of raster/s using its bounding box in the input directory (checks all sub directories as well).
#### Input:
A directory path and the raster file extension (make sure you add it this way for instance for geotiff write .tif)
#### Output:
shapefiles of raster extents
#### Requirements:
need fiona, rasterio, shapely and pathlib


## 2_.py:
#### Description:
On the contrarty to usual clip function, this script clips large vector into small subsets based on raster
#### Input:
A directory path, shapefile absolute path with extension and the raster file extension (make sure you add it this way for instance for geotiff write .tif)
#### Output:
clipped shapefiles if they overlay the rasters from the input directory
#### Requirements:
need rasterio, shapely, pandas, geopandas and pathlib
