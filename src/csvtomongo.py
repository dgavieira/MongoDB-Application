import os
import sys
import pandas as pd
from pymongo import MongoClient
import json


def import_csv(filepath):
    mng_client = MongoClient('localhost', 27017)
    mng_db = mng_client['covid_data']
    collection_name = 'covid_collection'
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)


if __name__ == '__main__':
    filepath = 'D:\GitHub\MongoDB-Application\data\owid-covid-data-1.csv'
    import_csv(filepath)
