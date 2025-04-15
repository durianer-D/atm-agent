import os
import xarray as xr

import cdsapi

client = cdsapi.Client()

# dataset = "<DATASET-SHORT-NAME>"
dataset = "reanalysis-era5-pressure-levels"
request = {
    # <SELECTION-REQUEST>
    'product_type': ['reanalysis'],
    'variable': ['geopotential'],
    'year': ['2024'],
    'month': ['03'],
    'day': ['01'],
    'time': ['13:00'],
    'pressure_level': ['1000'],
    'data_format': 'grib',

}
# target = "<TARGET-FILE>"
target = "download.grib"

# client.retrieve(dataset, request, target)

def cds_api(variable_name, latitude, longitude, time, is_demo=True):
    """
    
    arguments:
        variable_name: Name of meteorological variable, selecting from ["u10_v10", "geopotential", "t2m", "tp"]
        latitude: 
        longitude:
        time: 
    """
    if is_demo:
        
        ncfile = f"/era5.{variable_name}.longitude_{longitude}_latitude_{latitude}_time_{time}.000000000.nc"
        data = xr.open_dataset(ncfile)
        return data


