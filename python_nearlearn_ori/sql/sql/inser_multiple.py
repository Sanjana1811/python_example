
# Lets create a DB 
import  sqlite3

DB = 'nearlearn.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()

# insert  Multiple values values into DB 

values = [('Sanjana' ,23 ,'sanjana@gmail.com','Machine Learning'),
          ('Rakesh' ,27 ,'rake@gmail.com', 'Python'),
          ('Pratik' ,23 ,'prtk@gmail.com','Deeplearning'),
          ('Snadhya' ,25,'sdy@yahoo.com','DeepLearning'),
          ('Vistmita',22,'Vis@yahoo.com','MachineLearning')]

cursor.executemany('''
              INSERT INTO students(name,age,email,course)
              VALUES( ? ,? ,? ,?)
              ''' ,values)


# commmit  the changes
conn.commit()
print("INSERTED MULTIPLE VALUES..... \n")
# print the Data 
cursor.execute("SELECT * FROM students")
data = cursor.fetchall()

for row in data:
    print(row)