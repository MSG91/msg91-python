import json
from base import Base

class Phonebook:

    def add_group (self, group_name):
        values = {
            'authkey' : Base.authkey,
            'group_name' : group_name
        }
        response = Base.call('add_group.php', values)
        return response

    def delete_group (self, group_id):
        values = {
            'authkey' : Base.authkey,
            'group_id' : group_id
        }
        response = Base.call('delete_group.php', values)
        return response

    def list_group (self):
        values = {
            'authkey' : Base.authkey
        }
        response = Base.call('list_group.php', values)
        return response

    def add_contact (self, add_contact_values):
        default_values = {
            'authkey' : Base.authkey
        }
        values = {}
        values.update(default_values)
        values.update(add_contact_values)
        response = Base.call('add_contact.php', values)
        return response

    def edit_contact (self, edit_contact_values):
        default_values = {
            'authkey' : Base.authkey,
        }
        values = {}
        values.update(default_values)
        values.update(edit_contact_values)
        response = Base.call('edit_contact.php', values)
        return response

    def delete_contact (self, contact_id):
        values = {
            'authkey' : Base.authkey,
            'contact_id' : contact_id
        }
        response = Base.call('delete_contact.php', values)
        return response

    def list_contact (self, group):
        values = {
            'authkey' : Base.authkey,
            'group' : group
        }
        response = Base.call('list_contact.php', values)
        return response
