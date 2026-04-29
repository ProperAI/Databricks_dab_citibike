import os
import sys

sys.path.append(os.getcwd())

from pyspark.sql import SparkSession

import datetime
from src.citibike.citibike_utils import get_trip_duration_mins

def test_get_trip_duration_mins():
    spark = SparkSession.builder.getOrCreate()

    data = [ 
        (datetime.datetime(2026, 1, 20, 15, 25, 0), datetime.datetime(2026, 1, 20, 15, 35, 0)),  # 10 minutes
        (datetime.datetime(2026, 1, 10, 10, 0, 0), datetime.datetime(2026, 1, 10, 10, 30, 0))   # 30 minutes
    ]

    schema = "ts_start timestamp, ts_end timestamp"
    df = spark.createDataFrame(data, schema=schema)

    #check function, in minutes:
    assert_df = get_trip_duration_mins(spark, df, "ts_start", "ts_end", "calc_duration")

    test_results = assert_df.select("calc_duration").collect()

    print(data)
    display(assert_df)              
    display(test_results)

    # assert test_results[0:2] == [10, 30]
    assert test_results[0] == [10]
    assert test_results[1] == [30]


test_get_trip_duration_mins()