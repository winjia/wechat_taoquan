import tornado.web
from dbmysql import Mysql
from queryitems import QueryItems

dbhandle = Mysql()
queryhandle = QueryItems()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        iid = self.get_argument("iid", "")
        res = queryhandle.query_iid(iid)
        print(res)
        self.render("index.html", imgurl=res[15], title=res[2], coupons=res[9], price=res[7], reason=res[13], sale_num=res[10])
        #self.render("index.html")
