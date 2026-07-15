from sqlalchemy import text
from connector.connector import BaseConnector
from configs.settings import get_settings
import pandas as pd
from utils.load_query import load_query
from path.path import ingest_data,insert_jsonb
import uuid
from datetime import datetime, timezone

def ingest_to_bronze(oltp_connection_string, dw_connection_string):
    with BaseConnector(oltp_connection_string) as conn:
        engine = conn.get_engine()
        df = pd.read_sql(
            load_query(sql_path=ingest_data, schema=get_settings().OLTP_SCHEMA),
            engine
        )
    batch_id = str(uuid.uuid4())
    ingested_at = datetime.now(timezone.utc)

    with BaseConnector(dw_connection_string) as dw_conn:
        dw_engine = dw_conn.get_engine()
        temp_table = "raw_users_temp"
        df.to_sql(name=temp_table, con=dw_engine, schema=get_settings().DW_SCHEMA, if_exists="replace", index=False)

        raw_sql = load_query(
            sql_path=insert_jsonb, 
            schema=get_settings().DW_SCHEMA,
            temp_table=temp_table
        )
        with dw_engine.begin() as conn:
            conn.execute(
                text(raw_sql), 
                {"batch_id": batch_id, "ingested_at": ingested_at}
            )
            
            conn.execute(text(f"DROP TABLE {get_settings().DW_SCHEMA}.{temp_table};"))