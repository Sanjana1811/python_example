
# Lets create a DB 
import  sqlite3

DB = 'nearlearn.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()

# creating a Table 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER ,
               email TEXT,
               course TEXT NOT NULL
            )
               ''')

# commmit  the changes
conn.commit()
conn.close()

print("DB CREATED SUCESSFULLY.......!")
