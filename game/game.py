from .gameboard import Gameboard, Tile
import game.settings as s
import json
from .player import Player
import random as r
from typing import Any, Dict, List, Tuple
from .cards.items import name, BloodDagger, Bottle


class Game:
    def __init__(self):
        # load tiles
        tiles: Dict[str, Any] = json.load(
            open(s.get_path('assets', 'data/rooms.json')))
        self.rooms: Dict[str, Tile] = {room_info['name']: Tile(
            room_info) for room_info in tiles}

        # create floors
        self.floors: Dict[str, Gameboard] = {'ground': Gameboard(), 'basement': Gameboard(),
                                             'upper': Gameboard()}

        # set up initial tiles
        start_tiles: List[Tuple[int, str]] = [(4, 'Entrance Hall'), (3, 'Foyer'),
                                              (2, 'Grand Staircase')]
        for x, room in start_tiles:
            self.floors['ground'].place_tile(self.rooms[room], (x, 1))
            del self.rooms[room]

        self.floors['upper'].place_tile(self.rooms['Upper Landing'], (2, 1))
        del self.rooms['Upper Landing']

        self.floors['basement'].place_tile(
            self.rooms['Basement Landing'], (2, 1))
        del self.rooms['Basement Landing']

        # none of the initial tiles can be rotated
        for floor in self.floors.keys():
            self.floors[floor].recent_pos = None

        # shuffle deck
        self.room_keys: List[str] = list(self.rooms.keys())
        r.shuffle(self.room_keys)

        # load player info
        players: Dict[str, Any] = json.load(
            open(s.get_path('assets', 'data/players.json')))
        self.players: Dict[str, Player] = {
            player_info['name']: Player(player_info, self) for player_info in players}

        # test hero
        # TODO: replace with user-selected characters
        # TODO: figure out how to do turns?
        self.hero: Player = self.players['Peter Akimoto']
        self.floors['ground'].players = [self.hero]

        self.running: bool = True
