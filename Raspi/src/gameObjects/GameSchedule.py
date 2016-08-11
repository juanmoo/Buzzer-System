from Category import *

class GameSchedule(list):
    def append(self, thing):
        assert isinstance(thing, Category), ("Can not append "+str(thing)+" to the GameSchedule \nbecause "+str(thing)+" is not a category.")
        super(GameSchedule, self).append(thing)

    def insert(self, index, thing):
        assert isinstance(thing, Category), ("Can not append "+str(thing)+" to the GameSchedule \nbecause "+str(thing)+" is not a category.")
        super(GameSchedule, self).insert(index, thing)
