import unittest
import sys
sys.path.append('../')
import yaml
import requests
import json
from conf import globalvar as gl
from log.loggers import UserLog

yml = open(r'./conf/conf.yml',encoding='utf-8')
content = yaml.load(yml, Loader=yaml.FullLoader)

class TestSign(unittest.TestCase):
    def test_sign(self):
        url = content['host']+'/portal/forward?service=/ecard/v1/sign'
        data = {"channelNo":content['channelNo'],"aab301":gl.get_value('aab301'),"aac002":content['aac002'],"aac003":content['aac003'],"signSeq":gl.get_value('signSeq')}
        res = requests.post(url=url,data=json.dumps(data),headers=gl.get_value('headers'))
        gl.set_value("signNo",json.loads(res.text)['result']['signNo'])
        self.assertIn("成功",res.text,msg="一级签发失败")
        userlog = UserLog()
        loger = userlog.get_log()
        loger.info(url)
        loger.info(data)
        loger.info(res.text)
        userlog.close_handle()
