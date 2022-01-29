import pymysql

con = pymysql.connect(host = 'localhost', user = 'root', password = 'DieDieFBI!(()', db =  'sakila')

print('Connect sucsessful')

with con:

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))
