import os
from planetquery import *

def setup():
    #import planet api key from environment variable
    PLANET_API_KEY = os.environ.get('PL_API_KEY') #'PLAKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    cloudcover = 0.1
    startdate = convert_date('2022-07-01')
    enddate = convert_date('2022-08-30')
    aoi = {
    "type": "Polygon",
    "coordinates": [
        [ 
                [
                141.02552103573942,
                37.42523798714251
                ],
                [
                141.02552103573942,
                37.41697182701044
                ],
                [
                141.0353183469465,
                37.41697182701044
                ],
                [
                141.0353183469465,
                37.42523798714251
                ],
                [
                141.02552103573942,
                37.42523798714251
                ]
        ]
    ]
    }

    return [aoi, cloudcover, startdate, enddate, PLANET_API_KEY]