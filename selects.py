import sqlalchemy
from sqlalchemy import create_engine,text
import os
from sqlalchemy.orm import Session,sessionmaker


# SQL Alchemy Version Check

print(sqlalchemy.__version__) # 1.4.27

# SQL Alchmey Engine Oluştur ve İlgili Veri Tabanına Bağla

# print(os.getcwd())

dbUrl = "sqlite+pysqlite:///" + os.getcwd() + "\\database\\test.db"

engine = create_engine(dbUrl, echo=True, future=True) 

conn = engine.connect()
queryAll = text("Select * from some_table")

result = conn.execute(queryAll)

dataList = result.all()

"""
# tuple olarak kullan

for x,y in dataList:
    print("x:{} y:{}".format(x,y))

# indexler ile Kullan

for row in dataList:
    print("x:{}, y:{}".format(row[0],row[1]))

# Kolon Adıyla Kullan

for row in dataList:
    print("x:{} y:{}".format(row.x,row.y))

# Mapping İle Kullan

for row in result.mappings():
    print("x:{} y:{}".format(row["x"],row["y"]))   """

# Parametre İle Select İşlemi

queryparams = text("SELECT x, y FROM some_table WHERE y > :y and x < :x")
result = conn.execute(queryparams,{"y" : 4900, "x" : 999})  
dataList = result.all()
for row in dataList:
    print("x:{} y:{}".format(row.x,row.y))

# BindParams ile Select


queryparams = text("SELECT x, y FROM some_table WHERE y > :y and x < :x").bindparams(x=999,y=4980)
result = conn.execute(queryparams)  
dataList = result.all()
for row in dataList:
    print("x:{} y:{}".format(row.x,row.y))

queryparams = text("SELECT x, y FROM some_table WHERE y > :y and x < :x order by x desc").bindparams(x=999,y=4980)
result = conn.execute(queryparams)  
dataList = result.all()
for row in dataList:
    print("x:{} y:{}".format(row.x,row.y))

