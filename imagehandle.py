import urllib
from urllib import request
import requests
import config
import os
import json

def load_access_token(path):
    if os.path.exists(path):
        pfile = open(path, "r")
        string = json.load(pfile)
        pfile.close()
        return string["access_token"]
    return None

def upload_image(filepath, accesstoken, mediatype):
    pfile = open(filepath, "rb")
    posturl = "https://api.weixin.qq.com/cgi-bin/media/upload"
    data = {"access_token":accesstoken, "type":mediatype}
    files = {'file':pfile}
    response = requests.post(posturl, data=data, files=files)
    print("========")
    print(type(response))
    print(response.json())
    pfile.close()
    jsonstr = response.json()
    return jsonstr["media_id"]

def send_wx_image(path):
    accesstoken = load_access_token(config.TOKEN_PATH)
    mediaid = upload_image("aa.png", accesstoken, "Image")
    return mediaid

def download_image(url, savepath):
    try:
        request.urlretrieve(url, savepath)
        return 0
    except Exception as e:
        print(str(e))
    return 1



if __name__=="__main__":
    pass
    #download_image("https://pic3.zhimg.com/80/v2-4ff2c8099ccf0b2d8eb963a0ac248296_hd1.jpg", "test.jpg")
