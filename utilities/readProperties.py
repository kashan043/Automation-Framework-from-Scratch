import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../Configurations/config.ini"))


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password


