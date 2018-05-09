import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    def __init__(self, loggername):
        logger = logging.getLogger(loggername)
        logger.setLevel(logging.INFO)
        df = '%Y-%m-%d %H:%M:%S'
        formatstr = '[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s'
        formatter = logging.Formatter(formatstr, df)
        try:
            handler = TimedRotatingFileHandler('/usr/web_wx/log/all.log', when='D', interval=1, backupCount=7)
        except Exception:
            handler = TimedRotatingFileHandler('F:\program\web_wx\core\log\/all.log', when='D', interval=1, backupCount=7)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        try:
            handler2 = TimedRotatingFileHandler('/usr/web_wx/log/error.log', when='D', interval=1, backupCount=7)
        except Exception:
            handler2 = TimedRotatingFileHandler('F:\program\web_wx\core\log\error.log', when='D', interval=1, backupCount=7)
        handler2.setFormatter(formatter)
        handler2.setLevel(logging.ERROR)
        logger1.addHandler(handler2)
        # console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # 设置日志打印格式
        console.setFormatter(formatter)
        # 将定义好的console日志handler添加到root logger
        logger1.addHandler(console)



if __name__=="__main__":
    pass
