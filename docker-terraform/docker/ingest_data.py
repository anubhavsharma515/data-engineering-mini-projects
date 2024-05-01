import subprocess
import argparse

from time import time

import pandas as pd

from sqlalchemy import create_engine

def clean_columns(df) -> pd.DataFrame:

    df.tpep_pickup_time = pd.to_datetime(df.tpep_pickup_time)
    df.tpep_dropoff_time = pd.to_datetime(df.tpep_dropoff_time)
    return df

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    try: 
        subprocess.run(["wget", url, "-O", csv_name])
    except subprocess.CalledProcessError as e: 
        print(f"An error occurred: {e}"):

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    #In case the whole thing can't be read into memory at once, do it chunkwise.
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    #Get first round of values
    df = next(df_iter).pipe(clean_columns)

    #Creates a new table with only the desired shape (n=0)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    while True:
        try:
            t_start = time()

            df = next(df_iter).pipe(clean_columns)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f seconds' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres db")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to PG")

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='user password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='postgres database name')
    parser.add_argument('--table_name', required=True, help='name of table where we will write results to')
    parser.add_argument('--url', required=True, help='url of csv file')

    args = parser.parse_args()

    main(args)

