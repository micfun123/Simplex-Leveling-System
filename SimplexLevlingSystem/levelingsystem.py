import sqlite3 as sql
import aiosqlite
from discord import Guild, Member, Message, TextChannel, User
import os

databaselocation = None

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
    databaselocation = path
    print(f"Connected to {databaselocation} successfully")
    return databaselocation

def givexp(amount , member) -> int:
    """Will connect and open database then award the user the set amout of xp"""
    try:
        db = sql.connect(databaselocation)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM leveling WHERE GuildID = ? AND UserID = ? AND UserName = ?", (member.guild.id, member.id , member.name))
        data = cursor.fetchone()
        if data:
            cursor.execute("UPDATE leveling SET UserXP = UserXP + ? WHERE GuildID = ? AND UserID = ? AND UserName = ?", (amount, member.guild.id, member.id , member.name))
            db.commit()
        else:
            cursor.execute("INSERT INTO leveling(GuildID, UserID, UserName, UserXP) VALUES (?, ?, ?, ?)", (member.guild.id, member.id , member.name, amount))
            db.commit()
    except Exception as e:
        print(e)
        return e


        
    


    
    

    