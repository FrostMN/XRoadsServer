class Utility(object):

    _name: str

    @property
    def name(self):
        return self._name


class AblativePlating(Utility):

    _name = "Ablative Plating"
