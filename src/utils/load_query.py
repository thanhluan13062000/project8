from jinja2 import Template
from pathlib import Path
from utils.logger import get_logger

logger = get_logger("load_query",log_to_file=False)


def load_query(sql_path,**kwargs):
    path = Path(sql_path)
    if not path.exists():
        logger.error("Could not find the sql file: %s",{sql_path})
        raise FileNotFoundError(f"Could not find the SQL file: {sql_path}")
    template = Template(path.read_text(encoding="utf-8"))
    rendered = template.render(**kwargs)
    logger.info("Rendered SQL from %s",sql_path)
    return rendered