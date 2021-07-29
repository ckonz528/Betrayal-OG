import random as r


def roll_dice(num_rolls):
    die = [0, 0, 1, 1, 2, 2]

    # can only roll max of 8 dice
    if num_rolls > 8:
        num_rolls = 8

    rolls = []
    for i in range(num_rolls):
        rolls.append(r.choice(die))

    return sum(rolls)


def stat_roll(player, stat):
    bar, pos = player.stats[stat]
    num_dice = bar[pos]

    return roll_dice(num_dice)


def haunt_roll():
    return roll_dice(6)
