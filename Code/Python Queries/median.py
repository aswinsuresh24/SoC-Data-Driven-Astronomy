import psycopg2
import numpy as np

def column_stats(str1,str2):
  conn=psycopg2.connect(database='db', user='grok')
  cursor=conn.cursor()
  
  cursor.execute('SELECT %s FROM %s' %(str2,str1))
  records=cursor.fetchall()
  array=np.array(records)
  
  return (np.mean(array),np.median(array))