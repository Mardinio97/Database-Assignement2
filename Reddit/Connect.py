import mysql.connector
import sys

db = mysql.connector.connect(host="localhost",
                             user='root',
                             passwd="Kkmm570047",
                             db='reddit3')
cursor = db.cursor()
