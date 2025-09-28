import os
import configparser

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'Configuration', 'config.ini')
config.read(config_path)


class ReadConfig():
    @staticmethod
    def getApplicationURL():
       url =  config.get('Common info','base_url')
       return url

    @staticmethod
    def getemail():
        email = config.get('Common info', 'email')
        return email

    @staticmethod
    def getpassword ():
       password =  config.get('Common info','password')
       return password