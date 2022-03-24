import sqlalchemy
from sqlalchemy import create_engine
import os


# SQL Alchemy Version Check

print(sqlalchemy.__version__) # 1.4.27

# SQL Alchmey Engine Oluştur ve İlgili Veri Tabanına Bağla

# print(os.getcwd())

dbUrl = "sqlite+pysqlite:///" + os.getcwd() + "\\database\\test.db"

engine = create_engine(dbUrl, echo=True, future=True)  








