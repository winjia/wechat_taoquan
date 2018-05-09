import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

class LogHandle(object):
    def __init__(self, logname, logpath):
        self.logger = None
        if logname in Logger.manager.loggerDict:
            self.__get_logger(logname)
        else:
            self.__add_logger(logname, logpath)


    def __add_logger(self, logname, logpath):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.INFO)
        df = '%Y-%m-%d %H:%M:%S'
        formatstr = '[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s'
        formatter = logging.Formatter(formatstr, df)
        handler = TimedRotatingFileHandler(logpath, when='D', interval=1, backupCount=7)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)
        # console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def __get_logger(self, loggername):
        self.logger = logging.getLogger(loggername)

    def write_log(self, logstr):
        self.logger.info(logstr)


if __name__=="__main__":
    path = "./wechat.log"
    loghandl = LogHandle("test", path)
    loghandl.write_log("name")
    loghandl1 = LogHandle("test123", path)
    loghandl1.write_log("name123")

