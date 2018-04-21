class Background(object):
    """ set generic modifiers """
    _name:      str = "Background"
    _aim:       int = 0
    _defence:   int = 0
    _dodge:     int = 0
    _will:      int = 0
    _hacking:   int = 0
    _health:    int = 0
    _mobility:  int = 0

    @property
    def name(self):
        return self._name

    @property
    def aim(self):
        return self._aim

    @property
    def defence(self):
        return self._defence

    @property
    def dodge(self):
        return self._dodge

    @property
    def will(self):
        return self._will

    @property
    def hacking(self):
        return self._hacking

    @property
    def health(self):
        return self._health

    @property
    def mobility(self):
        return self._mobility

    def __str__(self) -> str:
        return self._name


class Resistance(Background):
    def __init__(self):
        super().__init__()
        self._name = "Resistance"
        self._aim = 65
        self._defence = 0
        self._dodge = 5
        self._will = 95
        self._hacking = 5
        self._health = 4
        self._mobility = 5


class Scientist(Background):
    def __init__(self):
        super().__init__()
        self._name = "Scientist"
        self._aim = 60
        self._defence = 0
        self._dodge = 0
        self._will = 100
        self._hacking = 20
        self._health = 4
        self._mobility = 5


class Scavenger(Background):
    def __init__(self):
        super().__init__()
        self._name = "Scavenger"
        self._aim = 55
        self._defence = 10
        self._dodge = 10
        self._will = 90
        self._hacking = 5
        self._health = 3
        self._mobility = 6


class Hunter(Background):
    def __init__(self):
        super().__init__()
        self._name = "Hunter"
        self._aim = 75
        self._defence = 0
        self._dodge = 0
        self._will = 100
        self._hacking = 11
        self._health = 3
        self._mobility = 4


class Athlete(Background):
    def __init__(self):
        super().__init__()
        self._name = "Athlete"
        self._aim = 70
        self._defence = 5
        self._dodge = -10
        self._will = 80
        self._hacking = 1
        self._health = 5
        self._mobility = 5
