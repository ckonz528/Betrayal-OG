class Item:
    def __init__(self):
        self.name = None

    def on_acquire(self, player):
        raise NotImplemented

    def on_use(self, player):
        raise Exception(f'{self.name} is not a usable item!')

    def on_lose(self, player):
        raise Exception(f'{self.name} cannot be dropped, traded, or stolen')
