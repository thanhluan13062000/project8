import os
from pathlib import Path

LOCAL_ROOT = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(os.getenv("PROJECT_ROOT") or LOCAL_ROOT)

ingest_data = ROOT_DIR/"sql"/"oltp_ingest.sql"
dw_init_path = ROOT_DIR/"sql"/"dw_init.sql"
insert_jsonb = ROOT_DIR/"sql"/"insert_jsonb.sql"