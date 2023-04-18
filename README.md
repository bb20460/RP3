# RP3: SATELLITE REMOTE SENSING TECHNIQUES FOR DETECTING PROXIES OF RADIATION ANOMALIES AT NUCLEAR FACILITIES: PROCESSING PROCEDURES AND LIMITATIONS

The research project aimed to investigate satellite remote sensing techniques for continuous monitoring of nuclear facilities, with a primary emphasis on outgoing longwave radiation, thermal infrared imagery, and structural defect assessment using machine learning techniques. The codebase developed for this project includes code that generates relevant figures based on the research findings, serving as a starting point for further exploration towards an analytics-based platform. The To-Do list highlights areas that require further research and serves as a guide for future investigations.

Notebooks have been provided for the figure generations, images and respective geojson files for each case study have been provided for ease of replication/interest. As of 19/04/2023, the datasets are accessible and provide the results obtained.

links for the models/reference examples used in this study

xView2: Building Damage Assessment  
1) https://github.com/DIUx-xView/xView2_baseline.git                       
1.1) https://github.com/vdurnov/xview2_1st_place_solution.git  
1.1.1) https://github.com/DIUx-xView/xView2_first_place/releases  

Landsat Temperature Downscaling  
2) https://github.com/palubad/LST-downscaling-to-10m-GEE.git  

General GEE code:  
3) https://github.com/google/earthengine-community.git  
4) https://github.com/google/earthengine-api.git  

Planet API:    
5) https://github.com/planetlabs/planet-client-python.git  


TO-DO/Caveats: (in further research)  

☐ Change the recent collections to filter for images that have the same acquisition time (within 30mins) over the course of a longer time period instead of within a week. 

☐ Do not directly call os.system command line calls, use GDAL api if available (?) and generalise for multiple application systems

☐ Finish steamlit website application/ or generate a user interface where a point is drawn on an interactive map.

☐ Main.py file which connects all utilities and methods
...
