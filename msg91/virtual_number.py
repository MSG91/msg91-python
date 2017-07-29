import json
from base import Base

class VirtualNumber:

    def balance(self, v_type):
        values = {
            'authkey' : Base.authkey,
            'type' : v_type
        }
        response = Base.call('longcodeBalance.php', values)
        return response