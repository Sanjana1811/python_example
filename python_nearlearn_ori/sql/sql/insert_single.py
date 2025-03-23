
# Lets create a DB 
import  sqlite3

DB = 'nearlearn.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()

# insert  single values into DB 
cursor.execute('''
              INSERT INTO students(name,age,email,course)
              VALUES('Rusdresh',25,'rushresh@gmail.com','Machine Learning')
              ''')


# commmit  the changes
conn.commit()

# print the Data 
cursor.execute("SELECT * FROM students")
data = cursor.fetchone()
print(data)

# conn.close()

