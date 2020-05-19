import unittest
import yaml
import requests
import json
import logging
import sys
sys.path.append('../')
from conf import globalvar as gl
from log.loggers import UserLog
yml = open(r'.\conf\conf.yml',encoding='utf-8')
content = yaml.load(yml, Loader=yaml.FullLoader)


class TestSignInfo(unittest.TestCase):
    #实名认证
    def test_signinfo(self):
        userlog= UserLog()
        loger = userlog.get_log()
        #print(content['header'])
        headers = content['header']
        #print(type(headers))
        headers['X-TOKEN'] = gl.get_value("X-TOKEN")
        #print("headers:", headers)
        #print("add", gl.get_value('X-TOKEN'))
        url = content['host']+'/portal/forward?service=/ecard/v1/sign/info'
        data = {"channelNo":content['channelNo'],"aab301":"","aac002":content['aac002'],"aac003":content['aac003']}
        res = requests.post(url=url,data=json.dumps(data),headers=headers)
        #print("signinfo"+res.text)
        gl.set_value('aab301',json.loads(res.text)['result'][0]['aab301'])
        self.assertIn('成功', res.text, msg='实名认证失败')
        print("实名认证")
        loger.info(url)
        loger.info(data)
        loger.info("test"+res.text)
        userlog.close_handle()




