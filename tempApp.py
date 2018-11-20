import urllib
import time
import sqlite3
import random

db_file = "tempData.db"
url_temp01 = "http://172.16.42.8/"

# function to connect to database, grab value from Arduino site, then store in database
# CREATE TABLE temps (id INTEGER PRIMARY KEY AUTOINCREMENT, datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, temp NUMERIC NOT NULL, preheat INTEGER NOT NULL);
def create_connection(temp, preheat):
    try:
        conn = sqlite3.connect(db_file)

        curs =  conn.cursor()

        curs.execute("BEGIN;")
        curs.execute("INSERT INTO temps (temp, preheat) VALUES (?, ?);", (temp, preheat))
        curs.execute("COMMIT;")

        conn.close()
    except:
        pass

    return None

def main():
    for i in range(5):
        rand = random.randint(1,300)
        create_connection(rand, 23)
        print(str(rand+.1) + " : " + "23")
        time.sleep(2)
        
main()
