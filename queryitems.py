import sys
from dbmysql import Mysql
from loghandle import LogHandle

loghandle = LogHandle("QueryItems", "./logs/wechat.log")

class QueryItems():
    def __init__(self):
        self.__dbhandle = Mysql()

    def query(self, word):
        sqlstr = "SELECT * FROM items_info WHERE title LIKE \"%"+word+"%\" limit 1"
        loghandle.write_log("sql:"+sqlstr)
        loghandle.write_log("safsaf1")
        res = self.__dbhandle.query(sqlstr)
        loghandle.write_log("safsaf2")
        if len(res) == 0:
            return None
        return res[0]

    def query_iid(self, iid):
        sqlstr = "SELECT * FROM items_info WHERE iid="+str(iid)
        res = self.__dbhandle.query(sqlstr)
        if len(res) == 0:
            return None
        return res[0]

