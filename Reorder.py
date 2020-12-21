import geopandas as gpd
# gpd.options.display_precision=3
import shapely.geometry

# shp_path = r"C:\Users\LonghanZhang\Airborne Logic\ABL-Team Site - Longhan\jupyter_demos\test.shp"
# shp = gpd.read_file(shp_path)

# new_list=shp.geometry

# d=list(list(new_list.loc[0].coords))
# c=list(list(new_list.loc[0].coords)[0])
# a=list(list(new_list.loc[0].coords)[0])[0]
# b=list(list(new_list.loc[0].coords)[1])[0]  # first value is rows ,second value is loc of points ,third is x or y

# print(d)
# print(c)
# print(a)
# print(b)


# for i in new_list:
#     print(list(i.coords))
    

# print('above coords is before the swap              below coords is after swap')
def reorder(gdf,direction):
    output = {}
    if (direction=="north"):
        for i,row in gdf.iterrows():
            if list(row['geometry'].coords)[0][1]<list(row['geometry'].coords)[1][1]:        # if the first point y vlaue is less than second point y value 
                new_line = shapely.geometry.LineString(list(row['geometry'].coords)[::-1])  #swap
            else:
                new_line = row['geometry']
            output[i] = new_line
    if (direction=="south"):
        for i,row in gdf.iterrows():
            if list(row['geometry'].coords)[0][1]>list(row['geometry'].coords)[1][1]:        # if the first point y vlaue is less than second point y value 
                new_line = shapely.geometry.LineString(list(row['geometry'].coords)[::-1])  #swap
            else:
                new_line = row['geometry']
            output[i] = new_line
    if (direction=="east"):
        for i,row in gdf.iterrows():
            if list(row['geometry'].coords)[0][0]<list(row['geometry'].coords)[1][0]:        # if the first point x vlaue is less than second point x value 
                new_line = shapely.geometry.LineString(list(row['geometry'].coords)[::-1])  #swap , logic: first point x is greater than second x, we do not flip ,otherwise...
            else:
                new_line = row['geometry']
            output[i] = new_line       
    if (direction=="west"):
        for i,row in gdf.iterrows():
            if list(row['geometry'].coords)[0][0]>list(row['geometry'].coords)[1][0]:        # if the first point x vlaue is less than second point x value 
                new_line = shapely.geometry.LineString(list(row['geometry'].coords)[::-1])  #swap, logic: first point x is less than second x ,we do not flip ,otherwise...
            else:
                new_line = row['geometry']
            output[i] = new_line 
    output = gpd.GeoSeries(output) 
    output.name = 'geometry'   
    return output
           
            

# new = reorder(shp,"north")

# print('===========================')
# # type (new)
# for i,row in shp.iterrows():
#     print(list(row['geometry'].coords))

# print('===========================')
# for i,line in new.items():
#     print(list(line.coords))

    
