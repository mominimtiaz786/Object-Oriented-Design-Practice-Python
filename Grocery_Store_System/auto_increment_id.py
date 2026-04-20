class AutoIncrementId:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._count = 0

    def __init__(self):
        cls = type(self)
        self._id = cls._count
        cls._count += 1

    def getId(self):
        return self._id