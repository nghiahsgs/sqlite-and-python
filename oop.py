import sqlite3
# conn = sqlite3.connect("user.db")
conn = sqlite3.connect(":memory:")
c = conn.cursor()

class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @property
    def email(self):
        return f"{self.first_name}@gmail.com"

        
        
if __name__ =='__main__':
    sql = 'CREATE TABLE user(firstName text,lastName text,age integer);'
    c.execute(sql)

    user1 = User(
        'nghia','nguyen',25
    )
    user2 = User(
        'nghia2','nguyen2',26
    )
    
    # insert to db
    with conn:
        c.execute("INSERT INTO user VALUES(:first_name,:last_name,:age);",{
            'first_name':user1.first_name,
            'last_name':user1.last_name,
            'age':25
        })
    # conn.close()

    # select
    with conn:
        c.execute("SELECT * FROM user;")
        result = c.fetchall()
        print(result)
    conn.close()