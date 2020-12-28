import mysql.connector as mcom


def db(val):
    try:
        conn = mcom.connect(host="localhost", user="root", password="", database=val)
        if conn:
            cursor = conn.cursor()
            x = input("Enter Table Name: ")
            sql = "CREATE TABLE " + x + "(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20), password VARCHAR(20))"
            try:
                cursor.execute(sql)
                print("Table Created Successfully")
            except:
                print("Already Exists")
            y = input("DO YOU WANT TO INSERT/DELETE/UPDATE/FIND/NOTHING: ")
            try:
                if y.upper() == 'INSERT':
                    val1 = input("Enter Username: ")
                    val2 = input("Enter Password: ")
                    sql = "INSERT INTO " + x + "(username, password) VALUES(%s, %s)"
                    value = (val1, val2)
                    cursor.execute(sql, value)
                    conn.commit()
                    print(cursor.rowcount, "Row Inserted")
                elif y.upper() == 'DELETE':
                    val1 = input("Enter Username: ")
                    val2 = input("Enter Password: ")
                    sql = "DELETE FROM " + x + " WHERE username = %s && password = %s"
                    value = val1, val2
                    cursor.execute(sql, value)
                    if cursor.rowcount == 0:
                        print("Please Enter Correct Username and Password")
                    else:
                        conn.commit()
                        print(cursor.rowcount, "Row Deleted")
                elif y.upper() == 'UPDATE':
                    val1 = input("Enter Username: ")
                    val2 = input("Enter new password : ")
                    sql = "UPDATE " + x + " SET password = %s WHERE username = %s"
                    value = val2, val1
                    cursor.execute(sql, value)
                    if cursor.rowcount == 0:
                        print("User name is Found")
                    else:
                        conn.commit()
                        print(cursor.rowcount, "Row Updated")
                elif y.upper() == 'FIND':
                    val1 = input("Enter Username: "),
                    sql = "Select * FROM " + x + " WHERE username = %s"
                    cursor.execute(sql, val1)
                    x = cursor.fetchall()
                    if x == []:
                        print("User Not Found")
                    else:
                        for i in x:
                            print(i)
                elif y.upper() == 'NOTHING':
                    print("ALRIGHT! THANK YOU. HAVE A NICE DAY")
                else:
                    print("ENTER ABOVE 5 OPTION ONLY.")
            except:
                print("ERROR! Please Enter Correct Information.")
    except ConnectionError:
        conn = mcom.connect(host="localhost", user="root", password="")
        if conn:
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            y = 'P'
            for i in cursor:
                if i[0] == val:
                    y = 'T'
            if y != 'T':
                print("Database not Found")
                x = input("Do you want to Create Database (Y or N): ")
                if x.upper() == 'Y':
                    sql = "CREATE DATABASE " + val
                    cursor.execute(sql)
                    print("Database Created Successfully")
                else:
                    print("Thank you. HAVE A NICE DAY")
        else:
            print("Connection Error")


val = input("Enter Database Name: ")
db(val)
