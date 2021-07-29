from . import Item


class MadMan(Item):
    def __init__(self):
        self.name = "Mad Man"
        self.droppable = False
        self.text = "Madman - Gain 2 Might and lose 1 Sanity now. Lose 2 Might and gain 1 Sanity if you lose custody of the Madman. This omen can't be dropped, traded, or stolen."

    def on_acquire(self, player):
        player.raise_stat('might', 2)
        player.lower_stat('sanity', 1)

    def on_lose(self, player):
        player.lower_stat('might', 2)
        player.raise_stat('sanity', 1)


class SpiritBoard(Item):
    def __init__(self):
        self.name = "Spirit Board"
        self.droppable = True
        self.text = "Spirit Board - Before you move during your turn, you can look at the top tile of the room stack. If you use the Spirit Board after the haunt has been revealed, the traitor can move any number of monsters 1 space closer to you (if you are the traitor, you don't have to move those monsters). If there is no traitor, all monsters move 1 space closer to you."

    def on_use(self, player):
        pass


class Book(Item):
    def __init__(self):
        self.name = "Book"
        self.droppable = True
        self.text = "Book - Gain 2 Knowledge now. Lose 2 Knowledge if you lose the Book."

    def on_acquire(self, player):
        player.raise_stat('knowledge', 2)

    def on_lose(self, player):
        player.lower_stat('knowledge', 2)


class Skull(Item):
    def __init__(self):
        self.name = "Skull"
        self.droppable = True
        self.text = "If you take mental damage, you can take all of it as physical damage instead."

    def on_use(self, player):
        pass


class Spear(Item):
    def __init__(self):
        self.name = "Spear"
        self.droppable = True
        self.text = "Spear - You roll 2 additional dice (maximum 8) when making a Might attack with this weapon. You cannot use anothe weapon while you're using this one."

    def on_use(self, player):
        pass


class Medallion(Item):
    def __init__(self):
        self.name = "Medallion"
        self.droppable = True
        self.text = "Medallion - You are immune to the effects of the Pentagram Chamber, Crypt, and Graveyard."

    def on_use(self, player):
        pass


class CrystalBall(Item):
    def __init__(self):
        self.name = "Crystal Ball"
        self.droppable = True
        self.used = 0
        self.text = "Crystal Ball - Once during your turn after the haunt is revealed, you can attempt a Knowledge roll to peer into the Crystal Ball: 4+: You see the truth. Search the item or event stack for a card of your choice. Shuffle that stack. Then place that card on top. 1-3: You avert your eyes. lose 1 Sanity. 0: You stare into Hell. Lose 2 Sanity."

    def on_use(self, player):
        if self.used == 1:
            print("You already used that this turn!")
        else:
            pass
