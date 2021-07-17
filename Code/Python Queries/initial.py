import psycopg2

def select_all(str):
  conn=psycopg2.connect(dbname='db', user='py')
  cursor=conn.cursor()
              
  cursor.execute('SELECT * FROM %s;' %str)
  records=cursor.fetchall()
                        
  return(records)