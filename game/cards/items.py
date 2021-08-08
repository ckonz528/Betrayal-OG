from . import Item, CardRegistry
from .. import game_actions as ga

name = CardRegistry()


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
    '''Ancient silver and inlaid gems inscribed with blessings.
    Gain 1 Might, 1 Speed, 1 Knowledge and 1 Sanity now.
    Lose 3 Might, 3 Speed, 3 Knowledge and 3 Sanity if you lose the Amulet.'''

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
    '''A perfect feather fluttering in your hand.
    When you attempt a roll of any kind, you can call out a number from 0 to 8.
    Use that number instead of rolling the dice.
    Discard this item after you use it.'''

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
    '''It's just prop armor from a Renaissance Fair, but it's still metal.
    Any time (not just once per turn) you take physical damage,
    take one point less of damage. This item can't be stolen.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Axe')
class Axe(Item):
    '''A weapon. Very Sharp. You roll 1 additional die (maximum of 8 dice)
    when making a Might attack with this weapon.
    You can't use another weapon while you're using this one.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Blood Dagger')
class BloodDagger(Item):
    '''A nasty weapon. Needles and tubes extend from the handle...
    and plunge right into your veins. You roll 3 additional dice
    (maximum of 8 dice) when making a Might attack with this weapon.
    If you do, lose 1 Speed. You can't use another weapon while you're using this one.
    This item cannot be traded or dropped. If it's stolen, take 2 dice of physical damage.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        # add 3 dice
        player.change_stat('speed', -1)

    def on_lose(self, player):
        player.items.remove(self)


@name('Bottle')
class Bottle(Item):
    '''An opaque vial containing a black liquid. Once during your turn after the haunt is revealed, you can roll 3 dice and drink from the Bottle. Discard this item after you use it.'''

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
    '''Are you feeling lucky? Once per turn, you can roll 3 dice.'''

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


@name('Dynamite')
class Dynamite(Item):
    '''The fuse isn't lit... yet. Instead of attacking, you can throw the Dynamite through a connecting door into an adjacent room. Each explorer and monster with Might and Speed traits in that room must attempt a Speed roll. Discard this item after you use it.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):

        speed_roll = ga.stat_roll(player, 'speed')

        if speed_roll >= 5:
            pass
        else:
            player.change_pysical(4)

        player.items.remove(self)

    def on_lose(self, player):
        player.items.remove(self)


@name('Healing Salve')
class HealingSalve(Item):
    '''A sticky paste in a shallow bowl. You can apply the Healing Salve to yourself or to another living explorer in the same room. If that explorer's Might or Speed is below it's starting value, raise one or both to its starting value. Discard this item after you use it.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        # TODO: add ability to use on another player
        speed_change = input(
            f'Return speed to starting value? ({player.base[0]}) (y/n)')

        if speed_change.lower() == 'y':
            player.stats['speed'] = (player.stats['speed'][0], player.base[0])

        might_change = input(
            f'Return might to starting value? ({player.base[1]}) (y/n)')

        if might_change.lower() == 'y':
            player.stats['might'] = (player.stats['might'][0], player.base[1])

        player.items.remove(self)

    def on_lose(self, player):
        player.items.remove(self)


@name('Idol')
class Idol(Item):
    '''Once per turn, you can rub the Idol before making any trait, combat, or event roll to add 2 dice to the roll (a maximum of 8 dice). Each time you do, you lose one sanity'''

    def on_acquire(self, player):
        player.items.append(self)
        self.used = 0

    def on_use(self, player):
        if self.used == 1:
            pass
        else:
            player.change_stat('sanity', -1)

    def on_lose(self, player):
        player.items.remove(self)


@name('Lucky Stone')
class LuckyStone(Item):
    '''A smooth, ordinary-looking rock. You sense it will bring you good fortune. After you attempt a roll of any kind, you can rub the stone once to reroll any number of those dice. Discard this item after you use it.'''

    def on_acquire(self, player):
        player.items.append(self)

    def on_use(self, player):
        # TODO: add logic to make sure no more dice are rolled than the original number of dice

        num_dice = int(input('Reroll how many dice? '))

        new_roll = ga.roll_dice(num_dice)

        player.items.remove(self)

        return new_roll

    def on_lose(self, player):
        player.items.remove(self)


@name('Medical Kit')
class MedicalKit(Item):
    '''A doctor's bag, depleted in some critical resources. Once during your turn, you can attempt a Knowledge roll to heal yourself or another explorer in the same room. You can't raise a trait above its starting value with the Medical Kit.'''

    def on_acquire(self, player):
        player.items.append(self)
        self.used = 0

    def on_use(self, player):
        if self.used != 0:
            print('You already used that!')
        else:
            # TODO: add logic to use on another player
            know_roll = ga.stat_roll(player, 'knowledge')

            # TODO: don't raise above starting value
            if know_roll >= 8:
                player.change_physical(3)
            elif know_roll == 6 or know_roll == 7:
                player.change_physical(2)
            elif know_roll == 4 or know_roll == 5:
                player.change_physical(1)
            else:
                pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Music Box')
class MusicBox(Item):
    '''A hand-crafted antique. It plays a haunting melody that gets stuck in your head. Once per turn, you can open or close the music box. While the Music Box is open, any explorer or monster with a Sanity trait that enters or starts in the same room (as the box) must make a sanity roll of 4+. If the roll fails, the explorer or monster ends its turn as it is mesmerized by the music. If the explorer or monster carrying the music box becomes mesmerized, they drop the Music Box. If the Music Box was open when it was dropped, and it remains open.'''

    def on_acquire(self, player):
        player.items.append(self)
        self.open = 0
        self.used = 0

    def on_use(self, player):
        if self.used != 0:
            pass
        else:
            pass

    def on_lose(self, player):
        player.items.remove(self)


@name('Puzzle Box')
class PuzzleBox(Item):
    '''There must be a way to open it. Once during your turn, you can attempt a knowledge roll to open the box.'''

    def on_acquire(self, player):
        player.items.append(self)
        self.used = 0

    def on_use(self, player):
        if self.used != 0:
            pass
        else:
            know_roll = ga.stat_roll(player, 'knowledge')

            if know_roll < 6:
                print("You just can't get it open")
            else:
                # TODO: draw 2 item cards
                player.items.remove(self)

    def on_lose(self, player):
        player.items.remove(self)
