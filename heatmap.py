from pyspark.sql import SparkSession
import folium
from folium.plugins import HeatMap

spark = SparkSession.builder.appName("Heatmap").getOrCreate()

data = spark.read.csv(
    "C:/Users/rahul/BDA_Nayan/chicago_crimes.csv",
    header=True,
    inferSchema=True
)

sample_data = data.sample(fraction=0.1, seed=42)

heatmap_data = sample_data.select("Latitude", "Longitude").dropna()

heatmap_small = heatmap_data.limit(5000)

heatmap_pd = heatmap_small.toPandas()

crime_map = folium.Map(location=[41.8781, -87.6298], zoom_start=10)

HeatMap(
    heatmap_pd[['Latitude', 'Longitude']].values
).add_to(crime_map)

crime_map.save("crime_heatmap.html")

print("Heatmap created successfully!")