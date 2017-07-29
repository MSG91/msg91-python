import json
import requests
from message import Message
from phonebook import Phonebook
from reseller import Reseller
from virtual_number import VirtualNumber
from sendotp import SendOTP
from base import Base

class Msg91(Message, Phonebook, VirtualNumber, SendOTP):

    message = Message()
    phonebook = Phonebook()
    reseller = Reseller()
    virtual_number = VirtualNumber()
    sendotp = SendOTP()

    def __init__(self, key):

        Base.authkey = key
    
    def route_balance(self, bal_route):
        values = {
            'authkey' : Base.authkey,
            'type' : bal_route
        }
        response = Base.call('balance.php', values)
        return response.strip('\n')

    def validate(self):
        values = {
            'authkey' : Base.authkey,
            'response' : 'json'
        }
        response = Base.call('validate.php', values)
        return response
