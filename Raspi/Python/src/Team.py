from Player import *
from GameSchedule import *
from Category import *

class Team(object):
    next_team_id = 0
    schedule = ''

    @staticmethod
    def setSchedule(schedule):
        assert isinstance(schedule, GameSchedule)
        Team.schedule = schedule

    def __init__(self, name):
        if Team.schedule == '':
            print '\n\n\n'
            print "The schedule for the Team class has not been defined."
            print "Use the Team.setSchedule(schedule) method define one."
            print '\n\n\n'
            raise Exception('*** Schedule Not Defined ***')
        else:
            Player.setSchedule(Team.schedule)
        self.team_id = Team.next_team_id
        Team.next_team_id += 1

        self.name = name
        self.active_players = list()
        self.unactive_players = list()
        self.offset = 0

    def addPlayer(self, player):
        assert isinstance(player, Player)
        if player.state == True:
            self.active_players.append(player)
        else:
            self.unactive_players.append(player)
        if len(self.active_players) > 4 or len(self.active_players) <= 0:
            print "\n\nThe number of active_players must be between 1 and 4.\n\n"
            raise Exception('*** Invalid Number of Active Players ***')

    def swapPlayers(self, player1, player2):
        if not ((player1 in self.active_players or player1 in self.unactive_players) and (player2 in self.active_players or player2 in self.unactive_players)):
            raise Exception('At least one of the two players is not on the team.')
        #Count the number of players in active_players
        players = [player1, player2]
        in_active = 0
        for player in players:
            if player in self.active_players:
                in_active += 1

        #Both players in active_players
        if (in_active == 2):
            p1_index = self.active_players.index(player1)
            p2_index = self.active_players.index(player2)
            self.active_players[p1_index] = player2
            self.active_players[p2_index] = player1
        #One player in active_players
        elif (in_active == 1):
            if player2 in self.active_players:
                temp = player1
                player1 = player2
                player2 = temp
        p1_index = self.active_players.index(player1)
        p2_index = self.unactive_players.index(player2)
        self.active_players[p1_index] = player2
        self.unactive_players[p2_index] = player1
        for player in players:
            player.state = not player.state
        #No on is in active_players
        else:
            pass

    def calculateScore(self, category):
        assert isinstance(category, Category)
        players = []
        for player in self.active_players:
            players.append(player)
        for player in self.unactive_players:
            players.append(player)
        total = 0
        for player in players:
            total += player.sheet.calculateScore(category)
        return total

    def calculateTotalScore(self):
        total = 0
        for category in Team.schedule:
            total += self.calculateScore(category)
        total += self.offset
        return total
