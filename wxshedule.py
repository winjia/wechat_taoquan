import os
import tornado.ioloop
import requests
import json
from loghandle import LogHandle
import config

loghandle = LogHandle("WxShedule", "./logs/wechat.log")

class WxShedule(object):
    def __init__(self):
        self.__expiretime = 7000*1000
        self.path = "./token.json"

    def excute(self):
        loghandle.write_log("[获取微信全局唯一票据access_token]>>>执行定时器任务")
        tornado.ioloop.IOLoop.instance().call_later(0, self.get_access_token)
        tornado.ioloop.PeriodicCallback(self.get_access_token, self.__expiretime).start()

    def get_access_token(self):
        """获取微信全局唯一票据access_token"""
        url = config.ACESSTOKEN_URL
        r = requests.get(url)
        loghandle.write_log("[获取微信全局唯一票据access_token] Response[" + str(r.status_code) + "]")
        if r.status_code == 200:
            res = r.text
            loghandle.write_log("[获取微信全局唯一票据access_token] >>>" + res)
            d = json.loads(res)
            if "access_token" in d.keys():
                access_token = d["access_token"]
                self.__set_access_token(access_token)
                # 获取JS_SDK权限签名的jsapi_ticket
                #self.get_jsapi_ticket()
                return access_token
            elif 'errcode' in d.keys():
                errcode = d['errcode']
                loghandle.write_log(
                    "[获取微信全局唯一票据access_token-SDK] errcode[" + str(errcode) + "], will retry get_access_token() method after 10s")
                tornado.ioloop.IOLoop.instance().call_later(10, self.get_access_token)
        else:
            loghandle.write_log("[获取微信全局唯一票据access_token] request access_token error, will retry get_access_token() method after 10s")
            tornado.ioloop.IOLoop.instance().call_later(10, self.get_access_token)

    def load_access_token(self):
        if os.path.exists(self.path):
            pfile = open(self.path, "r")
            string = json.load(pfile)
            pfile.close()
            return string["access_token"]

    def __set_access_token(self, accesstoken):
        pfile = open(self.path, "w")
        print(type(accesstoken))
        #json.dump(json.dumps({"access_token":accesstoken}), pfile)
        json.dump({"access_token":str(accesstoken)}, pfile)
        pfile.close()
