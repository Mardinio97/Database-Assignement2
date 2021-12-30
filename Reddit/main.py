import mysql.connector
import json
import sys
from Connect import cursor
from Connect import db
import datetime

# opening the commands file with all the needed attributes
file1 = open(str(sys.argv[4]), 'r')
Lines = file1.readlines()

dataFile = open(str(sys.argv[3]), 'r')

# Variables to use for the queries
SUBREDDIT_ID = Lines[0].strip()
SUBREDDIT = Lines[1].strip()
LINK_ID = Lines[2].strip()
PARENT_ID = Lines[3].strip()
ID = Lines[4].strip()
AUTHOR = Lines[5].strip()
SCORE = Lines[6].strip()
BODY = Lines[7].strip()
CREATED_UTC = Lines[8].strip()

index = 0
data = ''


def InsertLinkToDatabase(cursor, data):
    try:

        cursor.execute("INSERT IGNORE INTO reddit3.Link VALUES (%s,%s);",
                       (str(data[LINK_ID]), str(data[SUBREDDIT_ID])))
        db.commit()

        print("Link Record inserted successfully ")
    except mysql.connector.Error as error:
        print("Failed to insert record into Link table {}".format(error))


def InsertSubredditToDatabase(cursor, data):
    try:

        cursor.execute("INSERT IGNORE INTO reddit3.Subreddit VALUES (%s,%s);",
                       (str(data[SUBREDDIT_ID]), str(data[SUBREDDIT])))
        db.commit()

        print("Subreddit Record inserted successfully ")
    except mysql.connector.Error as error:
        print("Failed to insert record into Subreddit table {}".format(error))


def InsertCommentToDatabase(cursor, data):
    try:

        cursor.execute("INSERT IGNORE INTO reddit3.Comment VALUES (%s,%s,%s,%s,%s,%s,%s,%s);",
                       (str(data[ID]), str(data[AUTHOR]), str(data[SCORE]), str(data[BODY]),
                        str(data[SUBREDDIT_ID]), str(data[PARENT_ID]),
                        datetime.datetime.fromtimestamp(data[CREATED_UTC]),
                        str(data[LINK_ID])))
        db.commit()
        print("Comment Record inserted successfully ")
    except mysql.connector.Error as error:
        print("Failed to insert record into Comment table {}".format(error))


# Start time
start_time = datetime.datetime.now()

with dataFile as file:
    for data in file:
        try:
            index = index + 1
            data = json.loads(data)

            # Insert data from file to Subreddit table
            InsertSubredditToDatabase(cursor, data)

            # Insert data from file to Link table
            InsertLinkToDatabase(cursor, data)

            # Insert data from file to Comment table
            InsertCommentToDatabase(cursor, data)

            print(index, " ROWS INSERTED SUCCESSFULLY")
            print('------------------------------------------')


        except mysql.connector.Error as error:
            print("Failed to insert record into  table {}".format(error))

    # End time
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    # Total time
    execution_time = time_diff.total_seconds() * 1000
    print(execution_time)
