import logging
import os
import datetime
class UserLog(object):
    def __init__(self):
        #文件名称
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"/"+log_file


        self.logger = logging.getLogger(__name__)

         #文件输出日志
        #if not self.logger.handlers:
        self.logger.setLevel(level=logging.DEBUG)
        #self.file_handle = logging.StreamHandler()
        self.file_handle = logging.FileHandler(filename=log_name, encoding='utf-8')
        #self.file_handle = logging.FileHandler(log_name,'a',encoding='utf8')
        #self.file_handle.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


