import os
import psycopg2
import json as simplejson
import collections
import datetime
import numpy as np
import math
from itertools import groupby
from operator import itemgetter
from configdatabase import connectionStringDatabase

class extractdata:
    def getconnection(self):

        #Define our connection string to heroku basic database
        if os.environ.get('ON_HEROKU'):
            conn_string = os.environ.get('DATABASE_URL')
        else :
            conn_string = connectionStringDatabase
        #connect
        try:
            conn = psycopg2.connect(conn_string)
        except psycopg2.Error as e:
            print ("Unable to connect!")
            print (e.pgerror)
            print (e.diag.message_detail)
        else:
            print ("Connected!")

        return conn

    def insert_data(self, tweet_time, tweet_text, tweet_country, tweet_keyword ):
        connection = self.getconnection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO tweets (created_at, text, country_code, keyword) \
        VALUES (%s, %s, %s, %s);""", \
        (tweet_time, tweet_text, tweet_country, tweet_keyword))
        cursor.execute('COMMIT;')




def __init__(self):
        print ("in init")
