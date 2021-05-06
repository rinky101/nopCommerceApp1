import configparser

#rawconfigpraser is the class. using this method we can read data from ini fle
# and provide data to the testcase

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
       url = config.get('common data','baseURL')
       return url

    @staticmethod
    def getUseremail():
        username = config.get('common data', 'useremail')
        return username

    @staticmethod
    def getPassword():
        Password = config.get('common data', 'password')
        return Password
