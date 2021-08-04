from . import Item, name
import game_actions as ga


@name('Adrenaline Shot')
class Adrenaline(Item):
    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Amulet of the Ages')
class Amulet(Item):
    '''Ancient silver and inlaid gems inscribed with blessings. Gain 1 Might, 1 Speed, 1 Knowledge and 1 Sanity now. Lose 3 Might, 3 Speed, 3 Knowledge and 3 Sanity if you lose the Amulet.'''

    def on_acquire(self, player):
        player.items.append(self)
        for i in ['speed', 'might', 'sanity', 'knowledge']:
            player.change_stat(i, 1)

    def on_lose(self, player):
        for i in ['speed', 'might', 'sanity', 'knowledge']:
            player.change_stat(i, -1)
        player.items.remove(self)


@name('Angel Feather')
class AngelFeather(Item):
    '''A perfect feather fluttering in your hand. When you attempt a roll of any kind, you can call out a number from 0 to 8. Use that number instead of rolling the dice. Discard this item after you use it.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        num = int(input('Pick a number between 0 and 8: '))

        if num not in range(0, 9):
            print('Invalid choice.')
        else:
            player.items.remove(self)
            return num

    def on_lose(self, player):
        player.items.remove(self)


@name('Armor')
class Armor(Item):
    '''It's just prop armor from a Renaissance Fair, but it's still metal. Any time (not just once per turn) you take physical damage, take one point less of damage. This item can't be stolen.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Axe')
class Axe(Item):
    '''A weapon. Very Sharp. You roll 1 additional die (maximum of 8 dice) when making a Might attack with this weapon. You can't use another weapon while you're using this one.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Blood Dagger')
class BloodDagger(Item):
    '''A nasty weapon. Needles and tubes extend from the handle... and plunge right into your veins. You roll 3 additional dice (maximum of 8 dice) when making a Might attack with this weapon. If you do, lose 1 Speed. You can't use another weapon while you're using this one. This item cannot be traded or dropped. If it's stolen, take 2 dice of physical damage.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        # add 3 dice
        player.change_stat('speed', -1)

    def on_lose(self, player):
        player.items.remove(self)


@name('Bottle')
class Bottle(Item):
    '''An opaque vial containing a black liquid. Once during your turn after the haunt is revealed, you can roll 3 dice and drink from the Bottle. Discard this item after you use it'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        roll = ga.roll_dice(3)

        if roll == 6:
            # TODO choose a room and put your explorer there
            pass
        elif roll == 5:
            player.change_stat('might', 2)
            player.change_stat('speed', 2)
        elif roll == 4:
            player.change_stat('knowledge', 2)
            player.change_stat('sanity', 2)
        elif roll == 3:
            player.change_stat('knowledge', 1)
            player.change_stat('might', -1)
        elif roll == 2:
            player.change_stat('knowledge', -2)
            player.change_stat('sanity', -2)
        elif roll == 1:
            player.change_stat('might', -2)
            player.change_stat('speed', -2)
        else:
            for i in ['speed', 'might', 'sanity', 'knowledge']:
                player.change_stat(i, -2)

        player.items.remove(self)

    def on_lose(self, player):
        player.items.remove(self)


@name('Dark Dice')
class DarkDice(Item):
    '''Are you feeling lucky? Once per turn, you can roll 3 dice'''

    def on_acquire(self, player):
        player.items.append(self)
        self.used = 0

    def on_use(self, player):
        if self.used != 0:
            print('You already used that this turn')
        else:
            roll = ga.roll_dice(3)

            if roll == 6:
                # move to the location of any explorer not revealed as a traitor
                pass
            elif roll == 5:
                # move one other explorer in the same room into an adjacent room
                pass
            elif roll == 4:
                # gain 1 in a physical trait
                pass
            elif roll == 3:
                # immediately move into an adjacent room (no movement cost)
                pass
            elif roll == 2:
                # gain 1 in a mental trait
                pass
            elif roll == 1:
                # draw an event card
                pass
            else:
                # reduce all of your traits to lowest value above the skull symbol. Discard the Dark Dice
                player.items.remove(self)

    def on_lose(self, player):
        player.items.remove(self)
