from s2_clouds import *
from landsat_clouds import *
from recent_collections import *
from allmodel import *
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#ee.Authenticate()
ee.Initialize()


def main():
    final_landsat8_collection, suitablel8_images, final_landsat9_collection, suitablel9_images, extent = mainl8l9()
    final_S2_collection, suitableS2_images= mainS2()
    l9_list, l8_list, c8_list, c9_list = getRecent(suitablel8_images, suitablel9_images, suitableS2_images)
    print(l8_list)
    print("                        ")
    print(c8_list)
    print("                        ")
    print(l9_list)
    print("                        ")
    print(c9_list)
    #l_collection_recentimg,  s2_collection_recentimg, recent_pair_l, suitable_pairs, 
    stats8_downscale = np.array([]) # [Landsat 8 acquisition date, Sentinel 2 acquisition date, Max Temp, Min Temp, Mean Temp]
    stats8_normal = np.array([]) # [Landsat 8 acquisition date, Sentinel 2 acquisition date, Max Temp, Min Temp, Mean Temp]
    for i in range(len(l8_list)):
        stat_values, more_values = model(l8_list[i], c8_list[i], extent)
        print(stat_values)
        print(more_values)
        stats8_downscale = np.append(stats8_downscale, stat_values)
        stats8_normal = np.append(stats8_normal, more_values)
        
    
    #export stats to csv
    stats = stats8_downscale.reshape(len(l8_list), 5)
    df = pd.DataFrame(stats, columns = ['Landsat 8 acquisition date', 'Sentinel 2 acquisition date', 'Max Temp', 'Min Temp', 'Mean Temp'])
    df.to_csv('stats8_downscale.csv', index=False)

    stats = stats8_normal.reshape(len(l8_list), 5)
    df = pd.DataFrame(stats, columns = ['Landsat 8 acquisition date', 'Sentinel 2 acquisition date', 'Max Temp', 'Min Temp', 'Mean Temp'])
    df.to_csv('stats8_normal.csv', index=False)

    stats9_downscale = np.array([]) # [Landsat 8 acquisition date, Sentinel 2 acquisition date, Max Temp, Min Temp, Mean Temp]
    stats9_normal = np.array([]) # [Landsat 8 acquisition date, Sentinel 2 acquisition date, Max Temp, Min Temp, Mean Temp]
    for i in range(len(l9_list)):
        stat_values, more_values = model(l9_list[i], c8_list[i], extent)
        print(stat_values)
        print(more_values)
        stats9_downscale = np.append(stats9_downscale, stat_values)
        stats9_normal = np.append(stats9_normal, more_values)
        
    
    #export stats to csv
    stats = stats9_downscale.reshape(len(l9_list), 5)
    df = pd.DataFrame(stats, columns = ['Landsat 9 acquisition date', 'Sentinel 2 acquisition date', 'Max Temp', 'Min Temp', 'Mean Temp'])
    df.to_csv('stats9_downscale.csv', index=False)

    stats = stats9_normal.reshape(len(l9_list), 5)
    df = pd.DataFrame(stats, columns = ['Landsat 9 acquisition date', 'Sentinel 2 acquisition date', 'Max Temp', 'Min Temp', 'Mean Temp'])
    df.to_csv('stats9_normal.csv', index=False)



    #return l_collection_recentimg,  s2_collection_recentimg, recent_pair_l

main()

def stats():
    #import stats from csv
    df = pd.read_csv('stats.csv')
    
    # get the dates
    l8_date = df['Landsat 8 acquisition date']
    s2_date = df['Sentinel 2 acquisition date']

    # get the max, min, mean of the stats
    max_temp = df['Max Temp']
    min_temp = df['Min Temp']
    mean_temp = df['Mean Temp']

    # plot the stats
    plt.plot(l8_date, max_temp, label = 'Max Temp', color = 'red')
    plt.plot(l8_date, min_temp, label = 'Min Temp', color = 'green')
    plt.plot(l8_date, mean_temp, label = 'Mean Temp', color = 'blue')
    plt.xlabel('Landsat 8 acquisition date')
    plt.ylabel('Temperature (C)')
    plt.show()

#stats()


