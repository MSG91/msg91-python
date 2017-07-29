import json
from base import Base

class Reseller:

    def add_client(self, add_client_values):
        default_values = {
            'authkey' : Base.authkey
        }
        values = {}
        values.update(default_values)
        values.update(add_client_values)
        response = Base.call('add_client.php', values)
        return response

    def client_list(self):
        values = {
            'authkey' : Base.authkey
        }
        response = Base.call('client_list.php', values)
        return response

    def transfer_credit(self, transfer_credit_values):
        default_values = {
            'authkey' : Base.authkey
        }
        values = {}
        values.update(default_values)
        values.update(transfer_credit_values)
        response = Base.call('transfer_credit.php', values)
        return response
        
    def manage_client(self, client_id, status):
        values = {
            'authkey' : Base.authkey,
            'client_id' : client_id,
            'status' : status
        }
        response = Base.call('manage_client.php', values)
        return response

    def forgetpassword(self, client_name):
        values = {
            'authkey' : Base.authkey,
            'client_name' : client_name
        }
        response = Base.call('api_forgetpassword.php', values)
        return response

    def profile(self):
        values = {
            'authkey' : Base.authkey
        }
        response = Base.call('profile.php', values)
        return response

    def getexpiry(self):
        values = {
            'authkey' : Base.authkey
        }
        response = Base.call('getexpiry.php', values)
        return response

    def client_profile (self, client_id):
        values = {
            'authkey' : Base.authkey,
            'client_id' : client_id
        }
        response = Base.call('client_profile.php', values)
        return response

    def change_client_password (self, client_username, client_password):
        values = {
            'authkey' : Base.authkey,
            'clientUsername' : client_username,
            'clientPassword' : client_password
        }
        response = Base.call('ChangePassByReseller.php', values)
        return response

    def credit_history (self):
        values = {
            'authkey' : Base.authkey
        }
        response = Base.call('credit_history.php', values)
        return response