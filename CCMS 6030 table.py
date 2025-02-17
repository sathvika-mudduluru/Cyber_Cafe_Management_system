import mysql.connector as sql
conn = sql.connect(host ='localhost',user ='root',password ='',database ='ccms')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
c1.execute('create table Add_new_customer(Customer_name varchar(20),Age int,Address varchar(100),Phone_no int(10),Email_ID varchar(30))')
c1.execute('create table Bill(Customer_name varchar(20),Time_accessed_in_min int,Total_charges int)')
c1.execute('create table Time_charges(Time varchar(30),Amount_charged int)')
print("Table created")
