class MsgType(type):

    def __init__(self, *args, **kwargs):
        super(MsgType, self).__init__(*args, **kwargs)

    def __call__(self, action, *args, **kwargs):
        action = self.action_check(action)

        return super().__call__(action, *args, **kwargs)

    def action_check(cls, action):
        if len(action) > 15:
            return action[:15]
        return action
