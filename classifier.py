# Stores the hypotheses.

import shutil
import sqlite3
import os

database = './classifier.py'

def printTable(table):
    print('\n'.join(str(x) for x in table))

def get(c):
    c.execute("SELECT DISTINCT book FROM solutions")
    books = [x[0] for x in c.fetchall()]

def insert(values):
    c.execute("INSERT INTO unindexed VALUES(?,?,?,?)",(book,section,name,path))

conn = sqlite3.connect(database)
c = conn.cursor()

print("Sebastian Olsson's Indexer")
print("1. Index all")
print("2. Unindex section")
print("3. Unindex book")
#print("4. Unindex all")

options = {1 : index_all,
           2 : unindex_section,
           3 : unindex_book,
           4 : unindex_all
}

option = int(raw_input("Command?:"))

options[option](c)

conn.commit()
conn.close()
