from connector.connector import BaseConnector
from configs.settings import get_settings
import pandas as pd
from utils.load_query import load_query
from path.path import ingest_data
from etl.ingest import ingest_to_bronze
from dw_init.dw_init import dw_init_func

if __name__ == "__main__":
    # dw_init_func()
    ingest_to_bronze(get_settings().OLTP_URL,get_settings().DW_URL)