import sqlite3

conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''CREATE table PARTS2 (id_part int, sku text, brand text)''')

cursor.execute('''INSERT INTO PARTS2 (id_part, sku, brand) values (5, "03530", "FEBI")''')
cursor.execute('''INSERT INTO PARTS2 (id_part, sku, brand) values (6, "03531", "FEBI")''')
cursor.execute('''INSERT INTO PARTS2 (id_part, sku, brand) values (7, "03532", "FEBI")''')
conn.commit()
cursor.close()