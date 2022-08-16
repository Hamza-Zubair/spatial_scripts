from pathlib import Path
from shapely.geometry import box
import rasterio
import geopandas as gpd
import pandas as pd

import warnings
warnings.filterwarnings("ignore", message="pandas.Float64Index")
warnings.filterwarnings("ignore", message="pandas.Int64Index")

def clip_vector_to_raster(raster_directory, shapefile_path, raster_suffix):
    """ on the contrarty to usual clip function, it clips the vector on base of raster """
    count = 0
    shp = gpd.read_file(shapefile_path)
    for folder in Path(raster_directory).glob('**'):
        for filename in folder.iterdir():
            if filename.suffix == raster_suffix:
                raster = rasterio.open(filename)
                bounds = raster.bounds
                raster_extent = box(*bounds)
                # clip the shapefile
                clipped = gpd.clip(shp, raster_extent)
                # export the shapefile with same name as of raster which contains it
                out_path = Path.joinpath(folder,filename.stem +'.shp')
                crs = shp.crs
                try:
                    clipped.to_file(out_path, driver='ESRI Shapefile', crs = crs)
                    count = count + 1
                except:
                    pass       
    print ('Total shapefiles clipped as per overlaying raster/s: {}'.format(count))
    

def main():
    input_dir = input('give the raster directory path: ')
    if Path(input_dir).is_dir() is True:
        shp_path = input(r'complete path of shapefile including extension: ')
        if Path(shp_path).is_file(): 
            raster_suffix = input('give the suffix of raster file: ')
        else:
            print('shape file not found')
        try:
            clip_vector_to_raster(input_dir,shp_path, raster_suffix)
        except:
            pass
    else:
        print('Invalid input directory')  

        
if __name__=='__main__':
    main()  