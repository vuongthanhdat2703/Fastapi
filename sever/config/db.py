from sqlalchemy import create_engine, MetaData
engine= create_engine('mysql+pymysql://root:27032001@localhost:3306/customer')
meta = MetaData()
conn = engine.connect()