class RespType(type):

    def __init__(self, *args, **kwargs):
        super(RespType, self).__init__(*args, **kwargs)

    def __call__(self, resp=200, alert='OK'):
        resp = self.resp_check(resp)

        return super().__call__(resp, alert)

    def resp_check(cls, resp):
        try:
            if len(str(resp)) != 3:
                raise Exception('Число должно быть 3-x значным')
            resp = int(resp)
            return resp
        except ValueError:
            raise Exception("Аргумент должен быть типа int")
