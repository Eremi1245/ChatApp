import json
from time import time

from utility.const import ACTIONS
from utility.jim_settings.msg_type import MsgType


class MsgObj(metaclass=MsgType):

    def __init__(self, action, *args, **kwargs):
        self.action = action

        self.attr = {**kwargs}

    def __call__(self):
        jim_obj = {**self.attr}
        jim_obj["action"] = self.action
        jim_obj["time"] = time()
        bytes = json.dumps(jim_obj).encode('utf-8')
        return bytes

# j1 = MsgObj('здесь больше 15 символов', user={'hjij':"dsd"},mama='mama')
# j2 = MsgObj('15 символов')
#
# print(json.loads(j1().decode("utf-8")))
# print(j2())
