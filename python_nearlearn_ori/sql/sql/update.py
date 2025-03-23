# Lets create a DB 
import  sqlite3

DB = 'nearlearn.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()


# update the data base 
cursor.execute('''
               UPDATE students
               SET age = 26 ,course = 'Machine Learning'
               WHERE name = 'Rakesh'
               ''')


conn.commit()
print("UPDATES...... \n")

cursor.execute("SELECT * FROM students")
data = cursor.fetchall()
for row in  data:
    print(row)