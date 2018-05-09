import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from mainhandler import MainHandler
from indexhandler import IndexHandler
from wxshedule import WxShedule
import config


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug = False,
        )
        #super(Application, self).__init__(urlpatterns, **settings)
        super(Application, self).__init__([(r'/wx', MainHandler),(r'/', IndexHandler)], **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(80)
    #
    wx_shedule = WxShedule()
    wx_shedule.excute()
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

