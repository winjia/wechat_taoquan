import tornado.web
from dbmysql import Mysql
from queryitems import QueryItems

class SassHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sass_page.html")
