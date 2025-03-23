# Lets create a DB 
import  sqlite3

DB = 'nearlearn.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()


# lets Delete some values from DB 

cursor.execute('''
               DELETE FROM students WHERE id = ?''',(4,)
               )



conn.commit()
print("DELTE ALL THE VALUES....")
cursor.execute("SELECT * FROM students")
data = cursor.fetchall()
for row in  data:
    print(row)



