import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myuni"
    
)
# Create → Insert new record

# Read → Show existing records

# Update → Change any field (jaise address, name)

# Delete → Remove record from table

mycursor=mydb.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255),
age INT,
address VARCHAR(255)
)
""")
#student management system
def add_students():
    name=input("enter your name")
    age=int(input("Enter your age"))
    address=input("Enter your address")
    sql="INSERT INTO students(name,age,address) VALUES(%s,%s,%s)"
    val=(name,age,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Students addeed succesfully!\n")

def show_students():
    mycursor.execute("SELECT * FROM students")
    results=mycursor.fetchall()
    print("\n show studnets ")
    for row in results:
        print(row)
        print()

def update_students():
    students_id=int(input("Enter your id to update for "))
    students_address=input("Enter new address")
    sql="UPDATE sudents SET address=%s WHERE id=%s"
    val=(students_address,students_id)
    mycursor.execute(sql,val)
    mydb.commit()
    print("UPDATED SUCCESSFULLY")

def delete_students():
    students_id=int(input("Enter id for update"))
    sql="DELETE FROM students where id=%s"
    val=(students_id,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("DELETED SUCCESSFULLY!\n")

#menu loop
while True:
    print(".........MENU........")
    print("1: ADD STUDENTS")
    print("2: SHOW STUDENTS")
    print("3: UPDATE STUDNETS")
    print("4: DELETE STUDNETS")
    print("5: EXIT STUDENTS")

    choice=input("ENTER YOU CHOICE (1-5)")
    if choice=="1":
        add_students()
    elif choice=="2":
        show_students()
    elif choice=="3":
        update_students()
    elif choice=="4":
        delete_students()
    elif choice=="5":
        print("EXITING")
    else:
        print("Invalid choice! \n")



    
         
