"""
Created on Fri Aug 16 08:21:42 2019
Connect to vertica db
@author: ow
"""
import pyodbc
conn = pyodbc.connect(DSN="serverhostname", UID="login", PWD= "password")
conn.setencoding(encoding='utf-8')
cursor = conn.cursor()

line =cursor.execute("select * where date in ('01/01/2019', '02/02/2019')")

               
row = cursor.fetchall()
if row:
    print(row)               


conn.close()
