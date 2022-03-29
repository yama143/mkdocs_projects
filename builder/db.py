# db.py


from sqlmodel import create_engine, SQLModel
# import models as models
from db_config import DbConfig

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
configuration = DbConfig()
postgres_url = configuration.config_postgres()

engine = create_engine(postgres_url, echo=False)

print(engine)