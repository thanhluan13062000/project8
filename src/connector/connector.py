from sqlalchemy import create_engine,text
from sqlalchemy import Engine
from urllib.parse import urlparse
from utils.logger import get_logger

logger = get_logger("connector")
class BaseConnector:
    def __init__(
            self,
            connection_string,
            connection_args:dict | None=None,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,
            pool_recycle=3600,
            pool_timeout = 30
        ):
        self.connection_string = connection_string
        self._connection_args = connection_args or {}
        self._engine = None
        self._pool_configs = {
            "pool_size": pool_size,
            "max_overflow": max_overflow,
            "pool_pre_ping": pool_pre_ping,
            "pool_recycle": pool_recycle,
            "pool_timeout": pool_timeout
        }
        parse = urlparse(self.connection_string)
        if parse.hostname and parse.hostname not in {"localhost","127.0.0.1"}:
            self._connection_args.setdefault("sslmode","require")

    def get_engine(self):
        if self._engine is None:
            self._engine = create_engine(self.connection_string,connect_args=self._connection_args,**self._pool_configs)
        return self._engine

    def test_connection(self):
        try:
            with self.get_engine().connect() as conn:
                conn.execute(text("SELECT 1"))
                # logger.info
            logger.info("Connected to database successful")
        except Exception as e:
            logger.error(f"Connected to database failed: {e}")      

    def dispose(self):
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None
            logger.info("Database engine dispose")

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.dispose()