#from core.logger_helper import logger
import hashlib
import tornado.web
import os
import config
import xml.etree.ElementTree as ET
from loghandle import LogHandle 
import time
import template
import imagehandle as imghandle
from dbmysql import Mysql
from queryitems import QueryItems

dbhandle = Mysql()
queryhandle = QueryItems()

loghandle = LogHandle("MainHandler", "./logs/wechat.log")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            signature = self.get_argument('signature')
            timestamp = self.get_argument('timestamp')
            nonce = self.get_argument('nonce')
            echostr = self.get_argument('echostr')
            result = self.check_signature(signature, timestamp, nonce)
            if result:
                self.write(echostr)
                loghandle.write_log("微信sign校验,返回echostr="+echostr)
            else:
                loghandle.write_log("微信sign校验,校验失败")
        except Exception as e:
            loghandle.write_log("微信sign校验,---Exception"+str(e))

    def check_signature(self, signature, timestamp, nonce):
        token = config.WXTOKEN 
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        loghandle.write_log("sha1="+sha1+"&signature="+signature)
        return sha1 == signature

    def post(self):
        #render = web.template.render("./templates")
        body = self.request.body
        loghandle.write_log('[微信消息回复中心]收到用户消息:' + str(body))
        data = ET.fromstring(body)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        MsgType = data.find('MsgType').text
        if MsgType == "event":
            try:
                Event = data.find('Event').text

            except :
                pass
        elif MsgType == "text":
            content = data.find("Content").text
            loghandle.write_log('text-content:'+content)
            res = queryhandle.query(content)
            if res is None:
                out = template.TEXTTPL% (FromUserName, ToUserName, int(time.time()), 'text', "输入错误,请输入商品名称查询")
                loghandle.write_log('no replay')
                self.write(out)
                return
            url = "http://118.24.63.203:80?iid="+str(res[1])
            loghandle.write_log('replay url:'+url)
            itemtext = template.ITEM_TPL%(res[2], res[13], res[15], url)
            out = template.SINGLE_IMG_TEXT_TPL% (FromUserName, ToUserName, int(time.time()), 'news', '1', itemtext)
            self.write(out)
        elif MsgType == "image":
            picurl = data.find("PicUrl").text
            #mediaid = data.find("MediaId").text
            imghandle.download_image(picurl, config.IMAGEPATH+"/a.jpg")
            mediaid = imghandle.send_wx_image("")
            print(mediaid)
            out = template.IMAGETPL%(FromUserName,ToUserName, int(time.time()), mediaid)
            self.write(out)
        else:
            loghandle.write_log("No recognize msgtype!")


    def data_received(self, chunk):
        pass

