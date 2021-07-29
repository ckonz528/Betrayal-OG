import game_actions as ga


def add_item(player, item):
    player.items.append(item)


def mad_man(player):
    '''Madman - Gain 2 Might and lose 1 Sanity now. 
    Lose 2 Might and gain 1 Sanity if you lose custody of the Madman. 
    This omen can't be dropped, traded, or stolen.'''

    player.raise_stat('might', 2)
    player.lower_stat('sanity', 1)


def spirit_board(player):
    '''Spirit Board - Before you move during your turn, you can look 
    at the top tile of the room stack. If you use the Spirit Board after
    the haunt has been revealed, the traitor can move any number of 
    monsters 1 space closer to you (if you are the traitor, you don't 
    have to move those monsters). If there is no traitor, all monsters 
    move 1 space closer to you.'''

    pass


def book(player):
    '''Book - Gain 2 Knowledge now. Lose 2 Knowledge if you lose the Book.'''

    player.raise_stat('knowledge', 2)


def skull(player):
    '''If you take mental damage, you can take all of it as physical 
    damage instead.'''

    pass


def spear(player):
    '''Spear - You roll 2 additional dice (maximum 8) when making a Might 
    attack with this weapon. You cannot use another weapon while you're 
    using this one.'''

    pass


def medallion(player):
    '''Medallion - You are immune to the effects of the Pentagram Chamber, 
    Crypt, and Graveyard.'''

    pass


def crystal_ball(player):
    '''Crystal Ball - Once during your turn after the haunt is revealed, 
    you can attempt a Knowledge roll to peer into the Crystal Ball: 
    4+: You see the truth. Search the item or event stack for a card of 
    your choice. Shuffle that stack. Then place that card on top. 
    1-3: You avert your eyes. lose 1 Sanity. 
    0: You stare into Hell. Lose 2 Sanity.'''

    know_roll = ga.stat_roll(player, 'knowledge')

    if know_roll >= 4:
        pass
    elif know_roll == 0:
        player.lower_stat('sanity', 2)
    else:
        player.lower_stat('sanity', 1)


def holy_symbol(player):
    '''Holy Symbol - Gain 2 Sanity now. Lose 2 Sanity if you lose the 
    Holy Symbol.'''

    player.raise_stat('sanity', 2)


def ring(player):
    '''Ring - If you attack an opponent that has a Sanity trait, you can 
    attack with Sanity instead of Might (your opponent defends with Sanity, 
    and damage is mental instead of physical).'''

    pass


def bite(player):
    '''Bite - When you draw this card, the player on your right rolls a 
    Might 4 attack against you. You defend against this attack as normal, 
    by rolling dice equal to your Might. This omen cannot be dropped, traded, 
    or stolen.'''

    might_attack = ga.roll_dice(4)

    might_defend = ga.stat_roll(player, 'might')

    if might_attack - might_defend <= 0:
        pass
    else:
        player.lower_stat('might', might_attack - might_defend)


def mask(player):
    '''Mask - Once during your turn, you can attempt a Sanity roll to use 
    the mask: 4+: You can put on or take off the Mask. 
    If you put on the Mask, gain 2 Knowledge and lose 2 Sanity. 
    If you take off the Mask, gain 2 Sanity and lose 2 Knowledge. 
    0-3: You can't use the Mask this turn.'''

    san_roll = ga.stat_roll(player, 'sanity')

    # TODO: add logic to see if mask is on or off
    if san_roll <= 3:
        pass
    else:
        player.raise_stat('knowledge', 2)
        player.lower_stat('sanity', 2)


def girl(player):
    '''Girl - Gain 1 Sanity and 1 Knowledge now. Lose 1 Sanity and 1 
    Knowledge if you lose custody of the Girl. This omen cannot be dropped, 
    traded, or stolen.'''

    player.raise_stat('sanity', 1)
    player.raise_stat('knowledge', 1)


def dog(player):
    '''Dog - Gain 1 Might and 1 Sanity now. Lose 1 Might and 1 Sanity if 
    you lose custody of the Dog. Take a small monster token to represent 
    the Dog. Put it in your room. Once during your turn, the Dog can move 
    to any explored room up to 6 spaces away, using doors and stairs, and 
    then return. It can pick up, carry, and or drop 1 item before it returns. 
    The Dog isn't slowed by opponents. It can't use one-way passages or rooms 
    that require a roll. It can't carry items that slow movement. This omen 
    cannot be dropped, traded, or stolen.'''

    pass
