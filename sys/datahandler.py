import os
import sqlite3



def checkExistingDatabase():
    #Check if the required Database exists

    if os.path.isfile("../data/database.db") == True:

        connect = sqlite3.connect("../data/database.db")
        cursor = connect.cursor()


        print("Database is existing")
        print("Now Checking Database integrity")

        try:
            sql = "SELECT name, location, char, client, deadline, items, reward, description, details, status FROM quests"
            cursor.execute(sql)

            try:
                sql = "SELECT char, notes, design FROM misc"
                cursor.execute(sql)

                try:
                    sql = "SELECT name, age, gild, status, job, religion, rpitems, story, alive FROM characters"
                    cursor.execute(sql)
                    print("All Tables seem to be fine")
                except:
                    print("The Tabel Chars seems to be damaged")


            except:
                print("The Tabel Misc seems to be damaged")


        except:
            print("The Tabel Quests seems to be damaged")







        return

    #If not, create one
    else:

        connect = sqlite3.connect("../data/database.db")
        cursor = connect.cursor()

        #Create a Table for the Characters
        #Alive Code: 0 alive, 1 dead
        cursor.execute("""CREATE TABLE characters(
                        name TEXT, age TEXT, gild TEXT, status TEXT, job TEXT, religion TEXT, rpitems TEXT, story TEXT, alive INTEGER)""")
        #Create a Table for the Quests

        #Status Codes: 0 unsolved, 1 done, 2 failed
        cursor.execute("""CREATE TABLE quests(
                        name TEXT, location TEXT, char TEXT, client TEXT, deadline TEXT, items TEXT, reward TEXT, description TEXT, details TEXT, status INTEGER)""")

        cursor.execute("""CREATE TABLE locations(
                        name TEXT, char TEXT)""")

        #Create a Table for Notes and Design config
        cursor.execute("""CREATE TABLE misc(
                        char TEXT, notes TEXT, design TEXT)""")
        connect.commit()
        print("Database was created")

    return

