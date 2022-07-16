import sqlite3
conn = sqlite3.connect("user.db")

c = conn.cursor()


# sql = 'CREATE TABLE user(firstName text,lastName text,age integer);'
# c.execute(sql)

# INSERT COMMAND
# c.execute("INSERT INTO user VALUES('nguyen','nghia',20);")
# conn.commit()
# conn.close()

# with conn:
#     c.execute("INSERT INTO user VALUES('nguyen2','nghia2',20);")
# conn.close()



# SELECT COMMAND
# c.execute("SELECT * FROM user;")
# result = c.fetchall()
# print(result)

# c.execute("SELECT * FROM user;")
# result = c.fetchone()
# print(result)

# c.execute("SELECT * FROM user;")
# result = c.fetchmany(1)
# print(result)

# conn.close()