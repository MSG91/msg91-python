import json
import requests

class Base():

    baseUrl = "http://control.msg91.com/api/"
    authkey = ''
    
    @staticmethod
    def actionURLBuilder(actionurl):
        return Base.baseUrl + str(actionurl)

    @staticmethod
    def call(actionurl, args):
        url = Base.actionURLBuilder(actionurl)
        payload = (args)
        response = requests.post(url, data=payload, verify=False)
        return response.text