import json
import requests
from base import Base

route = 0
sender = ''

class Message:

    def set_route(self, new_route):
        global route
        route = new_route 

    def set_sender(self, new_sender):
        global sender
        sender = new_sender 

    def send (self, send_values):
        global sender
        global route
        default_value = {
            'authkey' : Base.authkey,
            'response' : 'json',
            'route' : route,
            'sender' : sender
        }

        values = {}
        values.update(default_value)
        values.update(send_values)

        response = Base.call('sendhttp.php', values)
        return response