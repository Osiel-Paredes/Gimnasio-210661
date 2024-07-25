from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql://avnadmin:AVNS_D2HR6XHDev6O6yrXXo-@mysql-d6cd71-oosielparedes-ca5d.l.aivencloud.com:13585/defaultdb'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@localhost:3307/test'  #Conexión local

#  Conexión local
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
