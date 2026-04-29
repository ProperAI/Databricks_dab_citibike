import os
import sys

sys.path.append(os.getcwd())

import datetime
from src.utils.datetime_utils import timestamp_to_date_col
from pyspark.sql import SparkSession

def test_timestamp_to_date_col():
    spark = SparkSession.builder.getOrCreate()

    #results via df, per intended functionality:
    data = [(datetime.datetime(2026, 1, 10, 5, 0, 0), )]
    schema = "ride_ts timestamp"
    df = spark.createDataFrame(data, schema)

    # Use the utility to add  a date column
    assert_df = timestamp_to_date_col(spark, df, "ride_ts", "dt_ride")

    # get row, compare assertion
    pull_date = assert_df.select("dt_ride").first()

    date_should_be = datetime.date(2026, 1, 10) #should be Jan 10, 2026

    assert pull_date["dt_ride"] == date_should_be

    