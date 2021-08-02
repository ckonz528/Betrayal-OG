class Item:
    def __init__(self, game_info):
        self.game_info = game_info

    def on_acquire(self, player):
        raise NotImplemented

    def on_use(self, player):
        raise Exception(f'{self.name} is not a usable item!')

    def on_lose(self, player):
        raise Exception(f'{self.name} cannot be dropped, traded, or stolen')

    def usable(self):
        try:
            self.on_use(None)
        except Exception as e:
            if 'not a usable item' in str(e):
                return False
            return True

    def losable(self):
        try:
            self.on_use(None)
        except Exception as e:
            if 'cannot be dropped' in str(e):
                return False
            return True


def name(n):
    def decorate(cls):
        old_init = cls.__init__

        def new_init(self, *args, **kwargs):
            self.name = n
            old_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorate
