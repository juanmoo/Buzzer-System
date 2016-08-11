from ScoreSheet import *
from GameSchedule import *

"""
Before creating a player the class schedule variable must be defined.
To define one use the following syntax where schedule is an instance of
the GameSchedule class:
    Player.setSchedule(schedule)
"""

class Player(object):
    next_player_id = 0
    schedule = ''

    @staticmethod
    def setSchedule(schedule):
        assert isinstance(schedule, GameSchedule)
        Player.schedule = schedule

    def __init__(self, name, initial_state):
        if Player.schedule == '':
            print '\n\n\n'
            print "The schedule for the Player class has not been defined."
            print "Use the Player.setSchedule(schedule) method define one."
            print '\n\n\n'
            raise Exception('*** Schedule Not Defined ***')
        self.player_id = Player.next_player_id
        Player.next_player_id += 1

        self.name = name
        self.sheet = ScoreSheet(Player.schedule)
        #Active Players will have a True state attribute.
        self.state = initial_state

    def getName(self):
        return self.name
