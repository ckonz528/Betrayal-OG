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


def menu(options):
    assert len(options) > 0
    while True:
        print('Please select an option:')
        for i, option in enumerate(options):
            print(f'\t{i + 1} - {option}')
        selected = int(input('Enter choice: '))
        if selected < 0 or selected > len(options):
            continue

        return selected - 1, options[selected - 1]
