import geopandas as gpd
gpd.options.display_precision=3
import shapely.geometry
import pandas as pd

# shp_path = r"C:\Users\LonghanZhang\Airborne Logic\ABL-Team Site - Longhan\jupyter_demos\test.shp"
# shp = gpd.read_file(shp_path)



# new_list=[];

def count_line(direction,start_val,gdf):
    # length=len(gdf)
    # print(length)
    new_list = []
    if (direction=="north"):
        gdf['y'] = gdf.centroid.y                     #   store the y axis into new column
        gdf=gdf.sort_values(by='y',ascending=False)    #   all columns will be sorted basing on the y value
        
        for i in range(0,len(gdf)):                   #   iterate each rows in GDF
            temp=start_val+i;                         #   start value increment one at each iteration
            new_list.append(temp);                    #   store the value into list
        
        gdf['rank']=new_list;                         #   label the rank  
        
        
    if (direction=="south"):
        gdf['y']=gdf.centroid.y
        gdf=gdf.sort_values(by='y',ascending=True)

        for i in range(0,len(gdf)):
            temp=start_val+i;
            new_list.append(temp);
        
        gdf['rank']=new_list;
        
        
    if (direction=="east"):
        gdf['x']=gdf.centroid.x
        gdf=gdf.sort_values(by='x',ascending=False)

        for i in range(0,len(gdf)):
            temp=start_val+i;
            new_list.append(temp);
        
        gdf['rank']=new_list;
        
        
    if (direction=="west"):
        gdf['x']=gdf.centroid.x
        gdf=gdf.sort_values(by='x',ascending=True)
        
        for i in range(0,len(gdf)):
            temp=start_val+i
            new_list.append(temp);
            
        gdf['rank']=new_list;
            
    return gdf    


# ha=count_line("east",6,shp)
# ha
