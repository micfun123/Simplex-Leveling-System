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
    except FileExistsError as e:
        return e