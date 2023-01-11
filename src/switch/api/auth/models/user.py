from switch.base.switch_object import SwitchObject

class User(SwitchObject):
    def __init__(self, user_name:str, id=None, **kwargs):
        self.__dict__.update(kwargs)
        self.id = id
        self.username = user_name


