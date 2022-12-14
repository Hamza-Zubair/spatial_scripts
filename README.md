### 1_raster_extent_to_shp.py:
#### Description:
Creates shapefile of extent of raster/s using its bounding box in the input directory (checks all sub directories as well).
#### Input:
A directory path and the raster file extension (make sure you add it this way for instance for geotiff write .tif)
#### Output:
shapefiles of raster extents
#### Requirements:
need fiona, rasterio, shapely and pathlib

## 2_clip_vector_to_raster.py:
#### Description:
On the contrarty to usual clip function, this script clips large vector into small subsets basis of raster
#### Input:
A directory path, shapefile absolute path with extension and the raster file extension (make sure you add it this way for instance for geotiff write .tif)
#### Output:
clipped shapefiles if they overlay the rasters from the input directory
#### Requirements:
need rasterio, shapely, pandas, geopandas and pathlib

## 3_pointcloud_to_shp.py:
#### Description:
Takes the directory as input, scans for pointcloud files (any .LAS or .LAZ files) and creates shapefile of the bounding box of pointclouds.
#### Input:
A directory path containing point cloud files.
#### Output:
shapefile generated for bbox of any/all point cloud files found in the directory
#### Requirements:
need shapely, geopandas and pathlib, subprocess, timeit. Also pdal should be installed. change the terminal in VS code so subprocess can access pdal external command.
Also to make sure output is written in script's location check: Go to File > Preferences > Settings and Search for "Execute in File Path".
