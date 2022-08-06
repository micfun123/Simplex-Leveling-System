import aiosqlite
import asyncio
import os

def filesetup(path):
    print("Setting up files...")
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        os.mknod(path/'leveling.db')
    except FileExistsError as e:
        return e

