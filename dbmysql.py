import pymysql
import time
from urllib import parse


class Mysql():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root',password='123123',database='taoqueqiao',use_unicode=True, charset="utf8")

    def re_connect(self):
    	try:
            self.conn.ping()
    	except:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root',password='123123',database='taoqueqiao',use_unicode=True, charset="utf8")

    def query(self,sqlstr):
        self.re_connect()
        cur = self.conn.cursor()
        result = []
        try:
            cur.execute(sqlstr)
            result = cur.fetchall()
        except:
            self.conn.rollback()
            print("query error!")
            raise
        finally:
            cur.close()
        return result


    def insert(self, sqlstr):
        self.re_connect()
        cur = self.conn.cursor()
        try:
            cur.execute(sqlstr)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("insert error!")
            raise
        finally:
            cur.close()

if __name__=="__main__":
    handle = Mysql()
    #handle.insert("insert into test_1 (id, iid, createtime) values (1, 12387877, %d)"%(time.time()))
    #handle.insert("insert into test_1 (iid, createtime) values (112387877, %d)"%(time.time()))
    #strs = "INSERT INTO items_image_url (iid, urls, createtime, updatetime) VALUES (528487067644,\"['https://img.alicdn.com/tfscom/i3/2836108396/TB20uIfdwNlpuFjy0FfXXX3CpXa_!!2836108396.jpg_440x440.jpg', 'https://img.alicdn.comtfscom/i4/2836108396/TB2RMUtdB8lpuFjSspaXXXJKpXa_!!2836108396.jpg_440x440.jpg', 'https://img.alicdn.com/tfscom/i4/2836108396TB2QjsCbHZnBKNjSZFhXXc.oXXa_!!2836108396.jpg_440x440.jpg', 'https://img.alicdn.com/tfscom/i3/2836108396/TB29Bx7XbaI.eBjSspaXXXIKpXa_!!2836108396.jpg_440x440.jpg', 'https://img.alicdn.com/tfscom/i3/2836108396/TB20uIfdwNlpuFjy0FfXXX3CpXa_!!2836108396.jpg_440x440.jpg']\",1524733411,1524733411)"
    #print(strs)
    #handle.insert(strs)
    sqlstr = "SELECT * FROM items_info WHERE title LIKE \"%xxx%\""#"SELECT * FROM items_info WHERE id=6"
    res = handle.query(sqlstr)
    print(res)
    print(len(res))

