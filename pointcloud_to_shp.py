## DEPENDENCIES
from shapely.geometry import Polygon
from pathlib import Path
import geopandas as gpd
import subprocess
import timeit
import json
#pdal library should be installed on the system


# Function to check wether the file extension is valid point cloud file
def is_pointcloud(pc_ext):
    """ Checker for valid point cloud extensions, support only LAS, LAZ formats """
    pc_ext_list = ['.las', '.laz']
    if pc_ext in pc_ext_list:
        return True
    else:
        return False



# Function to get bounding box of point cloud files and make shapefile of those
def pc_to_shp(pc_directory):
    """ Get the bounding box of point cloud and convert it to shapefile to get the bbox of point clouds """
    # start of time benchmark
    start = timeit.default_timer()
    # conversion of raw path to window path
    input_dir = Path(pc_directory)
    # empty lists to store file names and geometry polygons
    name_list = []
    shape_list = []
    for folder in input_dir.glob('**'):
        for filename in folder.iterdir():
            # check to pass only LAS, LAZ or TXT files
            if is_pointcloud(filename.suffix) is True:
                result = subprocess.run(['pdal', 'info', filename], stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
                json_result = json.loads(result.stdout.decode())
                coords = json_result['stats']['bbox']['native']['boundary']['coordinates']
                bbox_poly = Polygon(*coords)
                name_list.append(str(filename.stem))
                shape_list.append(bbox_poly)
            else:
                print('{} is not a valid point cloud file'.format(filename.stem))
    # write the shapefile
    raw_data = list(zip(name_list,shape_list)) 
    gdf = gpd.GeoDataFrame(raw_data, columns = ['file_name', 'geometry'], geometry='geometry')
    gdf.to_file("point_cloud_bbox.shp")
    # output the time consumed
    end = timeit.default_timer()
    total = end - start
    print('Whole program takes', round(total, 2), "seconds") 

                

## MAIN
def main():
    raw_input = input('give directory path: ')
    input_dir = Path(raw_input)
    if input_dir.is_dir() is True:
        print('directory path is valid, executing program')
        pc_to_shp(input_dir)
    else:
        print('Invalid directory, program aborted')



## EXECTUE  
if __name__=='__main__':
    main()