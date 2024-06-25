import os
from sqlalchemy import create_engine,text

db_connection_string = os.environ['DATABASE_URL']
engine = create_engine(db_connection_string,pool_size=20, max_overflow=0)


def load_jobs_from_db():
   
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = []
      for row in result.all():
          jobs.append(row._asdict())
      return jobs


    
    


 

