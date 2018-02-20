
import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""SELECT * FROM characters""")
tmp = cursor.fetchall()

cursor.execute("""SELECT * FROM quests""")
tmp2 = cursor.fetchall()

cursor.execute("""SELECT * FROM locations""")
tmp3 = cursor.fetchall()

cursor.execute("""SELECT * FROM misc""")
tmp4 = cursor.fetchall()


connection.close()

print("characters:\n" + str(tmp))

print("quests:\n" + str(tmp2))

print("locations:\n" + str(tmp3))

print("misc:\n" + str(tmp4))

