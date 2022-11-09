import geopandas as gpd
shppath = "./Point_4888_UID_2/point_4888_UID_2.shp"
gdf = gpd.read_file(shppath)



df1 = gdf[['UniqueID', 'FeatureNam','FeatureSta']]
df1  = df1.groupby(['UniqueID','FeatureNam','FeatureSta']).size().reset_index(name='Count')
df1.to_excel("output.xlsx")
print(df1)
