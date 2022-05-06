import json

from utility.jim_settings.resp_type import RespType


class RespObj(metaclass=RespType):

    def __init__(self, response, alert):
        self.response = response
        self.alert = alert

    def __call__(self):
        resp_obj = {
            "response": self.response,
            "alert": self.alert
        }
        bytes = json.dumps(resp_obj).encode('utf-8')
        return bytes

#
# r1 = RespObj()
# r2 = RespObj("226",[(1,2),(1,2)])
# r2()
# print(json.loads(r1().decode('utf-8')))
# print(r2())
