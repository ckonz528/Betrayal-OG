from . import Item


class Book(Item):
    def __init__(self):
        self.name = "Book"
        self.droppable = True

    def on_acquire(self, player):
        player.raise_stat('knowledge', 2)

    def on_lose(self, player):
        player.lower_stat('knowledge', 2)
