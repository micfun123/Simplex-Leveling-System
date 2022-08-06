from cgi import test
from logging import exception
import sqlite3 as sql
import aiosqlite
import asyncio
import os

def filesetup(path) -> str:
    """
    Makes the database and paths if they don't exist. Then sets up the database.
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