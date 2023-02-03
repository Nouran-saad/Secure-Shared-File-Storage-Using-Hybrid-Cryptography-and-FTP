from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, LongType,StringType,FloatType

spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

# Create schema when reading u.data
schema = StructType([ \
                     StructField("stationid", StringType(), True), \
                     StructField("date", IntegerType(), True), \
                     StructField("measuretype", StringType(), True), \
                     StructField("temperature", FloatType(), True)])

tempDF = spark.read.option("sep", ",").schema(schema).csv("/home/nouran/Downloads/spark/1800.csv") 

tempDF.createOrReplaceTempView("temps")

min_temps_df = spark.sql("select stationid,MIN(temperature) as min_temp from temps where measuretype='TMIN' group by stationid ")
min_temps_df.rdd.saveAsTextFile("./output2/min-temp-dataframe/")

# Grab the top 10
min_temps_df.show(10)

# Stop the session
spark.stop()
               
       