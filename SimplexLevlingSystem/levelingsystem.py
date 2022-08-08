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

async def givexp(amount , member) -> int:
    """Will connect and open database then award the user the give amout of xp"""
    try:
        async with aiosqlite.connect(databaselocation) as db:
            cursor = await db.execute("SELECT * FROM leveling WHERE GuildID = ? AND UserID = ?", (member.guild.id, member.id))
            result = await cursor.fetchone()
            if result is None:
                await db.execute("INSERT INTO leveling(GuildID, UserID, UserName, UserXP) VALUES(?, ?, ?, ?)", (member.guild.id, member.id, member.name, amount))
                await db.commit()
                return amount
            else:
                xp = result[3] + amount
                await db.execute("UPDATE leveling SET UserXP = ? WHERE GuildID = ? AND UserID = ?", (xp, member.guild.id, member.id))
                await db.commit()
                return xp
    except Exception as e:
        print(e)
        return e

async def getxp(member) -> int:
    """Will connect to the database and retreve the xp"""
    try:
        print("")
    except Exception as e:
        print(e)
        return e



        
    


    
    

    