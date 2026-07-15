from connector.connector import BaseConnector
from configs.settings import get_settings
from utils.load_query import load_query
from path.path import dw_init_path
from sqlalchemy import text
from utils.logger import get_logger

logger = get_logger("dw_init",log_to_file=False)

def dw_init_func():
    with BaseConnector(get_settings().DW_URL) as conn:
        engine = conn.get_engine()
        rendered_sql = load_query(sql_path=dw_init_path,schema = get_settings().DW_SCHEMA)
        statements = [stmt.strip() for stmt in rendered_sql.split(';') if stmt.strip()]
        try:
            with engine.begin() as transaction_conn:
                for stmt in statements:
                    transaction_conn.execute(text(stmt))
            logger.info("Init DW Schema Succesful")
        except Exception as e:
            logger.error(f"Init DW Schema Failed: {e}")
            raise RuntimeError (f"Init DW Schema Failed: {e}")