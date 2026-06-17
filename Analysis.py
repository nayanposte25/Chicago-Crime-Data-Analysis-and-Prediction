from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("Crime Analysis").getOrCreate()

# Load dataset
data = spark.read.csv(
    "C:/Users/rahul/BDA_Nayan/chicago_crimes.csv",
    header=True,
    inferSchema=True
)

# Sample data
sample_data = data.sample(fraction=0.1, seed=42)

# Top crimes
print("Top Crime Types:")
sample_data.groupBy("Primary Type") \
    .count() \
    .orderBy("count", ascending=False) \
    .show(10)

# Crimes by year
print("Crimes by Year:")
sample_data.groupBy("Year") \
    .count() \
    .orderBy("Year") \
    .show()

# Arrest analysis
print("Arrest Analysis:")
sample_data.groupBy("Arrest") \
    .count() \
    .show()

# District analysis
print("Top Districts:")
sample_data.groupBy("District") \
    .count() \
    .orderBy("count", ascending=False) \
    .show(10)