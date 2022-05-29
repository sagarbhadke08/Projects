import mysql.connector as con


def conn(id,name,mobile,class_,div_,email_,password_):
    db = con.connect(host="127.0.0.1", port=3306, user="root", password="root", database="db_student_attendance" ,charset="utf8")
    cur=db.cursor()

    
    query="insert into tbl_student(id,name,mobile,class_,div_,email_,password_) values(%s,%s,%s,%s,%s,%s,%s)"
    value=[id,name,mobile,class_,div_,email_,password_]
    cur.execute(query,value)
    db.commit()
    #tkMessageBox.showinfo("Information", "Person Added Successfull")
    


def log(id):
    flag=str(id)
    db = con.connect(host="localhost", user="root", password="root", database="db_student_attendance" ,charset="utf8")
    cur = db.cursor()
    
    query="select * from tbl_student where id='"+flag+"'"
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return row[1]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no record'

def find_daily_entry(id):
    flag=str(id)
    db = con.connect(host="localhost", user="root", password="root", database="db_student_attendance" ,charset="utf8")
    cur = db.cursor()
    
    query="select date_ from tbl_attend where name='"+flag+"' ORDER BY id DESC LIMIT 1 "
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return row[0]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no'
def insert_attend(name,date_):
    db = con.connect(host="localhost", port=3306, user="root", password="root", database="db_student_attendance" ,charset="utf8")
    cur=db.cursor()

    
    query="insert into tbl_attend(name,date_) values(%s,%s)"
    value=[name,date_]
    cur.execute(query,value)
    db.commit()


def view_all_attendance(name):
    
    db = con.connect(host="localhost", user="root", password="root", database="db_student_attendance" ,charset="utf8")
    cur = db.cursor()
    
    query="SELECT count(id), name FROM tbl_attend where name='"+name+"'"
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return row[0]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no'

def delete(id):
    db = con.connect(host="localhost", port=3306, user="root", password="", database="db_accident" ,charset="utf8")
    cur=db.cursor()

    
    query="delete from  tbl_police where id="+str(id)
    
    cur.execute(query)
    db.commit()
