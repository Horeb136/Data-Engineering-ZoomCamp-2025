#!/usr/bin/env python
# coding: utf-8

# Libraries used 
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

def main (params) : 
    # Import environment variables 
    load_dotenv()
    password = os.getenv("POSTGRES_PASSWORD")

    # Def the arguments 
    user = params.user
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_file = "output.csv"
    parquet_file = "output.parquet"

    # Get the parquet file
    os.system(f"wget {url} -O {parquet_file}")

    # Load the file and get the csv 
    df = pd.read_parquet(parquet_file, engine ="pyarrow")

    # Get the CSV 
    df.to_csv(csv_file, index=False)

    # Ingestion into the database
    # Create engine to connect to PostgreSQL
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
   
    # Create the iterative df
    df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)

    # Get the current df and make formatting
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Insert in database
    df.head(n=0).to_sql(name= table_name, con=engine, if_exists="replace") # Insert the columns of the dataframe
    df.to_sql(name= table_name, con=engine, if_exists="append")

    # Ingest the remain 
    while True:
        try:
            # Start the timer 
            t_start = time()

            # Read the next chunk
            df = next(df_iter)

            # Format the columns 
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            # Add data to the existing table
            df.to_sql(name= table_name, con=engine, if_exists="append")

            # End the timer
            t_end = time()

            print('Inserted another chunk... took %.3f second(s)' % (t_end - t_start))

        except StopIteration:
            print("End of data importation.")
            break

if __name__ == "__main__":
    # Def the arguments
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument('--table_name', help="name of the table where we will write the results to")
    parser.add_argument('--url', help="url of the parquet file")

    args = parser.parse_args()
    main(args)

