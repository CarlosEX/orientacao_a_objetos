from repositorio import Repositorio
from database import PostgresDB, MySql


db_conn_postgres = PostgresDB()
db_conn_mysql = MySql()
repo = Repositorio()

repo.insert(db_conn_postgres)
repo.insert(db_conn_mysql)

