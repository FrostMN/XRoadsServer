import json


class Utility(object):

    _name: str

    @property
    def name(self):
        return self._name

    def to_dict(self):
        item_dict = {"name": self._name}
        return item_dict


class AblativePlating(Utility):

    _name = "Ablative Plating"
