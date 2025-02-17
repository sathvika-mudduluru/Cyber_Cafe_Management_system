import mysql.connector as sql
conn = sql.connect(host ='localhost',user ='root',password ='',database ='ccms')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
print("                             ****************AMARAVIAN CYBER CAFE WELCOMES YOU****************        ")
print("                                               CYBER CAFE MANAGEMENT SYSTEM            ")
print("1.Customer details")
print("2.Time Charges")
print("3.Bill")
print("4.Customers detail view")
print("5.Quit")
a=int(input("Enter your choice :"))
if a==1:
    name=input("Enter your name :")
    age=int(input("Enter your age :"))
    address=input("Enter your residential address :")
    phone_no=int(input("Enter your phone number :"))
    email_id=input("Enter your Email ID :")
    ty="insert into Add_new_customer values('{}',{},'{}',{},'{}')".format(name,age,address,phone_no,email_id)
    c1.execute(ty)
    conn.commit()    
    print("                                                THANK YOU VISIT AGAIN               ")
if a==2:
    time=input("Enter the time :") 
    amount=int(input("Enter the amount :"))
    ss="insert into Time_charges values('{}',{})".format(time,amount)
    c1.execute(ss)
    conn.commit()
    print("                                                THANK YOU VISIT AGAIN               ")
if a==3:
    name=input("Enter your name :")
    time=int(input("Enter the time you accessed cyber cafe in minutes :"))
    total=time*30
    qw="insert into Bill values('{}',{},{})".format(name,time,total)
    c1.execute(qw)
    conn.commit()
    print("Please pay Rs.",total)
    print("Type YES to pay your bill or NO to pay it later")
    b=input("Type YES or NO:")
    if b=="YES":
        print("Bill paid successfully")
        print("                                            THANK YOU VISIT AGAIN               ")
    else:
        print("Bill not paid,pay the bill to leave the place")
if a==4:
    phone_no=input("Enter the phone number of the customer you want to search :")
    ea="select * from Add_new_customer where Phone_no=" + str(phone_no)
    c1.execute(ea)
    data=c1.fetchall()
    for row in data:
        print("Name:",row[0])
        print("Age:",row[1])
        print("Address:",row[2])
        print("Phone number:",row[3])
        print("Email ID",row[4])
    print("                                                THANK YOU VISIT AGAIN               ")
if a==5:
    print("                                                THANK YOU VISIT AGAIN               ")



    
