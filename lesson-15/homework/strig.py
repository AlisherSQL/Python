1. Create a new database with a table named Roster that has three fields: Name,
 Species, and Age. The Name and Species columns should be text fields, and
 the Age column should be an integer field
import sqlite3

with sqlite3.connect('ALI3.db') as ddd:
    cursor=ddd.cursor()

    create_table="""create table Roster (ID int, name text, age int)"""
    cursor.execute(create_table)
    values="""insert into Roster values (23,'SDF',34) """
    cursor.execute(values)
    ddd.commit

2  Populate your new table with the following values

import sqlite3

with sqlite3.connect('BOSS.db') as b:
    cursor=b.cursor()

    create_table="""create table if not exists BBB (Name text, Species text, age int)"""
    cursor.execute(create_table)
    values=[('Benjamin Sisko','Human',40), ('Jadzia Dax','Trill', 300), ('Kira Nerys','Bajoran',29)]
    cursor.executemany('INSERT INTO BBB VALUES (?, ?, ?);', values)
    b.commit()


3.Update the Name of Jadzia Dax to be Ezri Dax
  import sqlite3
with sqlite3.connect('BOSS.db') as b:
    cursor=b.cursor()
    
    cursor.execute("""update BBB set name= 'Ezri Dax' where name ='Jadzia Dax'; """)
    b.commit















