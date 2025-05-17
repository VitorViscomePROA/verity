from sqlalchemy import create_engine, text
import pandas as pd

DB_USER = "user"
DB_PASS = "password"
DB_NAME = "desafio"
DB_HOST = "localhost"
DB_PORT = "5432"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def executar_sql(query: str) -> pd.DataFrame:
    with engine.connect() as conn:
        return pd.read_sql_query(sql=text(query), con=conn)
