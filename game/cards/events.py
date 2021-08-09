from .. import game_actions as ga

# TODO: add discards to all


def a_moment_of_hope(current_tile):
    print('A MOMENT OF HOPE - Something feels strangely right about this room. Something is resisting the evil of the house.')

    current_tile.tokens.append('Blessing')
    print('A Blessing has been placed in this room. Each hero rolls 1 additional die (maximum of 8 dice) on all trait rolls while in this room.')
    # each hero rolls 1 additional die on all trait rolls in this room


def angry_being(player):
    print('ANGRY BEING - It emerges from the slime on the wall next to you. You must attempt a speed roll.')

    speed_roll = ga.stat_roll(player, 'speed')

    if speed_roll >= 5:
        print('You get away. Gain 1 speed.')
        player.change_stat('speed', 1)
    elif speed_roll >= 2 and speed_roll <= 4:
        print('Take 1 die of mental damage.')
        roll = ga.roll_dice(1)
        player.change_mental(-roll)
    else:
        print('Take 1 die of mental damage and 1 die of physical damage.')
        phys_roll = ga.roll_dice(1)
        player.change_physical(-phys_roll)

        mental_roll = ga.roll_dice(1)
        player.change_mental(-mental_roll)


def bloody_vision(player):
    print('BLOODY VISION - The walls of this room are damp with blood. The blood drips from the ceiling, down the walls, over the furniture, and onto your shoes. In a blink it is gone. You must attempt a sanity roll.')

    san_roll = ga.stat_roll(player, 'sanity')

    if san_roll >= 5:
        print('You steel yourself. Gain 1 sanity.')
        player.change_stat('sanity', 1)
    elif san_roll == 2 or san_roll == 3:
        print('Lose 1 sanity.')
        player.change_stat('sanity', -1)
    else:
        print('If an explorer or monster is in your room or an adjacent one, you must attack it(if you can). Choose the explorer with the lowest might if possible.')
        pass
