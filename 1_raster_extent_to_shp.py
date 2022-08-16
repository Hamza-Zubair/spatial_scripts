from pathlib import Path
from shapely.geometry import box, mapping
import fiona
from fiona.crs import to_string
import rasterio

def raster_extent_to_shp(directory,raster_suffix):
    """" Creates shapefile/s of extent for any/all rasters in directory with valid coordinate reference system
    directory: give directory path as raw-string 
    raster_suffix: give raster suffix for which creating extent shapefile is desired as str
    """
    count = 0
    for folder in Path(directory).glob('**'):
        for filename in folder.iterdir():
            if filename.suffix == raster_suffix:
                raster = rasterio.open(filename)
                bounds = raster.bounds
                raster_extent = box(*bounds)
                # set the path
                out_path = Path.joinpath(folder,filename.stem+'_extent.shp')
                # lil house keeping for making shapefile
                poly_schema = {'geometry': 'Polygon','properties': {'raster_name': 'str'},}
                if raster.crs is not None and raster.crs.is_valid is True:
                    crs_raster = to_string(raster.crs)
                    with fiona.open(out_path, 'w', 'ESRI Shapefile', poly_schema, crs= crs_raster) as c:
                        c.write({
                            'geometry': mapping(raster_extent),
                            'properties': {'raster_name': filename.stem},
                        })
                    count = count + 1
    print ('Total shapefiles written: {}'.format(count))

def main():
    input_dir = input('give the raster directory path: ')
    if Path(input_dir).is_dir() is True:
        raster_suffix = input('give the suffix of raster file: ')
        raster_extent_to_shp(input_dir, raster_suffix)
    else:
        print('Invalid input directory')  

        
if __name__=='__main__':
    main()