import sqlalchemy
from sqlalchemy import create_engine,text
import os
from sqlalchemy.orm import Session,sessionmaker

dbUrl = "sqlite+pysqlite:///" + os.getcwd() + "\\database\\test.db"

engine = create_engine(dbUrl, echo=True, future=True)

Sessions = sessionmaker(engine)
session = Sessions()

query = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=4980)
result = session.execute(query)

for row in result:
    print(f"x: {row.x}  y: {row.y}")

session2 = Session(engine)

query = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=4980)
result = session2.execute(query)

for row in result:
    print(f"x: {row.x}  y: {row.y}")

