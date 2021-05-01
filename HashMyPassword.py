import sqlite3
import hashlib
import os


class HashMyPassword:
    def connectToDB(self, dbfile):
        conn = None
        try:
            conn = sqlite3.connect(dbfile)
        except:
            print("Connect error")
        return conn

    def createUser(self, connection, user):
        user = '"%s"' % user
        cmd = "INSERT INTO hashpasswd (username) VALUES "+"("+user+")"
        try:
            connection.execute(cmd)
        except:
            print("Error in creating the user %s " %(user))
        finally:
            connection.commit()

    def createPasswd(self, connection, passwd, user):
        user = '"%s"' % user
        salt = os.urandom(32)
        passwd = str(hashlib.pbkdf2_hmac('sha256', passwd.encode('utf-8'), salt, 100000))
        passwd = '"%s"' % passwd
        cmd = "update hashpasswd set key="+passwd+" "+"where username="+user
        try:
            connection.execute(cmd)
        except:
            print("Error in creating password for the user %s " %(user))
        finally:
            connection.commit()
        salt = '"%s"' % salt
        cmdsalt = "INSERT INTO saltable (username, salt) VALUES " + "(" + user + ", " + salt + ")"
        try:
            connection.execute(cmdsalt)
        except:
            print("Error in updating salt")
        finally:
            connection.commit()



if __name__ == '__main__':
    dbfile = 'D:\sqlite\security.db'
    sql = HashMyPassword()
    conn = sql.connectToDB(dbfile)
    username = str(input("Enter username to create: "))
    sql.createUser(conn, username.strip())
    password = str(input("Enter password for user: "))
    sql.createPasswd(conn, password, username)