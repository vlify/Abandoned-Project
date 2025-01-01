class AI(object):
    def __init__(self):
        super(AI, self).__init__()
        self.create()

    def create(self):
        print(self.__class__.__name__ + " ticked!...")

    @staticmethod
    def update():
        pass
