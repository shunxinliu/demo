import sys
import unittest
import yaml
import json
import requests
sys.path.append('../')
from conf import globalvar as gl
from log.loggers import UserLog

yml = open(r'./conf/conf.yml',encoding='utf-8')
content = yaml.load(yml, Loader=yaml.FullLoader)


class TestCheckPhoto(unittest.TestCase):
    def test_checkphoto(self):
        f = open(r'./conf/photo.txt', encoding='utf-8')
        photo = f.read()
        url = content['host']+'/portal/forward?service=ecard/v1/sign/check/photo'
        data = {"channelNo":content['channelNo'],"aab301":gl.get_value('aab301'),"aac002":content['aac002'],"aac003":content['aac003'],"signSeq":gl.get_value('signSeq'),"aac201":photo,"aae586":'jpg'}
        res = requests.post(url=url,data=json.dumps(data),headers=gl.get_value('headers'))
        self.assertIn('成功', res.text,msg='实人认证失败')
        userlog = UserLog()
        loger = userlog.get_log()
        loger.info(url)
        loger.info(data)
        loger.info(res.text)
        userlog.close_handle()
        f.close()





