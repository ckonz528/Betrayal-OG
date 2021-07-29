from . import Item, name


@name("boobs")
class Book(Item):
    def on_acquire(self, player):
        print('lowering knowledge by 2')
        # player.raise_stat('knowledge', 2)

    def on_lose(self, player):
        player.lower_stat('knowledge', 2)
