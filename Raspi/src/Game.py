"""
Game Outline:

    I. Initialization Routine:
        a. Read Information from the configuration file with
        the parser.

        b. Create game schedule.
            i. Create Category Objects with the following properties:
                1. Category ID
                2. Name
                3. Number of questions
                4. Numbers of points per correct answer.
                5. Number of points per partial-points answer.
        c. Create Teams
            i. Name
            ii. Players
                1. Player ID
                2. Name
                3. Score sheet
            iii. Score Sheet
    II. Start Game Loop
"""

#Imports
from gameObjects.GameSchedule import *
from gameObjects.Category import *
from gameObjects.Player import *
from gameObjects.Team import *
import hardware
import os


#Definition of Global Variables
gameInfo = ''
schedule = ''
teams = ''
gs = 0
currentCategory = ''
currentQuestion = 0

#Definition of game methods
"""
    TODO:
    1. Create a module to visualize game.
"""
def initialization():
    import json
    #Open File
    try:
        gameFile = open('configuration/gameConfiguration.config')
    except IOError():
            print 'The configuration file was not found or was corrupted.'
            raise IOError('Bad config file')
    except:
            print 'Somthing Happened.'
            raise Exception('IDK -- fix it.')

    # Parse out actual infro from instructions.
    plainText = gameFile.read()
    start = plainText.find('#start')+6
    end = plainText.find('#stop')

    configInfo = plainText[start:end]

    global gameInfo
    gameInfo = json.loads(configInfo)

    initGameSchedule()
    initTeams()
    global schedule
    schedule.sort()

    global currentCategory
    global currentQuestion
    currentCategory = 0
    currentQuestion = 0



def initGameSchedule():
    global gameInfo
    global schedule

    schedule = GameSchedule()
    #add categories
    for cat in gameInfo['schedule']['categories']:
        category = Category(cat['name'], int(cat['numberOfQuestions']), int(cat['full_points']), int(cat['partial_points']), int(cat['penalty_points']))
        schedule.append(category)
        schedule.sort()

def initTeams():
    global teams
    teams = []
    Team.setSchedule(schedule)
    for t in gameInfo['teams']:
        team = Team(t['name'])
        for p in t['players']:
            player = Player(p['name'], bool(p['engagement']))
            team.addPlayer(player)
        teams.append(team)
    if not len(teams)==2:
        raise Exception('Invalid Number of Teams')


def gamesState():
    global gs

    #Unbuzzed and waiting for input from either the user or moderator.
    if gs == 0:
        #To be implemented.
        pass

    #Buzzed and waiting for moderator input.
    elif gs == 1:
        #To be implemented.
        pass
    #Unbuzzed with Timer
    elif gs == 2:
        #To be implemented.
        pass
    #Buzzed with Timer
    elif gs == 3:
        #TBI
        pass

#Running The File :
initialization()

while currentCategory < len(schedule):
    #Gameloop code goes here.
    break


os.system('rm ./gameObjects/*.pyc; rm ./hardware/*.pyc')
