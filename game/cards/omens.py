from . import Item, CardRegistry
from .. import game_actions as ga

name = CardRegistry()


@name("Book")
class Book(Item):
    def on_acquire(self, player):
        player.items.append(self)
        player.change_stat('knowledge', 2)

    def on_lose(self, player):
        player.change_stat('knowledge', -2)


@name("Bite")
class Bite(Item):
    def on_acquire(self, player):
        player.items.append(self)

        might_attack = ga.roll_dice(4)

        might_defend = ga.stat_roll(player, 'might')

        if might_attack - might_defend <= 0:
            pass
        else:
            player.change_stat('might', -(might_attack - might_defend))


@name("Crystal Ball")
class CrystalBall(Item):
    def on_acquire(self, player):
        player.items.append(self)
        self.used = 0

    def on_use(self, player):
        if self.used == 1:
            print("You already used that this turn!")
        else:
            know_roll = ga.stat_roll(player, 'knowledge')

            if know_roll >= 4:
                pass
            elif know_roll == 0:
                player.change_stat('sanity', -2)
            else:
                player.change_stat('sanity', -1)

    def on_lose(self, player):
        player.items.remove(self)


@name("Dog")
class Dog(Item):
    def on_acquire(self, player):
        player.items.append(self)
        self.dog_pos = player.pos
        self.dog_speed = 6
        self.used = 0

    def on_use(self, player):
        if self.used == 1:
            print("You already used the dog this turn!")
        else:
            # TODO: add ability to move the dog
            player.items.remove(self)


@name("Girl")
class Girl(Item):
    def on_acquire(self, player):
        player.items.append(self)
        player.change_stat('sanity', 1)
        player.change_stat('knowledge', 1)

    def losable(self, player):
        player.change_stat('sanity', -1)
        player.change_stat('knowledge', -1)
        player.items.remove(self)


@name("Holy Symbol")
class HolySymbol(Item):
    def on_acquire(self, player):
        player.items.append(self)
        player.change_stat('sanity', 2)

    def on_lose(self, player):
        player.change_stat('sanity', -2)


@name("Madman")
class Madman(Item):
    def on_acquire(self, player):
        player.items.append(self)
        player.change_stat('might', 2)
        player.change_stat('sanity', -1)

    def losable(self, player):
        player.change_stat('might', -2)
        player.change_stat('sanity', 1)
        player.items.remove(self)


@name("Mask")
class Mask(Item):
    def on_acquire(self, player):
        player.items.append(self)
        self.wearing = 0

    def on_use(self, player):
        san_roll = ga.stat_roll(player, 'sanity')

        if san_roll <= 3:
            print("You can't use the Mask this turn")
        else:
            if self.wearing == 0:
                self.wearing == 1
                player.change_stat('knowledge', 2)
                player.change_stat('sanity', -2)
            else:
                self.wearing == 0
                player.change_stat('knowledge', -2)
                player.change_stat('sanity', 2)

    def on_lose(self, player):
        player.items.remove(self)


@name("Medallion")
class Medallion(Item):
    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name("Ring")
class Ring(Item):
    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        sanity_roll = ga.stat_roll(player, 'sanity')

    def on_lose(self, player):
        player.items.remove(self)


@name("Skull")
class Skull(Item):
    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name("Spear")
class Spear(Item):
    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name("Spirit Board")
class SpiritBoard(Item):
    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)
