import sqlite3
import uuid

conn = sqlite3.connect('db.sqlite3')


c = conn.cursor()

tables = 'fabricaNode_area'

def randomName (n):
    return [(str(uuid.uuid4()),) for _ in range(n)]

names = randomName(10)

print(names)

for name in names:
    c.execute(f'''
        INSERT INTO {tables} (nome) VALUES (?)
    ''', name)

conn.commit()

conn.close()

print('Done!')