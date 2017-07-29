import json
from base import Base

class SendOTP:

    def send(self, sendotp_values):
        values = {
            'authkey' : Base.authkey
        }
        values.update(sendotp_values)
        response = Base.call('sendotp.php', values)
        return response

    def retry(self, contactNumber, retrytype='voice'):
        values = {
            'authkey' : Base.authkey,
            'mobile' : contactNumber,
            'retrytype' : retrytype
        }
        response = Base.call('retryotp.php', values)
        return response

    def verify(self, mobile, otp):
        values = {
            'authkey' : Base.authkey,
            'mobile' : mobile,
            'otp' : otp
        }
        response = Base.call('verifyRequestOTP.php', values)
        return response