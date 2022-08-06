
import sqlite3 as sql
import aiosqlite
from discord import Guild, Member, Message, TextChannel, User
import os

databaselocation = ""

def filesetup(path) -> str:
    """
    Makes the database and paths if they don't exist the folders and path will be made. Then sets up the database. with data
    """
    print("Setting up files...")
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        open(path + "/Leverling.db", "x")
        print(f"File has been made successfully at the path: {path} /Leverling.db" )
        try: 
            print("Setting up database...")
            db = sql.connect(path + "/Leverling.db")
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS leveling(GuildID INTEGER, UserID INTEGER, UserName TEXT, UserXP INTERGER)")
            db.commit()
            db.close()
            print("Database has been set up successfully.")
        except:
            print("Filemade but set up failed")
    except FileExistsError as e:
        return e

def declaredatabase(path) -> str:
    """declare the locations of the database file"""
    global databaselocation
    databaselocation = path + "/Leverling.db"
    return databaselocation

    
    
    

    